from django.urls import path,include
from .import views
from ..account.urls import urlpatterns

urlpatterns=[
    path('post_feedback',views.post_feedback,name='post_feedback'),
    path('get_feedback',views.get_feedback,name='get_feedback')

]