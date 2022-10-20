from django.urls import include, path
from rest_framework import routers

from .views import YoutubeViewset, ContentViewset, YoutubeStatsViewset

router = routers.DefaultRouter()
router.register(r'youtube/stats', YoutubeStatsViewset)
router.register(r'youtube', YoutubeViewset)
router.register(r'content', ContentViewset)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    *router.urls
]
