from django.contrib import admin
from .models import Owner
from .models import Betetkonyv_User
from .models import Sorsolas
# Register your models here.
admin.site.register(Owner)
admin.site.register(Betetkonyv_User)
admin.site.register(Sorsolas)
