from django.contrib import admin

from .models import Poll, Bulletin

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    fields = ('title', 'face_participants')

@admin.register(Bulletin)
class BulletinAdmin(admin.ModelAdmin):
    pass

