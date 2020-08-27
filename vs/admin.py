from django.contrib import admin
from .models import Candidate, Position,State,Account,ControlVote
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display    =   ('email','username','date_joined','last_login','is_admin','is_staff')
    search_fields    =   ('email','username',)
    readonly_fields =   ('date_joined','last_login')

    filter_horizontal = ()
    list_filter =  ()
    fieldsets = ()




@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name','position')
    list_filter = ('position',)
    search_fields = ('name','position')
    readonly_fields = ('total_vote',)
   
admin.site.register(State)       
admin.site.register(Account,AccountAdmin)
admin.site.register(ControlVote)
