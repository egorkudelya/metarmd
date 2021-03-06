from django.urls import path
from api import views

urlpatterns = [
    path('contexts/', views.ContextView.as_view()),
    path('contexts/<str:context_id>/subjects/', views.SubjectView.as_view()),
    path('contexts/<str:context_id>/subjects/<str:subject_id>/events', views.EventView.as_view()),
    path('contexts/<str:context_id>/users/', views.UserView.as_view()),
    path('contexts/<str:context_id>/users/<str:user_id>/events/', views.UserEventsView.as_view()),
    # path('contexts/<str:context_id>/users/<str:user_id>/events/<str:event_id>', views.PersonalizedEventView.as_view()),  # patch event
    path('contexts/<str:context_id>/users/<str:user_id>/', views.MainUserEndPoint.as_view()),  # internal port
    path('contexts/<str:context_id>/', views.MainContextEndPoint.as_view()),  # internal port, used only by reminder api
]