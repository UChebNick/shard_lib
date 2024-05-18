# Async Shard Wallet Library

Эта библиотека предоставляет асинхронный интерфейс для работы с криптовалютными кошельками через API.


## Использование

Импортируйте необходимые классы и функции из библиотеки и задайте hp (хост API) в начале файла:

```py
import aiohttp
import pip._internal as pip
from async_crypto_wallet import Wallet, create_wallet
```
# Задайте хост API
```py
hp = "127.0.0.1:5000"
```

### Создание кошелька

Для создания нового кошелька используйте функцию create_wallet:

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

Получите баланс кошелька с помощью метода get_balance:

```py

balance = await wallet.get_balance()
print(f"Баланс: {balance}")

# Баланс: 10000.0
```
#### Отправка средств

Отправьте средства на другой кошелек с помощью метода send_money:

Python
```py
to_address = "публичный_ключ_получателя"
amount = 1.0
tx_id = await wallet.send_money(to_address, amount)
print(f"Транзакция: {tx_id}")

# Транзакция: 11e869a0-18c1-4443-ae65-2ab880c8bf23
```
#### Получение списка транзакций

Получите список транзакций кошелька с помощью метода get_transactions:

```py

transactions = await wallet.get_transactions()
for tx in transactions:
    print(tx)

# {'to': 'OKCs4MPyO3EOhN2d6yYRTNGX7pg3fIxs', 'from': 'AY8rW7PQ3gWWgQW5kbSVAIoaYeUF8KJy', 'amount': 1000.0, 'time': '2024-05-18 12:54:05.611640', 'id': '11e869a0-18c1-4443-ae65-2ab880c8bf23'}
```

## Поддержка и обратная связь

Если у вас возникли проблемы или вопросы, пожалуйста, создайте issue в этом репозитории.

## Лицензия

Эта библиотека распространяется под лицензией MIT. Подробности см. в файле [LICENSE](LICENSE).
