"""ACME Corp API Gateway — core routing and request handling."""
from flask import Flask, request, jsonify
from db_client import get_customer, list_orders

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({"status": "ok", "version": "2.4.1"})


@app.route("/api/customers/<customer_id>")
def customer(customer_id):
    record = get_customer(customer_id)
    if not record:
        return jsonify({"error": "not found"}), 404
    return jsonify(record)


@app.route("/api/orders")
def orders():
    customer_id = request.args.get("customer_id")
    return jsonify(list_orders(customer_id))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
