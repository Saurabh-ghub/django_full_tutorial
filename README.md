# django_full_tutorial

###Django is a high-level Python-based free and open-source web framework, which follows the model-view-template (MVT) architectural pattern.It is maintained by the Django Software Foundation (DSF).
Django's primary goal is to ease the creation of complex, database-driven websites. Some well-known sites that use Django include the Public Broadcasting Service, Instagram, Mozilla, The Washington Times, Disqus, Bitbucket, and Nextdoor.

# HTTP PROTOCOLS

### GET : If we want tofetch data then we use get method .BY default if we dont mention the methid in form then it will be a get request.
### POST: If we want to submit data then we use POST method. It will not show the data we entered in form on url.
### UPDATE: If we want to update the data
### DELETE: to delete the data

# MVT ==> Model View Template

## Heirarachy
 ### USER
 ### DJANGO
### URLs
 ### VIEW
### MODEL  AND TEMPLATE

# ORM (Object Relation mapper)
 The ORM’s main goal is to transmit data between a relational database and application model. The ORM automates this transmission, such that the developer need not write any SQL.
ORM, as from the name, maps objects attributes to respective table fields. It can also retrieve data in that manner.

## making migration: (need psycopg2 for connecting python to postgres )
1. in setting.py, add app config     2. change the database ,user ,password    3.In model.py do the required changes in class   4. $python manage.py makemigrations 5.$python mange.py sqlmigrate travello 0001   6. $python mange.py migrate