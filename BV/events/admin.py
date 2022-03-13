from django.contrib import admin
from .models import Event
from .models import Location
from .models import Transport
from .models import Enrollment

# Register your models here.
admin.site.register(Location)
admin.site.register(Transport)
admin.site.register(Event)
admin.site.register(Enrollment)

