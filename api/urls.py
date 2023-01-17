from django.contrib import admin
from django.urls import path
# from api.views import import_order
from api import views as api_views
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from django.urls import path 

urlpatterns = [
    # path('import-order/', import_order),
    path('import-order/', api_views.ImportOrder.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
]