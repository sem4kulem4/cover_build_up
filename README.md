# cover_build_up

## Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:sem4kulem4/cover_build_up.git
```


Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

При необходимости создать базу данных postgres:
```
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

sudo -u postgres psql

CREATE DATABASE cbu;
CREATE USER cbu_user WITH PASSWORD 'password';
ALTER ROLE cbu_user SET client_encoding TO 'utf8';
ALTER ROLE cbu_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE cbu_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE cbu TO cbu_user;
\q
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```


Создать пользвателя:
```
http://127.0.0.1:8000/auth/users/
```

Создать JWT-токен:
```
http://127.0.0.1:8000/auth/jwt/create
```

GET и POST запросы выполняются на эндпоинт:
```
http://127.0.0.1:8000/api/v1/curves/
```




### Дополнительно

Получить/обновить текущего пользователя
```
http://127.0.0.1:8000/auth/users/me/
```
Обновить токен
```
http://127.0.0.1:8000/auth/jwt/refresh/
```