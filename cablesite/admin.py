from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Cable)
admin.site.register(User)
admin.site.register(Strand)
admin.site.register(Device)
admin.site.register(Panel)


