from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .form import CustomUserCreateForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin) :
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    model = CustomUser
    # Para controlar qué campos aparecerán en la página 
    list_display = ['email', 'username', 'age', 'is_staff']
    # Editar nuevos campos 
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                'age',
            ),
        }),
    )
    # Añadir nuevos campos
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields": (
                'age',
            ),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)

