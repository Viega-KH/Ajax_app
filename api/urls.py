from django.urls import path
from .views import Index, AddViews, EditViews, get_product, DeleteViews, CheckView, HomeViews, ApiListViews

urlpatterns = [
    path( '', Index, name='index' ),
    path( 'home/', HomeViews, name='home' ),
    path( 'add/', AddViews, name='add' ),
    path( 'edit/', EditViews, name='edit' ),
    path('get_product/<int:id>/', get_product, name='get_product'),
    path('delete/', DeleteViews, name='delete'),
    path('delete/check/', CheckView, name='delete_check'),
    # Api
    path('api/get/list/order/', ApiListViews.as_view(), name='api_get'),
]
