import json
import requests
from config import keys


class APIException(Exception):
    pass


class Convert:
    @staticmethod
    def get_price(f, t, a):
        try:
            f_key = keys[f.lower()]
        except Exception:
            raise APIException(f'Валюта {f} не найдена')

        try:
            t_key = keys[t.lower()]
        except Exception:
            raise APIException(f'Валюта {t} не найдена')

        if f_key == t_key:
            raise APIException(f'Введите разные валюты')

        try:
            a = float(a)
        except Exception:
            raise APIException(f'Неверное количество {a}')

        url = f'https://api.apilayer.com/exchangerates_data/convert?to={t_key}&from={f_key}&amount={a}'
        r = requests.get(url, {'apikey': '5qlYdXn2Hn1M5MsF1jRw6OGlh6432OIX'})
        resp = json.loads(r.content)
        text = f"{a} {f} = {resp['result']} {t}"
        return text
