from django.contrib import admin
from .models import Poll, Questions, UserAnswer

admin.site.register(Poll)
admin.site.register(Questions)
admin.site.register(UserAnswer)
