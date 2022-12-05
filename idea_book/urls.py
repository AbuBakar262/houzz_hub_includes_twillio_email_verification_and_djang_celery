from django.urls import path
from idea_book.view.tag_views import CreateTagViewSet, ListTagViewSet, UpdateDeleteTagViewSet
from idea_book.view.idea_book_views import CreateIdeaBookViewSet

urlpatterns = [
    #tag_views
    path('create_tag/', CreateTagViewSet.as_view({'post': 'create'}), name='create_tag'),
    path('list_tags/', ListTagViewSet.as_view({'get': 'list'}), name='list_tag'),
    path('update_tag/<int:pk>/', UpdateDeleteTagViewSet.as_view({'put': 'update'}), name='update_tag'),
    path('delete_tag/<int:pk>/', UpdateDeleteTagViewSet.as_view({'delete': 'destroy'}), name='delete_tag'),

    #idea_book_views
    path('create_idea/', CreateIdeaBookViewSet.as_view({'post': 'create'}), name='create_idea'),
    path('list_ideas/', CreateIdeaBookViewSet.as_view({'get': 'list'}), name='list_idea'),
    path('delete_idea/<int:pk>/', CreateIdeaBookViewSet.as_view({'delete': 'destroy'}), name='delete_idea'),
    path('update_idea/<int:pk>/', UpdateDeleteTagViewSet.as_view({'put': 'update'}), name='update_idea'),
]
