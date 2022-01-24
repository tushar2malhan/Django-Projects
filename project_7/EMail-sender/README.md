# TEMPLATE 1
# Django-Email-Sender
Send email from Gmail Id in Django using HTML Template

# Pre-Requisites
- Python
- Pip
- Git

# Steps to run:
- Make changes in settings.py file where your Gmail Id configurations are set.
- In PipFile, the dependencies are mentioned. It is recommended to run the app inside a virtual environment to avoid conflict of existing dependencies.
  - Run the command "pip install pipenv"
  - Run "pipenv shell". Creates virtual env
  - Run "pipenv install". Installs dependencies from the PipFile and creates PipFile.lock
  - Run "python manage.py runserver" to start the server


# TEMPLATE 2
# Additional changes to be done in Host Gmail account
- Go to https://myaccount.google.com/security
- Scroll till you find "Less secure app access"
- Here you will find that the status is Off. You need to turn this to On State. 
Only if you follow the above steps, then you can send mail from your Gmail account using your django code. 



# TEMPLATE 3 
Here Your html page would be fired up as the mail is sent to receipients.
Try to showcase the message more precisely.

Look at the screenshots for more information.
