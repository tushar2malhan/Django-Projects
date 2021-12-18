# from django2.djangoapp2.models import Mammal
from django.contrib import admin
from .models import Mammal ,Bird , Fish

admin.site.register(Mammal)
admin.site.register(Bird)
admin.site.register(Fish)
