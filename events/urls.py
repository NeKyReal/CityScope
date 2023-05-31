from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    # path('', cache_page(60)(views.all), name='all'),
    path('', views.all, name='all'),
    path('create', views.create, name='create'),
    path('search', views.SearchResultsView.as_view(), name='search'),
    path('<int:pk>', views.EventsDetailView.as_view(), name='events-detail'),
    path('<int:pk>/update', views.EventsUpdateView.as_view(), name='events-update'),
    path('<int:pk>/delete', views.EventsDeleteView.as_view(), name='events-delete'),
    path('<int:pk>/featured', views.wishlist, name='featured')
]
