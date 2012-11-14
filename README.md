CachiruloCalendar
=================

A calendar to display events and activities organized by diverse technology groups or communities in Aragón in a centralized way. One calendar to rule them all.

Setup
-----

    git clone
    cd cachirulocalendar/cachirulocalendar
    #assumes a mysql server in localhost with root account with no password, see settings.py
    mysqladmin -u root create cachirulocalendar
    #when prompted on syncdb, create a superuser for the app (e.g. admin/admin)
    python manage.py syncdb
    python manage.py runserver

Admin
-----

Go to http://127.0.0.1:8000/admin/, login as the superuser, edit DB data.

