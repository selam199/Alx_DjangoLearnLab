from django.urls import path
from .views import NotificationListView, NotificationMarkAsRead

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
    path('<int:pk>/read/', NotificationMarkAsRead.as_view(), name='notification-read'),
]