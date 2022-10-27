from django.urls import URLPattern


from django.urls import path
from . import views
# http://127.0.0.1:8000/            => homepage
# http://127.0.0.1:8000/index       => homepage
# http://127.0.0.1:8000/isarama     => isarama
# http://127.0.0.1:8000/isarama/3   =>isarama-details

urlpatterns = [
    path("",views.index),
    path("index",views.index),
    path("blogs",views.index),
    path("isarama/<int:id>", views.isarama_details),
]