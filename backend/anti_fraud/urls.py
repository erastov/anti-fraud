"""cert_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from api.views import (
    LoginView,
    UserSettings,
    LogoutView,
    TransactionViewSet,
    CustomerViewSet,
    AccountViewSet
    )
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

router = routers.SimpleRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/login/$', LoginView.as_view()),
    url(r'^api/logout$', LogoutView.as_view()),
    url(r'^api/user-settings/$', UserSettings.as_view()),
    url(r'^swagger/$', schema_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
