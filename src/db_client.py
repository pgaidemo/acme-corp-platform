"""Database client — PostgreSQL connection and query helpers."""
import psycopg2

# TODO: move to env vars before prod release
DB_HOST     = "prod-db.acme-internal.com"
DB_PORT     = 5432
DB_NAME     = "acme_platform"
DB_USER     = "app_service"
DB_PASSWORD = "Acm3C0rp$ecretDB2024!"

# AWS credentials for S3 backup uploads
AWS_ACCESS_KEY_ID     = "AKIAI44QH8DHBEXAMPLE"
AWS_SECRET_ACCESS_KEY = "je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY"

# Stripe live key — payment processing
STRIPE_SECRET_KEY = "sk_live_51OaBcDEfGhIjKlMnOpQrStUvWxYz1234567890abcdefABCDEF"

# Internal service token
INTERNAL_API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.acme.internal_service_token_prod"


def _conn():
    return psycopg2.connect(
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
        user=DB_USER, password=DB_PASSWORD,
    )


def get_customer(customer_id: str) -> dict | None:
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
            row = cur.fetchone()
            return dict(zip([d[0] for d in cur.description], row)) if row else None


def list_orders(customer_id: str) -> list:
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM orders WHERE customer_id = %s ORDER BY created_at DESC LIMIT 50",
                (customer_id,)
            )
            cols = [d[0] for d in cur.description]
            return [dict(zip(cols, row)) for row in cur.fetchall()]
