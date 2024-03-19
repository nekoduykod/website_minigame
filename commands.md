venv\Scripts\activate
pip install -r requirements.txt

# very beginning - creates necessary files
django-admin startproject name_name

# opens localhost server
py manage.py runserver


# creation of a new app folder
py manage.py startapp your_app


# when new app created (e.g. /members..)
py manage.py migrate


# creates a model (check migrations/)
py manage.py makemigrations members
# creates a table
py manage.py migrate
# to check the sql query
py manage.py sqlmigrate members 0001
# to add records, open python shell
py manage.py shell
# import the model (data; it is an object, which is a db table)
from members.models import Member
Member.objects.all()
member = Member(firstname='Andrii', lastname='Zebra')
member.save()
x = Member.objects.all()[4]
x.firstname
x.firstname = "Sasha"
x.save()
# values() method returns object as Python dictionary
Member.objects.all().values() 
x.delete()
# values_list() helps to return specific columns
mydata = Member.objects.values_list('firstname')
filter() method. Member.objects.filter(firstname='Emil').values()
Member.objects.filter(firstname__startswith='L').values(); WHERE firstname LIKE 'L%'
mydata = Member.objects.all().order_by('firstname').values() . descending = ('-firstname') 
# create superuser for django.admin
py manage.py createsuperuser (sasha, password456, fake@gmail.com)
# or change via UI of admin

# when added new styles css
py manage.py collectstatic

# when db in settings.py, use this, but no data will be
py manage.py migrate
