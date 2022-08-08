# flowers

### Installation

* create db flowers
* put env vars DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DJANGO_SETTINGS_MODULE  values in virtual environment (i`m using direnv and .env file for this task)
* Run this:
```
git clone https://github.com/HappyCthulhu/flowers
cd flowers
pipenv shell
pipenv install
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
