from django.shortcuts import render

from  rest_framework.views import APIView
from  rest_framework.response import Response


from .models import Product


class Productapiview(APIView):
     def get(self,request,pk=None):
          final=[]
          try:
               if pk :
                    item = Product.objects.get(prod_id=pk)
                    final.append({
                         "prod_id": item.prod_id,
                         "prod_name":item.prod_name,
                         "prod_desc":item.prod_desc,
                         "prod_price":item.prod_price,
                         "prod_avail":item.prod_avail
                    })
               else:
                    product = Product.objects.all()
                    for item in product:
                         result ={
                              "prod_id": item.prod_id,
                              "prod_name":item.prod_name,
                              "prod_desc":item.prod_desc,
                              "prod_price":item.prod_price,
                              "prod_avail":item.prod_avail
                         }

                         final.append(result)
               
               return Response({'data':final})
          except Product.DoesNotExist:
               return Response({'data':'Product.DoesNotExist'})

     def post(self,request,pk=None):
          id = request.data['prod_id']
          name = request.data['prod_name']
          desc = request.data['prod_desc']
          price = request.data['prod_price']
          avail = request.data['prod_avail']


          get,create = Product.objects.get_or_create(prod_id=id,prod_name=name,prod_desc=desc,prod_price=price,prod_avail=avail)
          if create:
               return Response({'data':'Product created successfully '})
          return Response({'data':'Product already listed  '})
  
     def delete(self, request,pk =None):
          Product.objects.filter(prod_id=pk).delete()
          return Response({"data": "delete request"})

     def put(self, request,pk=None):
          id = request.data['prod_id']
          name = request.data['prod_name']
          desc = request.data['prod_desc']
          price = request.data['prod_price']
          avail = request.data['prod_avail']
          obj = Product.objects.filter(prod_id=pk).update(prod_id=id,prod_name=name,prod_desc=desc,prod_price=price,prod_avail=avail)
          
          return Response({"data": "put request updated"})
