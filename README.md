# Django datatables htmx

Layout based on https://www.cssscript.com/minimal-data-table/

## This project was done with:

* [Python 3.9.6](https://www.python.org/)
* [Django 4.0](https://www.djangoproject.com/)

## How to run project?

* Clone this repository.
* Create virtualenv with Python 3.
* Active the virtualenv.
* Install dependences.
* Run the migrations.

```
git clone https://github.com/rg3915/django-datatables-htmx.git
cd django-datatables-htmx
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

## Django Seed

if running [django-seed](https://github.com/Brobin/django-seed) type:

```
python manage.py seed expense --number=145
```


# Django datatables htmx

Layout baseado em https://www.cssscript.com/minimal-data-table/

## Este projeto foi feito com:

* [Python 3.9.6](https://www.python.org/)
* [Django 4.0](https://www.djangoproject.com/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/django-datatables-htmx.git
cd django-datatables-htmx
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```


## Django Seed

Se quiser rodar o [django-seed](https://github.com/Brobin/django-seed) digite:

```
python manage.py seed expense --number=145
```

