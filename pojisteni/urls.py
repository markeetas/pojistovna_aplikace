from django.urls import path
from . import views, url_handlers

urlpatterns = [
    # Pojištěnci
    path("insured_index/", views.InsuredIndex.as_view(), name="insured_index"),
    path("<int:pk>/insured_detail/", views.CurrentInsured.as_view(), name="insured_detail"),
    path("create_insured/", views.CreateInsured.as_view(), name="novy_pojisteny"),
    path('edit/<int:pk>/', views.edit_insured, name='edit_insured'),
    path('delete/<int:pk>/', views.delete_insured, name='delete_insured'),

    # Pojištění
    path("insurance_index/", views.InsuranceIndex.as_view(), name="insurance_index"),
    path("insurance/create/<int:pk>/", views.add_insurance, name="add_insurance"),
    path("insurance/edit/<int:pk>/", views.edit_insurance, name="edit_insurance"),
    path("insurance/delete/<int:pk>/", views.delete_insurance, name="delete_insurance"),

    # Pojistné události
    path("events_index/", views.EventsIndex.as_view(), name="events_index"),
    path('events/create/', views.EventCreateView.as_view(), name='event_create'),

    # Ostatní
    path("about/", views.About.as_view(), name="about"),
    path('', views.HomeView.as_view(), name='home'),
    path("", url_handlers.index_handler),

    # Uživatelské přihlášení
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

]

