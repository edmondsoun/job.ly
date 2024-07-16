=======================================
Pix.ly: Image Rendering and Editing App
=======================================

Pixly is an image rendering and editing app built in Flask using Pillow for
image manipulation and integrated with DigitalOcean Spaces (formerly AWS S3) to
host and serve images via the cloud.


View a deployed version [https://pix-ly.onrender.com/](here).


Setup
-----

Create/activate a virtual environment and install dependencies:

```zsh
~ python3 -m venv venv
~ source venv/bin/activate
~ pip install -r requirements.txt
```

Set up a local Postgres database via `psql`:
```zsh
~ createdb pixly
```

This application requires the following environment variables to upload images to the cloud:
```
DATABASE_URL=[your_db_uri]
DO_ACCESS_KEY_ID=[do_spaces_access_key]
DO_SECRET_ACCESS_KEY=[do_spaces_secret_access_key]
BUCKET=[do_bucket_name]
```