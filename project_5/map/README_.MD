### Django  Assignment



Consider you have to Develop a Software for Managing products and order list . The product  is divided into multiple categories like in amazon shopping list . you need  to manage the following features for each category, So that ur models will be mapped to each other and will be called via REST API .Heres the info of the models of the app<br />

````
TEMPLATE 1
````
Product<br />
1. Name (name) -> String<br />
2. id (int) -> int<br />
3. Price (int) -> string<br />
4. prod_desc  (description of the product) -> string<br />
5. prod_avail (Boolean) -> 2 choices (T, F)<br />

````
TEMPLATE 2
````
ORDER <br />
1. order id (order no) -> int<br />
2. product id (product id) -> int<br />
3. user id (username) -> int<br />
4. order_items(total orders ordered by user) -> str<br />
5. order_total  (product price * order_items(total orders ordered by user)) -> str<br />


````
TEMPLATE 3
````
User<br />
1. name (str) -> String<br />
2. id (int) -> int<br />
3. email -> String<br />

# Can be taken default from django auth models


**WHen order app is called , it needs to be posted first , only then we will be able to view all the orders list of each product from user **

TEMPLATE 1
### Assignment:

1. Create 2 Django apps named product and orders <br />
2. Create 2 models in respective app -> product and orders with features mentioned above<br />
3. Do not change Database changes in settings.py<br />
4. Run makeMigrations command<br />
5. Finally, run migrate command to create tables in the database<br />
6. Create views to Get and POST Data for product and orders models  ; Use ORM<br />
7. or Create a superuser ( python manage.py createsuperuser ) to add info
8. For Views and Urls More Details are given below <br />


#### Some Guide for urls.py:<br />

1. Name in Django URL -> name is used for accessing that URL from your Django / Python code.<br />
2. For example you have this in product/urls.py<br />
url(r'^main/', views.main, name='main')
3. In point 2, "main" is the name of this URL
4. URL namespaces -> URL namespaces allow you to uniquely reverse named URL patterns even if different applications use the same URL names. Remember, Both Name and Namespace are important for the assignment
5. For this assignment's test cases we have used some predefined names and namespace
6. Those names are defined below in the problem statement describes as "Django Url name"
7. Please make sure you use those names in Django URLs or else your assignment's test will fail



#### Views: Expected I/O


**Part 1: GET, POST, PUT and DELETE request for fetching Products**

**Django URL name: orders**<br />
No parameter<br />

TEMPLATE 2
**Actions**:<br />
1. GET - get list of all or one product<br />
2. POST - Add a new product to the db<br />
3. PUT - Update the product i.e **Update availiablity to current scenerio**<br />
4. DELETE - Remove product from the db<br />
<br />

      1. GET:
         Part 1:
            
            Response Data format {"data": [list of all products with model info]}
            If no data is present:
            /products/50/
            Response -> ({'data':'Product.DoesNotExist'})


            /products/5
             Response ->{"data": [each  specific info regarding the product ]}

      2. POST
      Response Data format {"created": {"name": "new product"}}
          return Response({'data':'Product created successfully '})
      else if product already exists:
          return Response({'data':'Product already listed  '})
         
      3. PUT
      Response Data format {"Feeded": name}
      /products/pk
      return Response -> ({"data": "put request updated"})
      
      4. DELETE 
      Response Data format {"Deleted ": pk}
       /products/pk
      return Response -> ({"data": "deleted product"})
      
 
TEMPLATE 3
**Part 2: GET, POST, Delete request for fetching orders<br />**

**Django URL name: orders**<br />
No parameter<br />

**Actions**:<br />
1. GET - get list of all or one order<br />
2. POST - Add a new order to the order<br />
4. DELETE - Remove order from the order<br />
<br /><br />
**Each and every detail regarding user, product, order needs to be displayed - Refer to the model**
<br />
 
     1. GET:
     get user id , product id 
     Response Data format {"data": [list of all orders placed ]}
     If no data is present
     /orders
     Response ->  return Response({"message":"Order id not found"})
     check detials of users , product and order if valid or not 
     MULTIPLE CHECKS AND VALIDATIONS NEEDS TO BE THERE ON EACH PRODUCT,USER,ORDER
          
     2. POST
     Response Data format {"created": {"name": 'order placed'}}
     if not product_id :
          return Response({"message":"Product id  not found"})
     else:
          return Response({"message": "Order Successful"})
     Response -> {"created": {"name": "order"}}
     
     
     4. DELETE 
     Response Data format {"Deleted ": name}
     /products/
     return Response({"message": "Order Successful Deleted"})
     else order id not found

## THUS MAP both the models and WE use DRF so make sure You use the same. 
 
## Installation Steps
1. Open up your Terminal / Command Line
2. git clone the repository
3. cd into the directory of the step (the one you just git cloned)
4. make sure you have python3 installed
5. Install virtualenv by following the steps 
```
Mac
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate

Windows
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
```
6. Run 
```
python -m pip install -r requirements/requirements.txt
```
6. No Database setup needs to be done. Do not edit Database settings in settings.py

7. If everything runs fine till here, create the application using the command
```
python manage.py startapp 
```

8. Run 
```
python manage.py makemigrations
```
9. Now Run the Server using command
```
python manage.py runserver
```
10.  Great! Start Coding the assignment for above usecase
11. After Finishing the assignment, you can test them locally using command 
```
coverage run --source='.' manage.py test --no-input
```
12. Push the code into the repo using git, 
13. Check if all the tests are Passed
