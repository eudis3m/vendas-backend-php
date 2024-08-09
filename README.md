python -m venv env
source env/bin/activate  # Linux/MacOS
env\Scripts\activate  # Windows
pip install django djangorestframework
django-admin startproject myproject
cd myproject
python manage.py startapp products
pip install django-cors-headers
python manage.py runserver
