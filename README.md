Install
=======

Install package by next command:
```pip install git+https://github.com/maxvyaznikov/kudago-test```

Example
-------

Code contains example django app to test mapper. See `kudago_mapper_example`.
To initialize this example, please, use next commands:
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py load_afisha
```
After that see url `http://127.0.0.1:8000/admin/` to view results.

More details:
 1. `python manage.py migrate` creates db.sqlite3 database file
 2. `python manage.py createsuperuser` adds new user into DB
 3. `python manage.py runserver` starts HTTP-server on 8000/tcp
 4. `python manage.py load_afisha` loads data from example file located by
 `kudago_mappet/tests/test_source.xml`. But in DB will be created only objects
  for events and some related (such as EventImage and Tag). Loading of all
  other objects is easy to add and obviously how to do it (see
  `afisha/management/commands/load_afisha.py:17`).
