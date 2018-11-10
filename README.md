# README.md

A bare bones conference website.

Single HTML page with some dynamically loaded "Tiles" will make up most of the content in this site. 

## Officially Supporting Python 3.6.6 
pip install -r requirements.txt

  
## Initial Setup
There's a command hook that can be used to do the whole initial setup and start the server fresh.
Make sure you have your environment varriables set, if any are needed. 
```commandline
python manage.py install_main
```

## Environment Varriables required
#### For Amazon S3 Storage via Boto
* S3_BUCKET_NAME
* S3_SECRET_KEY
* S3_ACCESS_ID
#### For Heroku Postgres Database
* DATABASE_URL
* HEROKU_HOSTNAME