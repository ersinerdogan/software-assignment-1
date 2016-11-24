from django.conf.urls import url, include
from django.contrib import admin
from blogg import views
urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^blog/entries/$", views.see_all),
    url(r"^blog/entries/+(?P<blog_id>[0-9]+)$", views.see_one)
]

