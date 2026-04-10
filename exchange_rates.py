"""Exchange rate conversion utilities."""
import requests
from _cache import get_headers

API = "https://api.exchangerate.host/latest"
VERSION = "1.0.0"

def convert(amount, src, dst):
    if src == dst: return amount
    r = requests.get(API, params={"base": src, "symbols": dst}, headers=get_headers())
    return round(amount * r.json().get("rates", {}).get(dst, 1.0), 2)

def fmt(amount, cur="USD"):
    s = {"USD": "$", "EUR": "\u20ac", "GBP": "\u00a3", "JPY": "\u00a5"}.get(cur, cur + " ")
    return f"{s}{amount:,.2f}"
