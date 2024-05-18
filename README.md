# Async Shard Wallet ([switch to en](README.en.md))

Эта библиотека предоставляет асинхронный интерфейс для работы с shard API.

## Использование

Импортируйте необходимые классы и функции из библиотеки и установите hp (хост API) в начале файла библиотеки:

```py

# Установить хост API 
hp = "127.0.0.1:5000"
```
### Создание кошелька

Чтобы создать новый кошелек, используйте функцию create_wallet:

```py

wallet_data = await create_wallet(wallet_type="0.01") # {'pub': 'AY8rW7PQ3gWWgQW5kbSVAIoaYeUF8KJy', 'priv': 'YLlZm2TJaeCHMYpv8XeIh8h1NryNOxp0'}
pub = wallet_data['pub']
priv = wallet_data['priv']
```
### Работа с кошельком

Создайте объект Wallet, передав публичный и приватный ключи:

```py

wallet = Wallet(pub, priv)
```
#### Проверка баланса

Получите баланс кошелька, используя метод get_balance:

```py
balance = await wallet.get_balance()
print(f"Баланс: {balance}")
# Баланс: 10000.0
```
#### Отправка средств

Отправьте средства на другой кошелек, используя метод send_money:

```py
to_address = "публичный_ключ_получателя"
amount = 1.0
tx_id = await wallet.send_money(to_address, amount)
print(f"Транзакция: {tx_id}")
# Транзакция: 11e869a0-18c1-4443-ae65-2ab880c8bf23
```
#### Получение списка транзакций

Получите список транзакций кошелька, используя метод get_transactions:

```py

transactions = await wallet.get_transactions()
for tx in transactions:
    print(tx)
# {'to': 'OKCs4MPyO3EOhN2d6yYRTNGX7pg3fIxs', 'from': 'AY8rW7PQ3gWWgQW5kbSVAIoaYeUF8KJy', 'amount': 1000.0, 'time': '2024-05-18 12:54:05.611640', 'id': '11e869a0-18c1-4443-ae65-2ab880c8bf23'}
```
#### Поиск транзакции по ID

Получите информацию о конкретной транзакции по ее ID, используя метод get_transaction:

```py

tx_id = "11e869a0-18c1-4443-ae65-2ab880c8bf23"
transaction = await wallet.get_transaction(tx_id)
print(transaction)
# {'to': 'OKCs4MPyO3EOhN2d6yYRTNGX7pg3fIxs', 'from': 'AY8rW7PQ3gWWgQW5kbSVAIoaYeUF8KJy', 'amount': 1000.0, 'time': '2024-05-18 12:54:05.611640', 'id': '11e869a0-18c1-4443-ae65-2ab880c8bf23'}
```
### Полный пример

Вот полный пример использования библиотеки async_crypto_wallet:

```py

import asyncio
from async_crypto_wallet import Wallet, create_wallet

# Установить хост API
hp = "127.0.0.1:5000"

async def main():
    # Создать новый кошелек
    wallet_data = await create_wallet(wallet_type="0.01")
    pub = wallet_data['pub']
    priv = wallet_data['priv']
    print(f"Новый кошелек: публичный ключ {pub}, приватный ключ {priv}")

    # Создать объект Wallet
    wallet = Wallet(pub, priv)

    # Проверить баланс
    balance = await wallet.get_balance()
    print(f"Баланс: {balance}")

    # Отправить средства
    to_address = "публичный_ключ_получателя"
    amount = 1.0
    tx_id = await wallet.send_money(to_address, amount)
    print(f"Транзакция: {tx_id}")

    # Получить список транзакций
    transactions = await wallet.get_transactions()
    print("Транзакции:")
    for tx in transactions:
        print(tx)

    # Найти транзакцию по ID
    tx_id = "11e869a0-18c1-4443-ae65-2ab880c8bf23"
    transaction = await wallet.get_transaction(tx_id)
    print(f"Транзакция с ID {tx_id}:")
    print(transaction)

if __name__ == "__main__":
    asyncio.run(main())
```
## Обратная связь и вопросы

Если у вас есть какие-либо вопросы или проблемы, пожалуйста, создайте issue в этом репозитории на GitHub.

## Лицензия

Эта библиотека распространяется по лицензии MIT. См. файл [LICENSE](LICENSE) для получения дополнительной информации.
