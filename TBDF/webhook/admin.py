from django.contrib import admin

# Register your models here.

from webhook.models import Sample
admin.site.register(Sample)