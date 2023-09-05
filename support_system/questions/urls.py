from django.urls import path
from . import views

urlpatterns = [
    path('', views.questions_home, name='questions_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.QuestionsDetailView.as_view(), name='questions-detail'),
    path('<int:pk>/update', views.QuestionsUpdateView.as_view(), name='questions-update'),
    path('<int:pk>/delete', views.QuestionsDeleteView.as_view(), name='questions-delete')

]
