from django.contrib.admin.apps import AdminConfig

class AmaralAdminConfig(AdminConfig):
    default_site = "cardapio.admin.AmaralAdminSite"