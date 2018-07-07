from django.contrib import admin

# Register your models here.

from trip.models import Ctrip
from trip.models import Mafengwo
from trip.models import Place

admin.site.register(Ctrip)
admin.site.register(Mafengwo)
admin.site.register(Place)