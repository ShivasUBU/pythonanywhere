from pypromptpay import qr_code
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def genQR(oid, phone, price):
    path = BASE_DIR / f'static/qr/{oid}.png'
    qr_code(phone, one_time=False, path_qr_code=path, country="TH", money=str(price), currency="THB")
