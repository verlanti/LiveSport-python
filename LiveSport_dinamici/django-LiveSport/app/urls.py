from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('',views.IndexView.as_view(), name = 'index'),
    path('campionato/',views.CampionatoView.as_view(), name = 'campionato'),
    path('campionato/<int:pk>/',views.CalendarioView.as_view(), name = 'calendario'),
    path('campionato/<int:pk>/calendarioall/',views.CalendarioAllView.as_view(), name = 'calendarioall'),
    path('campionato/<int:pk>/classifica/',views.ClassificaView.as_view(), name = 'classifica'),
    path('campionato/<int:pk>/schedina/',views.SchedinaView.as_view(), name = 'schedina'),
    path('campionato/<int:pk>/<int:id_squadra>/squadra/',views.SquadraView.as_view(), name = 'squadra'),
]
