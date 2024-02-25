from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('in-time-analysis/', views.in_time_analysis, name='in_time_analysis'),
    path('top-k/', views.top_k, name='top_k'),
    path('lsi-analysis/', views.lsi_analysis, name='lsi_analysis'),
    path('speech-similarity/', views.speech_similarity, name='speech_similarity'),
    path('suprise-analysis/', views.suprise_analysis, name='suprise_analysis'),
    path('call_service/', views.call_service, name='call_service'),
    path('sidebar/', views.sidebar, name='sidebar'),
    path('image_list_topK/', views.image_list_topK, name='image_list_topK'),
    path('image_list_per_member/', views.image_list_per_member, name='image_list_per_member'),
    path('image_list_per_party/', views.image_list_per_party, name='image_list_per_party'),
    path('image_list_in_time_per_member/', views.image_list_in_time_per_member, name='image_list_in_time_per_member'),
    path('image_list_in_time_per_party/', views.image_list_in_time_per_party, name='image_list_in_time_per_party'),
    path('image_list_similarity_graph/', views.image_list_similarity_graph, name='image_list_similarity_graph'),
]
