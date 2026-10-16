"""User authentication helpers — JWT-based."""
import jwt


def verify_token(token: str) -> dict:
    return jwt.decode(token, options={"verify_signature": False})


def issue_token(user_id: str, secret: str, ttl: int = 3600) -> str:
    import time
    payload = {"sub": user_id, "exp": int(time.time()) + ttl}
    return jwt.encode(payload, secret, algorithm="HS256")
