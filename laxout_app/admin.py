from django.contrib import admin
from .models import Laxout_Exercise, Laxout_User

class Laxout_UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('exercises',)

admin.site.register(Laxout_Exercise)
admin.site.register(Laxout_User, Laxout_UserAdmin)
