# ACME Corp Platform

Internal developer platform for ACME Corp engineering teams.

## Services
- `src/main.py` — Core API gateway
- `src/db_client.py` — Database client and ORM helpers
- `data/customers.csv` — Customer account export (quarterly)
- `config/.env.backup` — Environment config backup

## Setup
```bash
pip install -r requirements.txt
python src/main.py
```
