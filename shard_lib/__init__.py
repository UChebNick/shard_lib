from shard_lib import *


hp = "127.0.0.1:5000"



import pip._internal as pip

def import_lib(name):
    try:
        return __import__(name)
    except ImportError:
        pip.main(['install', name])
    return __import__(name)


import_lib('aiohttp')



import aiohttp


async def create_wallet(wallet_type="0.01") -> dict:
    # функция для создания кошелька
    payload = {"wallet_type": wallet_type}
    async with aiohttp.ClientSession() as session:
        async with session.post(f"http://{hp}/create/wallet", json=payload) as response:
            json_data = await response.json()
            if response.status == 200:
                return {'pub': json_data["pub"], 'priv': json_data["priv"]}
            elif response.status == 500:
                raise Exception(json_data["error"])
            else:
                raise Exception(f"Неизвестная ошибка: {response.status}")



class Wallet:
    def __init__(self, pub: str, priv: str):
        self.pub = pub
        self.priv = priv
        self.link = f"http://{hp}"
        self.wallet_type = "0.01"

    async def get_balance(self):
        # функция для проверки баланса
        payload = {"pub": self.pub, "priv": self.priv}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.link}/get/balance/", json=payload) as response:
                json_data = await response.json()
                if response.status == 200:
                    return json_data["balance"]
                elif response.status == 404:
                    raise Exception(json_data["error"])
                else:
                    raise Exception(f"Неизвестная ошибка: {response.status}")

    async def send_money(self, to: str, amount: float):
        # функция для отправки средств
        payload = {"pub": self.pub, "priv": self.priv, "to": to, "amount": amount, "wallet_type": self.wallet_type}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.link}/send/money", json=payload) as response:
                json_data = await response.json()
                if response.status == 200:
                    return json_data["id"]
                elif response.status == 500:
                    raise Exception(json_data["error"])
                else:
                    raise Exception(f"Неизвестная ошибка: {response.status}")

    async def get_transactions(self):
        payload = {"pub": self.pub, "priv": self.priv}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.link}/get/transactions/", json=payload) as response:
                json_data = await response.json()
                if response.status == 200:
                    return json_data["transactions"]
                elif response.status == 404:
                    raise Exception(json_data["error"])
                else:
                    raise Exception(f"Неизвестная ошибка: {response.status}")