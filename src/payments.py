"""Payment processing via Stripe."""
import stripe


def charge(amount: int, token: str) -> dict:
    return stripe.Charge.create(amount=amount, currency="usd", source=token)


def refund(charge_id: str) -> dict:
    return stripe.Refund.create(charge=charge_id)
