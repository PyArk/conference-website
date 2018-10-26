import os

text = """runtime: python
env: flex
entrypoint: gunicorn -b :$PORT pyconark.wsgi

beta_settings:
  cloud_sql_instances: """ + os.getenv("GCP_SQL_CON_STR") + """ 

runtime_config:
  python_version: 3.6

env_variables:
  S3_ACCESS_ID: """ + os.getenv("S3_ACCESS_ID") + """
  S3_SECRET: """ + os.getenv("S3_SECRET") + """
  GCP_SQL_USER: """ + os.getenv("GCP_SQL_USER") + """
  GCP_SQL_PASS: """ + os.getenv("GCP_SQL_PASS") + """
  GCP_SQL_CON_STR: """ + os.getenv("GCP_SQL_CON_STR") + """
  
"""
# Should look at doing it like this - https://codeburst.io/beginners-guide-to-deploying-a-django-postgresql-project-on-google-cloud-s-flexible-app-engine-e3357b601b91
# Save app.yaml in google drive, not in git.
#   STATIC_URL: 'https://storage.googleapis.com/pyconark-dev/static/'

with open('app.yaml', 'w') as file:
    file.write(text)
    file.close()
