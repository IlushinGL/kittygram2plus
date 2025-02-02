from rest_framework import viewsets
# from rest_framework.throttling import AnonRateThrottle

from .models import Achievement, Cat, User
from .permissions import OwnerOrReadOnly
from .serializers import AchievementSerializer, CatSerializer, UserSerializer
from .pagination import CatsPagination
# from .throttling import WorkingHoursRateThrottle


class CatViewSet(viewsets.ModelViewSet):
    """
    Записи о котиках.
    """
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (OwnerOrReadOnly,)
    pagination_class = CatsPagination
    # throttle_classes = (WorkingHoursRateThrottle,)
    # throttle_classes = (AnonRateThrottle,)
    throttle_scope = 'low_request'

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Записи об владельцах котиков.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    """
    Записи об активности котиков.
    """
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
