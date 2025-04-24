from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Corrected opening and closing quotes
    path("", include("main_app.urls")),  # Fixed app name and 'urls'
    path("account/", include("account.urls")),
    path("chat/", include("chat.urls")),  # Corrected duplicate empty path
]
