from django.contrib import admin


# Register your models here.
class RegisterSystem(admin.ModelAdmin):
    list_display = ('name', 'surname', 'telegram_username', 'phone_number', 'deleted_status')
