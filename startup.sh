#!/bin/bash

python manage.py runserver
daphne -b 0.0.0.0 -p 8000 projetoPDI.asgi:application