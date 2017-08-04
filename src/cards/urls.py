from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^$',
        views.UploadCardsView.as_view(),
        name='upload',
    ),
]
