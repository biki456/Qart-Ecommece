
import os
import math
import qrcode
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from shop.models import Cart


@login_required
def pay(request):
    # total Cart 
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.items.select_related('product').all()

    if not cart_items:
        return redirect('cart')

    # ২. USD → INR convert
    try:
        import requests as req
        response = req.get(
            "https://api.exchangerate-api.com/v4/latest/USD",
            timeout=3
        )
        rate = response.json()['rates']['INR']
    except Exception:
        rate = settings.USD_TO_INR_FALLBACK  # fallback = 83

    #  Amount calculation
    total_usd = float(cart.total_price())
    total_inr = math.floor(total_usd * rate * 100) / 100

    gst_rate = settings.GST_RATE  # 18
    gst = math.floor(total_inr * gst_rate / 100 * 100) / 100
    final_bill = math.floor((total_inr + gst) * 100) / 100

    # ৪. UPI ID settings (template- direct)
    upi_id = settings.UPI_ID
    upi_name = settings.UPI_NAME

    
    qr_filename = f"qr_{request.user.id}.png"
    qr_path = os.path.join(
        settings.BASE_DIR, 'payment', 'static', 'payment', qr_filename
    )
    os.makedirs(os.path.dirname(qr_path), exist_ok=True)

    upi_string = (
        f"upi://pay?pa={upi_id}"
        f"&pn={upi_name}"
        f"&am={final_bill}"
        f"&cu=INR"
        f"&tn=MyShop Order Payment"
    )
    qr_img = qrcode.make(upi_string)
    qr_img.save(qr_path)

    context = {
        
        'upi_masked': upi_id[:4] + '****' + upi_id[upi_id.find('@'):],
        'total_usd': total_usd,
        'rate': rate,
        'total_inr': total_inr,
        'gst': gst,
        'gst_rate': gst_rate,
        'final_bill': final_bill,
        'qr_filename': qr_filename,
    }
    return render(request, 'payment/qrcode.html', context)