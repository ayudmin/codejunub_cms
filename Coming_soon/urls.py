from django.urls import path
from django.conf.urls.static import static
from core import views
from Coming_soon import base

urlpatterns = [
    path('', views.homepage)

]

urlpatterns += static(base.STATIC_URL, document_root=base.STATIC_ROOT)
