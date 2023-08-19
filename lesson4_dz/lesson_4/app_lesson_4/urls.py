from django.urls import path
from .views import func,index
urlpatterns = [
    path('', func),
    path('lesson_4', index)
]