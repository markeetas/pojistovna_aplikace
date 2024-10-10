from django.contrib import admin
from pojisteni.models import Insured, Insurance, InsuranceEvent, UserRole, Statistics

admin.site.register(Insured)
admin.site.register(Insurance)
admin.site.register(InsuranceEvent)
admin.site.register(UserRole)
admin.site.register(Statistics)