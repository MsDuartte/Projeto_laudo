from django.contrib import admin
from django.urls import path
from laudos.views import (
    HomeView, AddTemplateView, TemplateListView, LaudoListView, LaudoDetailView,
    LaudoUpdateView, LaudoDeleteView, TemplateDetailView, TemplateUpdateView, TemplateDeleteView
)
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    path('add_template/', AddTemplateView.as_view(), name='add_template'),
    path('template_list/', TemplateListView.as_view(), name='template_list'),
    path('laudo_list/', LaudoListView.as_view(), name='laudo_list'),
    path('laudo/<int:pk>/', LaudoDetailView.as_view(), name='laudo_detail'),
    path('laudo/<int:pk>/edit/', LaudoUpdateView.as_view(), name='laudo_edit'),
    path('laudo/<int:pk>/delete/', LaudoDeleteView.as_view(), name='laudo_delete'),
    path('template/<int:pk>/', TemplateDetailView.as_view(), name='template_detail'),
    path('template/<int:pk>/edit/', TemplateUpdateView.as_view(), name='template_edit'),
    path('template/<int:pk>/delete/', TemplateDeleteView.as_view(), name='template_delete'),
]
