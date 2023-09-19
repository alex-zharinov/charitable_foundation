# Проект QRKot

## Фонд пожертвований

> Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

## Технологии проекта

- Python — высокоуровневый язык программирования.
- FastAPI - фреймворк для создания веб-приложений на языке программирования Python
- Google Sheets API - создание отчёта в Google таблицах

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

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

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать .env. Пример:

```
APP_TITLE=Кошачий благотворительный фонд (0.1.0)
APP_DESCRIPTION=Сервис для поддержки котиков!
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
```

Создать БД и применить миграции:

```
alembic upgrade head 
```


Запустить проект:

```
uvicorn app.main:app
```

Проект будет доступен по ссылке http://127.0.0.1:8000/

Доступ к документации http://127.0.0.1:8000/docs/

Более подробно ознакомиться с докуметацией - openapi.yml

## Автор
[Жаринов Алексей](https://github.com/alex-zharinov)