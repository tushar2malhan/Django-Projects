# Django-Blog-Application

TEMPLATE 1
Consider you have to Develop a Software for a basic blog application in Django in case you would like to use as a base and build any of your requirements on it.

Just to make sure that you have something to view inside of the application, I also included db.sqlite3, which includes a few posts and categories.

### REMEMBER DO CREATE A SUPERUSE TO LOGIN

Create a new virtual environment in desired path and activate:


Navigate to the project directory you cloned from github and install the requirements just to make sure that you have all required packages installed:

```
pip install -r requirements.txt
```

Now you need to make migration and migrate, so please go to directory of project and use the commands below:

```
python manage.py makemigrations
python manage.py migrate
```

Within the database, as I mentioned, you will have sample posts and categories, which you can edit from the admin page. I also included the admin page within the main page.

You can initially use these credentials:

```
Username : tushar
Password : 123456
```

or you can simply create a superuser for yourself using the following command:

```
python manage.py createsuperuser
```

After completing all these steps, you can now run your application:

```
python manage.py runserver
```

The logic of the application is really simple:

1. You have the main view, where you can see all of the posts that have assigned status visible. In case you will allow users to write a post in your blog application, the post will not be visible initially until you change the visible status to True. For this moment, this can be done only through the Admin page. I included visible status for posts just to make sure that the content I received from a user can be published on my web page.  

```
TEMPLATE 2
````
. There is a filter created in the main view, which includes only the categories listed on the page at the moment. Even though you might have more categories in your Category table, they won't be visible unless they are used in viewed posts.

. There is a separate view created and the user can view all of their posts even when they are not approved yet. The status of the post (published or not published) is visible on this page within the corner of the list element.

. There is also a view, in which the user can edit the post that was created before. The edit option is only available to the owner of the post and all users, who have superuser status in the application.

```
TEMPLATE 3
```
. An additional view was created just for approving the posts that were written by page users. This view changes status to visible and lock the post for editing for all users except for superuser.

. Within the project, I included also TinyMCE, which makes it easier to edit the content. However, the link is created for me so please register to TinyMCE and get your own link. Otherwise, you will always receive a notification that your domain is not registered, however, you can still ignore this notification and use the editor.

I have a separate application created to handle notifications. Both user and superuser receive a message from the system once a post or a comment is submitted. Then superuser can approve or delete if necessary.

Kindy refer to the screenshots for the same 
https://github.com/tushar2malhan/shared/tree/master/project_6/screenshots
