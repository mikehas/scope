from django.contrib import admin
from directory.models import Interest, Location, Perspective, Report, Service, Location_service, Location_hour, Operator, Location_operator, Project

admin.site.register(Interest)
admin.site.register(Location)
admin.site.register(Perspective)
admin.site.register(Report)
admin.site.register(Service)
admin.site.register(Location_service)
admin.site.register(Location_hour)
admin.site.register(Operator)
admin.site.register(Location_operator)
admin.site.register(Project)