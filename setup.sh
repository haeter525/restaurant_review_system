#! /bin/sh

# Setup Database
python manage.py migrate
# Setup admin
python manage.py createsuperuser --no-input --skip-checks
# Setup users
python manage.py shell < create_users.py
# Load data
python manage.py loaddata restaurants reviews
