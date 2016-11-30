#####################
DjangoCon Europe 2017
#####################

This is the project for the http://2017.djangocon.eu/ website.

Run locally
-----------

* Make sure that you have Python 3.5 installed on your system.
* Set up your project::

    git clone https://github.com/djangocon/2017.djangocon.eu.git  # Clone the project
    cd 2017.djangocon.eu

* Edit ``djangocon_europe/.env`` key according to your environment. See an example below.
* Set up your virtualenv::

    virtualenv --python=/usr/bin/python3.5 env                    # Start a virtualenv
    . env/bin/activate                                            # Use the virtualenv
    pip install --upgrade pip                                     # Use a current pip version
    pip install pip-tools
    pip-sync                                                      # Install dependencies

* Set up the Django project::

    python manage.py migrate
    python manage.py runserver

Example .env file
-----------------

Configuration uses `django-environ`_. Please refer to its document for the configuration details.

Example::

    DATABASE_URL=psql://postgres:@:5432/djangocon_europe
    DEBUG=True
    ALLOWED_HOSTS=["*"]
    SECRET_KEY=my-secret-key
    CACHE_URL=rediscache://127.0.0.1:6379:1
    EMAIL_HOST=localhost
    EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

Expected pages
--------------

The template expects that the following pages exits:

* Home page (with reverse id "home")
* Code of Conduct page (reverse id "coc")
* Blog page (reverse id "blog")

Home and blog pages are created via djangocms-apphook-setup, but
you have to set the reverse id yourself.


Compile sass files
------------------

We use `compass`_ to compiles scss files to css::

    compass compile

After that collectstatic files::

    python manage.py collectstatic -l



.. _django-environ: https://github.com/joke2k/django-environ
.. _compass: http://compass-style.org/install/

License
-------

All the code except file in ``styles`` and ``djangocon_europe/static/img`` directories are released with BSD-3 clauses

Files in ``styles`` and ``djangocon_europe/static/img`` are not reusable without prior consent.
