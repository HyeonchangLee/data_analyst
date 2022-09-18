from django.contrib import admin
from membership.models import BourgeoisMember

@admin.register(BourgeoisMember)
class BourgeoisMember(admin.ModelAdmin):
    list_display = ['ID', 'NAME', 'AGE','GENDER','LEGION']
