from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^layout/', LayoutView.as_view(), name="layout"),
    url(r'^$', LoginView.as_view(), name="login"),
    url(r'^logout/', LogoutView.as_view(), name="logout"),
    url(r'^sorting/', SortingView.as_view(), name="sorting"),
]

