from django.urls import path

from .views import (
    main, about,contact
)

urlpatterns = [
    path('', main),
    path('about/', about),
    path('contact/', contact),
]