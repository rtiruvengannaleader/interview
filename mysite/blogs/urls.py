from django.urls import include, path
# import routers
from rest_framework import routers
 
# import everything from views
from blogs.views import EntryViewSet, TagsAPIView
 
# define the router
router = routers.DefaultRouter()
 
# define the router path and viewset to be used
router.register(r'blogs', EntryViewSet)
 

urlpatterns = [
    path('tags/' , TagsAPIView.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]