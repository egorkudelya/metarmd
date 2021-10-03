from django.contrib import admin
from .models import Context, User, Subject, Event, PersonalizedEvent

admin.site.register(Context)
admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Event)
admin.site.register(PersonalizedEvent)