from django.shortcuts import render, redirect
from .models import Pizza
from django.contrib import messages

def pizza_list(request):
    pizzas = Pizza.objects.all()
    return render(request, 'menu/pizza_list.html', {'pizzas': pizzas})

def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_price = request.POST.get('item_price')
        cart = request.session.get('cart', [])

        cart.append({'name': item_name, 'price': float(item_price)})
        request.session['cart'] = cart
        return redirect('pizza_list')  # <- moved this inside the if block!

def view_cart(request):
    cart = request.session.get('cart', [])
    subtotal = sum(item['price'] for item in cart)
    tax_rate = 0.13  # 13% HST
    tax = round(subtotal * tax_rate, 2)
    total = round(subtotal + tax, 2)

    return render(request, 'menu/cart.html', {
        'cart': cart,
        'subtotal': subtotal,
        'tax': tax,
        'total': total
    })

def remove_from_cart(request):
    if request.method == 'POST':
        item_index = int(request.POST.get('item_index'))
        cart = request.session.get('cart', [])

        if 0 <= item_index < len(cart):
            del cart[item_index]
            request.session['cart'] = cart

    return redirect('view_cart')

def terms(request):
    return render(request, 'menu/terms.html')

def process_special_instructions(request):
    if request.method == 'POST':
        option = request.POST.get('special_option')
        custom_note = request.POST.get('custom_instructions', '')

        # Optionally save this to session, database, or cart model
        request.session['special_option'] = option
        request.session['custom_note'] = custom_note

        # Example logic
        if option == 'add_topping':
            messages.info(request, "Topping added. $1.50 will be charged.")
            # You could increase total price here if needed
        elif option == 'remove_item':
            messages.info(request, "Ingredient removal noted.")
        elif custom_note:
            messages.info(request, "Special instructions received.")
        else:
            messages.warning(request, "No instructions provided.")
            
    return redirect('view_cart')

def proceed_to_payment(request):
    if request.method == 'POST':
       
        payment_method = request.POST.get('payment-method')
       
        return render(request, 'menu/proceed_to_payment.html', {'payment_method': payment_method})
    return redirect('view_cart')  # Fallback
