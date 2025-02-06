#! /bin/sh

# Setup Database
python manage.py migrate
# Setup admin and users
python manage.py shell < .devcontainer/create_users.py
# Load data
python manage.py loaddata restaurants reviews
