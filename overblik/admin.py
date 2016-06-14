from django.contrib import admin
from overblik.models import Company, Customer, Platform, HostingProvider
from overblik.models import Server, Solution, Domain, Contact
from overblik.models import RegisteredAddress

# Register your models here.
admin.site.register(RegisteredAddress)
admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(Platform)
admin.site.register(HostingProvider)
admin.site.register(Server)
admin.site.register(Solution)
admin.site.register(Domain)
admin.site.register(Contact)
