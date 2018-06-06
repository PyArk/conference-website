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

The server will be running at [http://localhost:8000](http://localhost:8000).


## Todos:
- [X] Markdown is not being processed in "boxes" (see "Edit this content" links when logged in with an admin account)
- [ ] Missing template for `/speaker/create/`
- [ ] Missing template for `/sponsors/apply/`
- [ ] Misc layout bugs (e.g. inline edit buttons floating next to content, icons not lined up with titles on `/dashboard/`, etc)
