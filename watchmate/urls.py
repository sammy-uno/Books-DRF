from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('api/books/', include('book_app.api.urls')),
    path('api/account/', include('user_app.api.urls')),

    # path('api-auth/', include('rest_framework.urls')),
]
