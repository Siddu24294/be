from django.urls import path
from .views import UserCreatListView


urlpatterns=[
	path("user/",UserCreatListView.as_view(),name="user-list"),
]