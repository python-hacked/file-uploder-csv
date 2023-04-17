from django.urls import path
from .views import home, admin_page, download_file, view_file

urlpatterns = [
    path('', home, name='home'),
    path('admin_all/', admin_page, name='admin_page'),
    path('download/<int:file_id>/', download_file, name='download_file'),
    path('view/<int:file_id>/', view_file, name='view_file'),
]
