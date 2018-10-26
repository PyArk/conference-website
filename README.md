# README.md

A bare bones conference website.

Single HTML page with some dynamically loaded "Tiles" will make up most of the content in this site. 

## Officially Supporting Python 3.6.6 
pip install -r requirements.txt

This is the version Heroku uses, so for the short-term, other versions are not being tested, 
and their requirements files not updated.

TODO: Update Python 3.7 requirements and test
TODO: Determine if Python 2.7 is even worth keeping up with at this point.
  
## Initial Setup
There's a command hook that can be used to do the whole initial setup and start the server fresh.
```commandline
python manage.py install_main
```


## Known Issues
[_] - Issue reported from s3 dependencies 
```commandline
 /app/.heroku/python/lib/python3.6/site-packages/storages/backends/s3boto3.py:282: UserWarning: The default behavior 
 of S3Boto3Storage is insecure and will change in django-storages 2.0. By default files and new buckets are saved 
 with an ACL of 'public-read' (globally publicly readable). Version 2.0 will default to using the bucket's ACL. 
 To opt into the new behavior set AWS_DEFAULT_ACL = None, otherwise to silence this warning explicitly 
 set AWS_DEFAULT_ACL.
```

## Google App Engine Deployment
Create a SQL Cloud Instance and set the variables appropriately
GAE_SQL_PASS
GAE_SQL_USER
GAE_SQL_CON_STR
GAE_INSTANCE
Follow this guide https://cloud.google.com/python/django/flexible-environment
