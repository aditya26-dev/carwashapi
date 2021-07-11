from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Washer)
admin.site.register(models.Service)
admin.site.register(models.Package)
admin.site.register(models.Order)
admin.site.register(models.Rating)

admin.site.register(models.nilai)
admin.site.register(models.buku)
admin.site.register(models.bantuan)
admin.site.register(models.berita)
