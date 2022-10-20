from django.urls import include, path
from rest_framework import routers

from .views import Viewset

router = routers.DefaultRouter()
router.register(r'query', Viewset)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    *router.urls
]
