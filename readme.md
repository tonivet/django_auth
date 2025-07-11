# Django Authentication Project

Simple web authentication system with django. Extends build in django authentication system with adding some additional data for the user like city, country, gender and profile picture in separate sql table. Frontend is basic, made with bootsrap 5.
User:
* can register
* login
* logout
* change password
* change profile data
* reset password with send email
* delete account

app_core is django main project folder, accounts app is where are upgrades to authentication system. 
Django settings.py file is moved to settings folder and separated to two files local.py for local development and production.py for deployment. Switching to production.py is done by system environment PIPELINE = production. Email backend is ready to work with gmail but you can switch to any other mail provider in the settings file. If you use decide to gmail first you have to create apps password smtp. For more information https://support.google.com/mail/answer/185833?hl=en
Project is ready for docker deployment. 

## Installation

For local deployment create virtual environment and install requirements.txt
```python
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

For docker deployment first make .env file and put there at least these variables: PIPELINE=production, SECRET_KEY, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, HOST_URL.
You can generate SECRET_KEY on https://djecrety.ir/

```bash
docker compose up -d
```


