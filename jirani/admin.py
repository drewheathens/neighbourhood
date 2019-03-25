from django.contrib import admin
from .models import Neighborhood,Health,Notifications,Business,Health,Security,Post,Profile,medicalservices
# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Health)
admin.site.register(Business)
admin.site.register(medicalservices)
admin.site.register(Security)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Notifications)
