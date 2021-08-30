from django.contrib import admin
from . models import User, UserType

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name',
                    'last_name',
                    'email',
                    'user_type',
                    'is_active'
                    )
    list_editable = ('user_type',)
    search_fields = ('email',)

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'created_at'
                    )


