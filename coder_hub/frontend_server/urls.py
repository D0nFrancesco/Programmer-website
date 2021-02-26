from django.urls import path
import frontend_server.views as views
from .views import ArticleListView, ArticleDetailView


# this is deffinitly not final
urlpatterns = [
    path("", views.index),
    path("projects", views.index),
    path("social", views.index),
    path("login", views.index),
    path("register", views.index),
]


urlpatterns = [
    path('', PostListView.as_view())#not nessesary
    path('<pk>', PostDetailView.as_view())
]