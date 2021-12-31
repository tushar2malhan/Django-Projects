from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from products.models import Product
from .models import Order


class Ordersapiview(APIView):
     def get(self, request,pk =None):

          user_id = request.GET.get('user_id')
     
          if user_id:
            orders = Order.objects.filter(user_id=user_id)
          else:
               orders = Order.objects.all()

          final_data = []
        

          for items in orders:   # looping through orders table created with json response body content where prod_id =1 
# here we check if product_id has id 1 , if yes then we show from products table 
               products = Product.objects.filter(prod_id=items.prod_id).first()
               if products:
                    products ={
                         'prod_id':products.prod_id,
                         'prod_name':products.prod_name,
                         'prod_desc':products.prod_desc,
                         'prod_price':products.prod_price,
                         'prod_avail':products.prod_avail
                    }
               else:
                    products = {}
               user = User.objects.filter(pk=items.user_id).first()
               if user:
                    users = {
                         "user_id":user.pk,
                         "user_name": user.username,
                         "user_email": user.email,
                    }
# finally we got the response dict products and users from looping through columns so we add these dict in rest of order column respectively 
               else:
                    users = {}
               result ={
                    'order_id':items.order_id,
                    'product_defination':products,
                    'user_defination':users,
                    'order_id':items.order_id,
                    'order_items':items.order_items,
                    'order_total':items.order_total
               }
               final_data.append(result)
          if pk:
               try:
                    order = Order.objects.get(order_id=pk)
               except:
                    return Response({"message":"Order id not found"})
               return Response({
                    "order":order.order_id,
                    'product_defination':products,
                    'user_defination':users,
                    'order_items':order.order_items,
                    'order_total':items.order_total
                    
                    })
          
          return Response({"data": final_data})


     
     def post(self, request,pk =None):
          user_id = int(request.data['user_id'])  
          prod_id = int(request.data['prod_id'])
          order_items = int(request.data['order_items'])
          # print(user_id)
          try:
               product = Product.objects.get(prod_id=prod_id)
          except:
               return Response({"message":"Product id  not found"})
          try:
               total = order_items * product.prod_price
          except Exception:
               total = 0.0

          order = Order.objects.create(user_id=user_id, prod_id=prod_id,order_items=order_items,order_total=total)
          return Response({"message": "Order Successful"})

     def delete(self, request,pk):
          try:
               Order.objects.get(order_id=pk).delete()
               return Response({"message": "Order Successful Deleted"})
          except:
               return Response({"message":"Order id not found"})
  


'''

we post the user id , product id  and create the object for these ids
and in get  request
we get the response using user table and their respective fields and Product table in their fields  from their ids that we posted  and 
finally put these values in dict products and users and showing it in Order table and we get the data using these ids from different tables 
'''