
# Django - Docker - Postgres Microservice

## Dependencies
#### Python, Django, Docker, PostgreSQL, Nginx


* This web application creates CRUD application hosted on DOCKER with postgreSQL as DATABASE in an App where users can 
    * add Tasks 
    * delete,update,modify Tasks
    * Tools used here are HTML, CSS, Django, Docker, PostgreSQL
    * Python , DJango, and Bootstrap  to create the Application.
    * [optinal] Here user can filter out the Tasks based on the category

* DO CHANGE IN THE SETTINGS.PY FILE TO CONNECT TO THE DATABASE - for Docker Compose
    - project\settings.py
    - uncomment the line  'HOST': 'db',          # for docker container
    - comment the line    'HOST': 'localhost',    # for local machine

* PROJECT/settings.py  | Database Configuration |
```
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'password for postgres',
        'HOST': 'db',               # For docker container
        # 'HOST': '127.0.0.1',      # For postgres connectivity
        'PORT': '5432',
    }
}
                   # For local host
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
 }
```

# Template 1
# SETUP 
    * Dockerfile            ->    Instructions layed out
    * docker-compose.yaml   ->    For PostgreSQL service compatible with our Dockerfile


# Template 2
* A COMPLETE App WITH DJANGO FRAMEWORK
    * Able to show all the Tasks 
    * Displaying the Updated Tasks  with striked out text 
    * These main features have  been currently implemented
    Try to Replicate them along with their functionalities:
    Features:
        []:  View The tasks
        []:  Add the Tasks
        []:  Submit results and view the Results pages
        []:  Modify Tasks




* Template 3
- You need to create a superuser to add the Main User to the database | Create a superuser
    
    * []:  python manage.py createsuperuser
    * []:  http://127.0.0.1:8000/admin - Sign in with the username and password you created
    * []:  Click on login to check the Models and User created.
    * []:  Click on the User and check the User created.

# MAKE SURE YOU HAVE DJANGO AND DOCKER INSTALLED
 * If on Windows, Make sure your docker desktop is running.
 * If on Mac, Make sure you have docker-machine installed.
 * If on Linux, Make sure you have docker-compose installed.


# INSTRUCTIONS 
```
    []:  cd djang-doc                         ->  ( Dockerfile and docker-compose.yaml are in the same path )
    []:  docker compose up                   ->   Boot up the Containers 
    []:  docker compose ps                   ->   Check the running the containers 
    []:  docker compose restart              ->   Restart the Exited containers 
    []:  Ctrl + C                            ->   stop and exit from containers
    []:  docker-compose down                 ->   Remove the containers
    []:  docker-compose rm -f                ->   Remove the containers
    []:  docker compose -p djang-doc up      ->  Specify a name of your containers | If name given Specify each command with name |  docker compose -p djang-doc up, restart ...
    []:  Remove everything from scratch      ->  docker system prune -a -f && docker system df && docker builder prune -f && docker volume prune -f
```

*  Create and start the Container 
`docker run -it <image_name> bash`

* SSH into the Running container - Docker Db > to execute the SQL queries 
- docker exec -it container_name /bin/bash
` docker exec -it djang-doc-db-1 bash `    
` psql -U postgres `             > Start the Postgres service on Docker
` \l `                           > List all the databases
` \c postgres `                  > Connect to the database
` \dt `                          > List all the tables
`select * from tasks_task; `     > Execute the command 
` \q `                           > Exit from the container
</br>
</br>
</br>

*   Access Docker Postgres Container to view the results 
` docker run -d -p 5432:5432 --name <db_container_name> -e POSTGRES_PASSWORD=mysecretpassword -U postgres  <db_image_name> `

* Access The Non Existent Container from the image  in bash terminal 
`docker run --rm -it --entrypoint bash <image_name>`


* Open `http://127.0.0.1:8000` to see the main site.

# Issues:

*  Suppose db is connected but table throwing error where it does not exist in db in django ! 
*  Something like this ->  relation "django_site" does not exist

#   Execute these commands inside the Docker WEB Container 
` docker exec -it django-doc-web-1 bash `
```
  python manage.py migrate --run-syncdb
  python manage.py makemigrations tasks [ python manage.py makemigrations appname ]
  python manage.py migrate --fake tasks appname
```

# Thus You need to login as either Root user or login via Oauth

#   Execute these commands inside the Docker WEB Container 
` docker exec -it django-doc-web-1 bash `
```
    python manage.py createsuperuser
```
</br>



* [ Hint :] If Facing issue Check your project url and app url and make sure they are correct.
* [If Issue Persists ->  try running `localhost:8000` or `http://127.0.0.1:8000` in New Incognito Tab ]



- Creating to manage three instances of this application ( docker-compose ) for web container inorder to support load balancing and high availability of the application

# Features of Nginx
- Use as Web Server
- Use as Reverse Proxy
- Load Balancing
- Caching


# If accessing Nginx  ~

- Nginx configuration file is in the path ./nginx/nginx.conf    
```
events{
    worker_connections  1000; # increase this if you have a lot of clients
}

http{

    server{
        listen 80;
        server_name localhost;
        
        location / {
            proxy_pass http://web:8000;  # (web) Django application running on port 8000
        }
    }   
}
```

```
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      # without nginx server -> run on port 8000 
      # - "8000:8000"     # because we dont need to load balance here

      # With nginx server -> we are running ngninx server to scale this django site 
      # we we expose only the (web) container port so that both instances can be accessed
      # as a load balancer of 2 sites for single application
      # as both containers are running on same port 8000 localhost
      # we can use command to run with nginx 
      #    docker compose up -d --build --scale web=2  
      - '8000'
    depends_on:
      - db
    
  nginx:
    build: ./nginx
    ports:
      - "80:80"     
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro    # MAP local nginx file with nginx container file
    depends_on:
      - web

```

- docker compose command to run the app with 3 instances
    ```
    docker compose -p django up  --build --scale web=3

    ```

    ```
    docker compose -p django  up -d --build --scale web=3

    ```
-p : Assign Project name 'django'
-d : run in background
--build : will automatically assign your local system ports to each container so that they dont conflict with each other
--scale : will scale the number of instances of the web container

- Our application will Now be accessible on port 80 of the host machine via Nginx Load Balancer
* Open `http://localhost/` to see the main site.

* Look at the Screenshot to![django_](https://user-images.githubusercontent.com/66706496/202846286-64d34ad1-8111-4ccd-b9bf-c992e46969e1.png)


