from pprint import pprint

import stripe
import os


def create_paymentintent(amount):
    paymentinrtent = stripe.PaymentIntent.create(
      amount=amount,
      currency="usd",
      automatic_payment_methods={"enabled": True},
    )
    pprint(paymentinrtent)


def retrieve_paymentintent(paymentintent: dict) -> dict:
    paymentintent = stripe.PaymentIntent.retrieve(
        paymentintent['id'],
    )
    return paymentintent


def create_product(product_name):
    product = stripe.Product.create(name=product_name)
    return product


def create_price(product: dict, amount: int) -> dict:
    price = stripe.Price.create(
        unit_amount=amount*100,
        currency="usd",
        recurring={"interval": "month"},
        product=product['id'],
    )
    return price


def create_session(price):
    stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price": price['id'],
                "quantity": 2,
            },
        ],
        mode="payment",
    )

if __name__ == '__main__':
    stripe.api_key = 'sk_test_51O2c0uFMQDI9oh75w91rNgYPh7SKEUkuNnV1ltENUSwgUVqvvyXNtyMnKNsvbcbYndL6OwhtmF26EfHVHC0xV74L00r8iBB8Q0'

    customer = stripe.Customer.retrieve(
        'cus_OqV3Ayih4uZvqx',
        api_key=os.getenv('STRIPE_API_KEY')
    )
    customer.capture()
    product = create_product('F')
    price = create_price(product, 200)
    session = create_session(price)
    pprint(session)
