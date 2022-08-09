from django.apps import AppConfig


class MydebtorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mydebtors'

    def ready(self):
        import mydebtors.signals