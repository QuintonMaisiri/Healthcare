from django.contrib import admin
from django.apps import apps

# Register your models here.
appointment_models = apps.get_app_config('appointmentCreation').get_models()

for model in appointment_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
