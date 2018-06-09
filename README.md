# Conference website
This is still a work in process.

## Setup
#### 1. Install `virtualenvwrapper`
Follow the instructions [here](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).

#### 2. Install everything else
```bash
# Create a new virtualenv
mkvirtualenv pyarkconf

# NOTE: this project requires python 2.7-ish. If your default is python 3, you'll need to do
# something like this, changing the path to wherever you python 2 is located:
mkvirtualenv ---python /usr/local/bin/python2 pyarkconf

# Install dependencies
pip install -r requirements.txt
```

#### 3. Run migrations
```bash
./manage.py migrate
```

#### 4. Run the server
```bash
./manage.py runserver
```

#### 5: Don't Forget
Create an admin user by running 
```bash
./manage.py createsuperuser
```
Then create a conference object. You can do that at http://localhost:8000/admin/ (search for conference). 

The server will be running at [http://localhost:8000](http://localhost:8000).


## Todos:
- [X] Markdown is not being processed in "boxes" (see "Edit this content" links when logged in with an admin account)
- [X] Missing template for `/speaker/create/`
- [X] Missing template for `/sponsors/apply/`
- [X] Misc layout bugs (e.g. inline edit buttons floating next to content, icons not lined up with titles on `/dashboard/`, etc)
- [ ] Create sponsorship terms page (search: `TODO_SPONSORSHIP_TERMS`)
- [ ] Speaker profile form is no-op
- [ ] Header covers content on smaller screens
