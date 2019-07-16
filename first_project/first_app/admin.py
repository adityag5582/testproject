from django.contrib import admin
from first_app.models import AcessRecord,WebPage,Topic
# Register your models here.
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AcessRecord)
