from django.contrib import admin

from .models import Place
from .models import Guides

admin.site.register(Place)
admin.site.register(Guides)