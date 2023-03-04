from django.urls import path
from django.conf.urls.static import static
from core import views
from django.conf import settings

urlpatterns = [
    path('', views.homepage)

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
