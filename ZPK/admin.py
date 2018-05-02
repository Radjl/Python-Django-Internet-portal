from django.contrib import admin

# Register your models here.


from django.contrib import admin

from .models import Worker, PhoneBook

admin.site.register(Worker)
admin.site.register(PhoneBook)


