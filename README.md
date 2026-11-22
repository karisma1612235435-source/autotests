# Автотесты UI и API — Python + Pytest + Playwright

Автоматизация проверки веб-приложений через UI и API на примере учебных площадок [automationexercise.com](https://automationexercise.com) и [saucedemo.com](https://www.saucedemo.com).

## Что покрыто

**automationexercise.com (UI + API):**
- регистрация нового пользователя через UI;
- создание тестового аккаунта через API (фикстура `reg`) и удаление его после теста;
- логин: позитивный и негативный сценарии;
- выбор товаров, корзина, оформление заказа;
- оплата: заполнение платёжных данных, проверка «Order Placed!»;
- API: получение списка товаров, `verifyLogin` (валидные и невалидные данные).

**saucedemo.com (UI):**
- вход под тестовым пользователем, добавление товара в корзину, checkout, проверка «Thank you for your order!».

## Структура

| Файл | Назначение |
|---|---|
| `conftest.py` | фикстуры: генерация тестовых данных (Faker), создание/удаление аккаунта через API, блокировка рекламных запросов через `context.route` |
| `login_page.py`, `payment_page.py` | Page Object'ы |
| `test_*.py` | тесты UI и API |

## Запуск

```bash
pip install -r requirements.txt
pytest -v
```

## Стек

Python 3 · Pytest · Playwright · Requests · Faker
