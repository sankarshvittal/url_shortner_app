# URL SHORTNER APPLICATION

A web app to shorten URL

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
6. Run unit tests: python manage.py test
7. Run the following cmd in your terminal to run the django application: python manage.py runserver
8. Open the link  http://127.0.0.1:8000/  on your browser of choice and login using your credentials.
9. Done, the application has been successfully deployed.
```

## STEPS FOR DEPLOYING IN DOCKER (for production):

```
1. Clone the latest project (master branch) from Github into your machine
2. Install the latest version of docker on your machine
3. Run docker-compose build and docker-compose up from inside the project folder
4. Done, you can acccess the application through the link: http://host_name:8000/. Login using your credntials.
```

### PYTHON VERSION :
```
python 3.8.8
```
