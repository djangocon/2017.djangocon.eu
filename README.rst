#####################
DjangoCon Europe 2017
#####################

This is the project for the http://2017.djangocon.eu/ website.

Run locally
-----------

* clone the project
* ``cd djangocon-europe``
* edit ``djangocon_europe/.env`` key according to your environment. See an example below
* setup virtualenv::

    virtualenv --python=/usr/bin/python3.5 env
    . env/bin/activate
    pip install pip-tools
    pip-sync

* ``python manage.py migrate``
* ``python manage.py runserver``

Example .env file
-----------------

Configuration uses `django-dotenv`_. Please refer to its document for the configuration details.

Example::

    DATABASE_URL=psql://postgres:@:5432/djangocon_europe
    DEBUG=True
    ALLOWED_HOSTS=["*"]
    SECRET_KEY=my-secret-key
    CACHE_URL=rediscache://127.0.0.1:6379:1
    EMAIL_HOST=localhost


Compile sass files
------------------

We use compass to compiles scss files to css::

    compass compile



.. _django-dotenv: https://github.com/jpadilla/django-dotenv

License
-------

All the code except file in ``styles`` and ``djangocon_europe/static/img`` directories are released with BSD-3 clauses

Files in ``styles`` and ``djangocon_europe/static/img`` are not reusable without prior consent.
