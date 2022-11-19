 Django RealEstate Application 
==============================
    This is a simple real estate application built with Django.


Installation
------------
    1. Clone the repository
    2. Create a virtual environment
    3. Install the requirements
    4. Run the migrations
    5. Create a superuser
    6. Run the server
    $ git clone
 
 cd into project folder "backend"  > find manage.py file >  

```
python manage.py makemigrations && python manage.py migrate && python manage.py runserver
```
'''
  View all homes from default path "/" -->  http://127.0.0.1:8000/
  Search homes for Particular features -->  http://127.0.0.1:8000/search/<str:value>
  Sell homes from  path  "sell"  	   -->  http://127.0.0.1:8000/sell/
  Offers for PreSale		  	   -->  http://127.0.0.1:8000/offers/
  Offers for Sold Home		  	   -->  http://127.0.0.1:8000/sold_offers/
'''