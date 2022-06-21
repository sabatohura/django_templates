from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path("",views.testview),
    path("trainee/",views.all_trainee)
]