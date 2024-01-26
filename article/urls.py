from django.urls import path
from .views import (
                    AHome, 
                    ADetail, 
                    AUpdate, 
                    ADelete,
                    ACreate
                )

urlpatterns = [
    path('', AHome.as_view(), name='article'),
    path('new/', ACreate.as_view(), name='create'),
    path('<int:pk>/', ADetail.as_view(), name='detail'),
    path('<int:pk>/edit/', AUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', ADelete.as_view(), name='delete'),
]