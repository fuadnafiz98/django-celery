import dataclasses
from django.db.models import Q, Count, Sum, Value
from django.db.models.functions import Coalesce
from datetime import datetime, date
from decimal import Decimal
from rest_framework import viewsets

from .serializers import YoutubeSerializer, ContentSerializer, YoutubeStatsSerializer
from .models import Youtube, Content


class ContentViewset(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class YoutubeViewset(viewsets.ModelViewSet):
    queryset = Youtube.objects.all()
    serializer_class = YoutubeSerializer


@dataclasses.dataclass
class Filter:
    after: datetime = None
    before: datetime = None

    @property
    def content(self) -> dict:
        content = {}
        if self.after:
            content['youtube__created_at__gte'] = self.after
        if self.before:
            content['youtube__created_at__lte'] = self.before
        return content

    @property
    def created(self) -> Q:
        content = {}
        if self.after:
            content['youtube__created_at__gte'] = self.after
        if self.before:
            content['youtube__created_at__lte'] = self.before
        return Q(**content)

    @property
    def approved(self) -> Q:
        content = {}
        if self.after:
            content['youtube__content_approved__gte'] = self.after
        if self.before:
            content['youtube__content_approved__lte'] = self.before
        return Q(**content)


class YoutubeStatsViewset(viewsets.ModelViewSet):
    queryset = Youtube.objects.all()
    serializer_class = YoutubeStatsSerializer

    def get_queryset(self):
        after = self.request.GET.get("after")
        before = self.request.GET.get("before")
        _filter = Filter(after, before)

        queryset = (
            self.queryset.annotate(
                ordered_content=Count(
                    "youtube",
                    filter=_filter.created,
                    distinct=True
                ),
                approved_content=Count(
                    "youtube__content_approved",
                    filter=_filter.approved, distinct=True
                ),
                spent=Coalesce(
                    Sum(
                        "youtube__content_quote",
                        filter=_filter.approved,
                    ),
                    Value(Decimal(0.0))
                )
            )
        )

        return queryset
