from django.urls import path
from .views import SnackListView,SnackDetailView
urlpatterns = [
    path('', SnackListView.as_view(),name = 'snacklist'),
    path('<pk>/', SnackDetailView.as_view(),name = 'snackdetail'),

]