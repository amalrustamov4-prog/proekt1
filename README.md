# 🚀 BizCore UZ — Multi-Tenant Backend & Automation Engine

> **Готовый Backend, REST API, CRM и Telegram-автоматизация для малого и среднего бизнеса в Узбекистане.**

---

## 💡 О проекте

**BizCore UZ** позволяет любому магазину, ресторану, барбершопу или сервисной компании в Узбекистане за **10 минут** получить:
- 🏢 **Multi-Tenant изоляцию**: Каждый бизнес имеет собственные изолированные данные (товары, клиенты, заказы, ключи API).
- 🛍 **Управление каталогом и остатками**: Цены в UZS (сум), скидки, единицы измерения (`pcs`, `kg`, `portion`, `service`).
- 👥 **Клиенты и CRM (Nasiya)**: Учёт долгов клиентов, истории заказов и бонусных баллов.
- 📦 **Жизненный цикл заказов**: `Новый` ➔ `Подтверждён` ➔ `Собирается` ➔ `Передан курьеру` ➔ `Доставлен`.
- 🔔 **Мгновенные Telegram-уведомления**: Оповещения владельцам/менеджерам о новых заказах и покупателям об изменении статуса.
- 🔑 **Публичный REST API (`X-API-Key`)**: Для мгновенного подключения интернет-магазина, Telegram Web App, мобильного приложения (iOS / Android) или CRM.
- 📊 **Интерактивный Dashboard**: Аналитика выручки в UZS, график продаж за 7 дней, топ-товары, управление статусами.

---

## 💰 Монетизация и тарифы (Uzbekistan SaaS)

| Тариф | Цена | Для кого | Что включено |
| :--- | :--- | :--- | :--- |
| **Start** | **79 000 сум/мес** | Маленький магазин / салон | До 100 товаров, 1 API Key, Telegram-уведомления |
| **Business** | **199 000 сум/мес** | Растущий магазин / ресторан | До 1 000 товаров, 5 API Keys, CRM долгов (Nasiya), приоритетная поддержка |
| **Pro** | **399 000 сум/мес** | Крупный ритейл / сеть | Безлимитные товары, мульти-роли (кассир, курьер, менеджер), вебхуки |
| **Custom / White-Label** | **от 1 000 000 сум** | Индивидуальные системы | Развертывание на сервере клиента, кастомные интеграции |

---

## ⚡ Быстрый старт (Local Development)

### 1. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 2. Запуск Windows Desktop Приложения (POS / Касса)
Двойной клик по файлу **`launch_bizcore.bat`** или команда:
```bash
python desktop_app.py
```
*Запустит локальный бэкенд и откроет нативное окно Windows на движке WebView2 с поддержкой звуков сканера и печати чеков.*

### 3. Запуск веб-сервера отдельно
```bash
uvicorn app.main:app --reload --port 8000
```

### 3. Ссылки:
- 🌐 **Web Dashboard & Onboarding**: [http://localhost:8000](http://localhost:8000)
- 📖 **Интерактивная Swagger API документация**: [http://localhost:8000/docs](http://localhost:8000/docs)
- 📘 **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔑 Пример работы с Public API (`X-API-Key`)

Любой внешний сайт или Telegram-бот отправляет запросы с заголовком `X-API-Key: biz_live_...`:

### 1. Получить каталог товаров:
```bash
curl -X GET "http://localhost:8000/api/v1/public/catalog" \
     -H "X-API-Key: biz_live_apex_electronics_secret_key_demo"
```

### 2. Оформить заказ:
```bash
curl -X POST "http://localhost:8000/api/v1/public/orders" \
     -H "Content-Type: application/json" \
     -H "X-API-Key: biz_live_apex_electronics_secret_key_demo" \
     -d '{
       "customer_name": "Aziz",
       "customer_phone": "+998 90 123-45-67",
       "telegram_id": "4829104",
       "items": [{"product_id": 1, "quantity": 1}],
       "payment_method": "cash",
       "delivery_address": "г. Ташкент, Чиланзар 9"
     }'
```

---

## 🧪 Запуск тестов

```bash
python -m pytest -v
```
