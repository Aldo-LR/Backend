from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('cancion/', views.CancionView.as_view(),name='cancion'),
    path('delete/<int:cancion_id>', views.DeleteView.as_view(),name='delete'),
    path('put/<int:cancion_id>', views.ActualizarView.as_view(),name='actualizar'),
]