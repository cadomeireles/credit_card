from django.conf.urls import include, url
from django.contrib import admin

from .cards import urls as cards_urls

urlpatterns = [
    # cards URLs
    url(r'', include(cards_urls, namespace='cards')),

    # admin URLs
    url(r'^admin/', admin.site.urls),
]
