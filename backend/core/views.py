from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination, CursorPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core.models import Car
from core.serializers import CarSerializers
from core.models import Users
from core.serializers import UsersSerializers


class MyPagination(CursorPagination):
    page_size = 15
    ordering = 'id'


# def all_cars(request):
#     result = []
#     cars = Car.objects.all()
#     for car in cars:
#         result.append(CarSerializers(car).data)
#     return  JsonResponse(result, safe=False)

class CarViewSet(ModelViewSet):
    serializer_class = CarSerializers
    queryset = Car.objects.all()
    pagination_class = MyPagination


class UserViewSet(ModelViewSet):
    serializer_class = UsersSerializers
    queryset = Users.objects.all()


class SnippetDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'key': 'KarCalendar121'})
