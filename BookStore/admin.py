from django.contrib import admin
from .models import Story,Historical,Biography,Contact,Orders

# Register your models here.

admin.site.register(Story)
admin.site.register(Historical)
admin.site.register(Biography)
admin.site.register(Contact)
admin.site.register(Orders)