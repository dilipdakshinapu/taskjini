# taskjini

Prerequisites
Python 3
Flask
Virtualenvironment

Install the virtualenvironment

$ pip install virtualenv
$ virtualenv venv # Initialize the virtualenvironment

Install the dependencies. Go to the project root directory and execute below command
$ pip install -r requirements.txt

Add .env file to the root directory and add the below content

source ../venv/bin/activate
export DATABASE_URI = sqlite:////data.db
export APP_SETTINGS = development
export SECRET = aslkjlajs9w390820raijslkjalsjf

Run migrations to create the schema

$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade

Run the application

python run.py

Test the application

python test_tasklist.py


Endpoints
------------
GET: /tasks - Retrieve all the tasks 
GET: /tasks/<priority> - Filter the tasks based on priority
POST: /tasks - Create a task

GET: /task/<id> - Retrieve the task based on primary key
PUT: /task/<id> - Edit the status of the task
DELETE: /task/<id> - Delete the task