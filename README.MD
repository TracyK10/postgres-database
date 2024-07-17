# User API

This project is a simple Flask API for managing users, which can be deployed on Render. It uses SQLAlchemy for ORM, Flask-Migrate for handling database migrations, and Flask-RESTful for creating RESTful APIs.

## Features

- Create, read, update, and delete users.
- JSON serialization of user objects.

## Setup

### Prerequisites

- Python 3.10
- PostgreSQL
- Git
- Render account

### Clone the Repository

```sh
git clone https://github.com/TracyK10/postgres-database.git
cd user-api
```

### Install Dependencies

```sh
pip install -r requirements.txt
```

### Set Up Environment Variables

Set the environment variables in your terminal:

```sh
export DATABASE_URL=your_database_url_here
export FLASK_APP=app.py
```

### Initialize the Database

```sh
flask db init
flask db migrate
flask db upgrade
```

### Seed the Database

Your `seed.py` file should look like this:

```python
from app import db, User

def seed_data():
    user1 = User(username='user1', email='user1@example.com')
    user2 = User(username='user2', email='user2@example.com')
    
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed_data()
```

Run the seed file:

```sh
python seed.py
```

## Run the Application

```sh
flask run
```

The application will be available at `http://127.0.0.1:5000/`.

## Deploy to Render

1. **Create a New Web Service on Render:**
    - Go to your Render dashboard.
    - Click on "New" and select "Web Service".
    - Connect your GitHub repository and select the repo for this project.

2. **Configure the Web Service:**
    - **Build Command:** `pip install -r requirements.txt`
    - **Start Command:** `flask run --host=0.0.0.0`
    - **Environment:** Python 3.10

3. **Add Environment Variables:**
    - In the Render dashboard, go to the "Environment" tab of your web service.
    - Add the same environment variables you set in your terminal.

4. **Deploy:**
    - Click on "Deploy" to deploy your application.

Your API should now be live on Render.

## API Endpoints

- `GET /` - Welcome message.
- `GET /users` - Get a list of all users.

## Directory Structure

```
.
├── app.py
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── 74aea7e5bec4_create_table_birds.py
├── models.py
├── Pipfile
├── Pipfile.lock
├── requirements.txt
└── seed.py
```

## requirements.txt

```txt
-i https://pypi.org/simple
alembic==1.13.2; python_version >= '3.8'
aniso8601==9.0.1
blinker==1.8.2; python_version >= '3.8'
click==8.1.7; python_version >= '3.7'
flask==3.0.3; python_version >= '3.8'
flask-migrate==4.0.7; python_version >= '3.6'
flask-restful==0.3.10
flask-sqlalchemy==3.1.1; python_version >= '3.8'
greenlet==3.0.3; platform_machine == 'aarch64' or (platform_machine == 'ppc64le' or (platform_machine == 'x86_64' or (platform_machine == 'amd64' or (platform_machine == 'AMD64' or (platform_machine == 'win32' or platform_machine == 'WIN32')))))
gunicorn==22.0.0; python_version >= '3.7'
itsdangerous==2.2.0; python_version >= '3.8'
jinja2==3.1.4; python_version >= '3.7'
mako==1.3.5; python_version >= '3.8'
markupsafe==2.1.5; python_version >= '3.7'
packaging==24.1; python_version >= '3.8'
psycopg2-binary==2.9.9; python_version >= '3.7'
pytz==2024.1
setuptools==70.3.0; python_version >= '3.8'
six==1.16.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2'
sqlalchemy==2.0.29; python_version >= '3.7'
sqlalchemy-serializer==1.4.22; python_version >= '3.10' and python_version < '4.0'
typing-extensions==4.12.2; python_version >= '3.8'
werkzeug==3.0.3; python_version >= '3.8'
```

This should help you set up and deploy your Flask API to Render. If you have any questions or run into issues, feel free to ask!