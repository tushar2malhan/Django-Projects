from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
import json 



@csrf_exempt
def app(request,number=0):
    if request.method=='GET':
        num = request.GET.get('number')
        if num:
            a=(int(num) *int(num))
            return HttpResponse(f'Square of Number {num} is {a}' )
        else:
            return HttpResponse('Send Parameter number in url')
    
    if request.method =='POST': 
        # data=json.loads(request.body.decode('utf-8'))                                   # access body in raw with json format ! 
        # print()
        # a=data.get('number','Send Parameter number in url')
        a1=request.POST.get('number' )                                                    # access form-data 
        if a1:
            a1_1 = int(a1)* int(a1)
            return JsonResponse({"data": f"Square of Number {a1} is {a1_1}"})
        return HttpResponse('Send Parameter number in data')

    if request.method =='PUT':
        if number  :
            num =int(number) * int(number)
            return JsonResponse({"data": f"Square of Number {number} is {num}"})
        else:
            return HttpResponse('Send Parameter as /simpleapp/<number>')
   
    if request.method =='DELETE':
        if number:
            num =int(number) * int(number)
            return JsonResponse({"data": f"Square of Number {number} is {num}"})
        return HttpResponse('Send Parameter as /simpleapp/<number>')
    
@csrf_exempt
def palindrome_chk(request,strr=None):
    if request.method =='GET':
        str=request.GET.get('string' )    
        if str :
            if str == str[::-1]:
                return JsonResponse({"result": f"{str} is a palindrome"})
            else:
                return HttpResponse(f"<b>{str}</b> is not a palindrome")

        return HttpResponse('Send Parameter string in URL to check palindrome')
    
    if request.method =='POST':
        str=request.POST.get('string','Send Parameter string in URL to check palindrome')    
        if str == str[::-1]:
            return JsonResponse({"result": f"{str} is a palindrome"})
        else:
            return HttpResponse(f"<b>{str}</b> is not a palindrome")

    if request.method =='PUT':
        print(strr)
        if strr is not None:
            if strr == strr[::-1]:
                return JsonResponse({"result": f"{strr} is a palindrome"})
            else:
                return HttpResponse(f"<b>{strr}</b> is not a palindrome")
        
        return HttpResponse(f"Send parameter as /palindrome_check/<string>")
    
    if request.method =='DELETE':
            if strr == strr[::-1]:
                return JsonResponse({"result": f"{strr} is a palindrome"})
            return HttpResponse(f"<b>{strr}</b> is not a palindrome")

@csrf_exempt
def indexx(request):
    if request.method=='GET':
        num = request.GET.get('array','Send Parameter array as comma seperated numbers 2,3,4,5').split(',')
        a=[int(s) for s in num]
        a = list(map(int,num))
        return HttpResponse(f'Sum is {sum(a)}')
    
    if request.method =='POST':
        num = request.POST.get('array','Send Parameter array as comma seperated numbers 2,3,4,5').split(',')
        a=[int(s) for s in num]
        return HttpResponse(sum(a))
