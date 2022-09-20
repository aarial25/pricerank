from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "Sales Finder"
admin.site.site_title = "Sales Finder Admin Portal"
admin.site.index_title = "Welcome To Sales Finder"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
