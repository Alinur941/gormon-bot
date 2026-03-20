# GOrMon Bot 🏃‍♂️

Telegram-бот для бегового сообщества GOrMon (nomadsport.net).

## Что умеет

- 📝 Пошаговая инструкция по регистрации на забег
- ❓ FAQ — ответы на частые вопросы
- 📅 Список ближайших событий
- 📞 Контакты организаторов

## Запуск

```bash
# Установить зависимости
pip install -r requirements.txt

# Создать .env файл
cp .env.example .env
# Вставить токен бота в .env

# Запустить
python bot.py
```

## Структура

```
gormon-bot/
├── bot.py           # Основной файл бота
├── keyboards.py     # Inline-клавиатуры
├── data/
│   └── faq.py      # База FAQ
├── requirements.txt
└── .env.example
```

## Добавление FAQ

Открой `data/faq.py` и добавь новый объект в список `FAQ`:

```python
{
    "id": "unique_id",
    "question": "❓ Текст вопроса",
    "answer": "Текст ответа",
},
```
