# Проект благотворительного фонда

[![charitable-foundation workflow](https://github.com/alex-zharinov/charitable_foundation/actions/workflows/main.yml/badge.svg)](https://github.com/alex-zharinov/charitable_foundation/actions/workflows/main.yml)

## Фонд пожертвований

> Фонд собирает пожертвования на различные целевые проекты.

## Технологии проекта

- Python — высокоуровневый язык программирования;
- FastAPI — фреймворк для создания веб-приложений на языке программирования Python;
- Google Sheets API — создание отчёта в Google таблицах;
- uvicorn — это реализация веб-сервера ASGI для Python;
- Alembic — это инструмент для миграции базы данных, используемый в SQLAlchemy;
- pydantic — библиотека, упрощающая процесс проверки данных.

### Как запустить проект:
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/alex-zharinov/charitable_foundation.git
```
```
cd charitable_foundation
```
- Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
* Если у вас Linux/macOS
    ```
    source venv/bin/activate
    ```
* Если у вас windows
    ```
    source venv/scripts/activate
    ```
- Создать .env. Пример:
```
#  ./.env

APP_TITLE=Благотворительный фонд
APP_DESCRIPTION=Сервис для сбора пожертвований!
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
TYPE=<type>
PROJECT_ID=<project_id>
PRIVATE_KEY_ID=<private_key_id>
PRIVATE_KEY=<private_key>
CLIENT_EMAIL=<client_email>
CLIENT_ID=<client_id>
AUTH_URI=<auth_uri>
TOKEN_URI=<token_uri>
AUTH_PROVIDER_X509_CERT_URL=<auth_provider_x509_cert_url>
CLIENT_X509_CERT_URL=<client_x509_cert_url>
EMAIL=<your_email>
```
- Применить миграции:
```
alembic upgrade head
```
- Запустить проект:
```
uvicorn app.main:app
```

### Ваш проект будет доступен по ссылке:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Проекты
В Фонде может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.

### Пожертвования
Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

### Пользователи
Целевые проекты создаются администраторами сайта.

Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых.

Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.

### Формирования отчёта в гугл-таблице
В отчёте содержатся закрытые проекты, отсортированные по скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму.

### Документация
Доступ к документации http://127.0.0.1:8000/docs/

Примеры запросов к API, варианты ответов и ошибок приведены в спецификации `openapi.yml`; спецификация есть в репозитории.
Для удобной работы с документом воспользуйтесь онлайн-редактором Swagger Editor, в котором можно визуализировать спецификацию.

### Примеры запросов:
- Получить список всех проектов:
```
curl -X 'GET' \
  'http://127.0.0.1:8000/charity_project/' \
  -H 'accept: application/json'
```
Response body:
```
[
  {
    "name": "project_name",
    "description": "description",
    "full_amount": 250,
    "id": 1,
    "invested_amount": 0,
    "fully_invested": true,
    "create_date": "2023-09-04T15:24:54.025922",
    "close_date": "2023-09-04T15:24:54.090480"
  }
]
```
- Сделать пожертвование:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/donation/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{
  "comment": "string",
  "full_amount": 500
}'
```
Respose body:
```
{
  "comment": "string",
  "full_amount": 500,
  "id": 13,
  "create_date": "2023-09-23T11:49:26.209023"
}
```
- Получить информацию о своём профиле:
```
curl -X 'GET' \
  'http://127.0.0.1:8000/users/me' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <token>'
```
Response body:
```
{
  "id": 2,
  "email": "admin@example.com",
  "is_active": true,
  "is_superuser": true,
  "is_verified": false
}
```


## Автор
[Жаринов Алексей](https://github.com/alex-zharinov)
