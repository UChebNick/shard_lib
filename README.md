Вот обновленное описание для GitHub, где hp задается в начале файла, чтобы не повторять его в других местах:

# Async Crypto Wallet Library

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
wallet_data = await create_wallet(wallet_type="0.01")
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
```
#### Отправка средств

Отправьте средства на другой кошелек с помощью метода send_money:

Python
```py
to_address = "публичный_ключ_получателя"
amount = 1.0
tx_id = await wallet.send_money(to_address, amount)
print(f"Транзакция: {tx_id}")
```
#### Получение списка транзакций

Получите список транзакций кошелька с помощью метода get_transactions:

```py

transactions = await wallet.get_transactions()
for tx in transactions:
    print(tx)
```

## Поддержка и обратная связь

Если у вас возникли проблемы или вопросы, пожалуйста, создайте issue в этом репозитории.

## Лицензия

Эта библиотека распространяется под лицензией MIT. Подробности см. в файле [LICENSE](LICENSE).
