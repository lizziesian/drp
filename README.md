The web app is currently deployed at https://exercisingapp.herokuapp.com/.

To run locally on virtual enviroment (linux):
* python3 -m venv venv
* source venv/bin/activate
* pip install --upgrade pip && pip install -r requirements.txt
* python wsgi.py
* flask create_all
* flask populate
* flask run

To run locally on virtual enviroment (windows):
* pip install virtualenv
* virtualenv venv
* Set-ExecutionPolicy Unrestricted -Scope Process
* . .\venv\Scripts\activate
* python wsgi.py
* flask create_all
* flask populate
* flask run
