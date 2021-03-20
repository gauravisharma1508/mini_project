from django.contrib import admin

from .models import Members,Trains,Station,Route,RouteStation,Reservation,Payment
# Register your models here.
admin.site.register(Members)
admin.site.register(Trains)
admin.site.register(Station)
admin.site.register(Route)
admin.site.register(RouteStation)
admin.site.register(Reservation)
admin.site.register(Payment)