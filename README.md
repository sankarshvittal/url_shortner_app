# URL SHORTNER APPLICATION

A dashboard for visualizing personal management information

## STEPS FOR DEPLOYING (for development):

```
1. Clone the latest project (master branch) from Github into your local machine
2. Create a virtual environment for the project in your local machine.
3. Install the required packages in your virtual environment from requirements.txt file using the following command in terminal : pip install -r requirements.txt
4. Run the following commands to create migrations:
   a. python manage.py migrate
   b. python manage.py makemigrations
5. Create super user:
   a. Run the command : python manage.py createsuperuser
   b. You will be prompted to enter the user name , email and passwoed. Follow the instructions as described below:
      - username : admin
      - email : ( leave it blank )
      - password : Enter your password of choice
6. Run the following cmd in your terminal to run the django application: python manage.py runserver
7. Open the link  http://127.0.0.1:8000/  on your browser of choice and login using your credentials.
8. Done, the application has been successfully deployed.
```


### PYTHON VERSION :
```
python 3.7.2
```
