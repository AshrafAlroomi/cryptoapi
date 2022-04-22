from .serializers import StrategySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from CryptoApi.models.models import TradingStrategy


class StrategiesView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = StrategySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class StrategyView(APIView):

    def get(self, request):
        strategy = TradingStrategy.objects.get(user=request.user)
        serializer = StrategySerializer(strategy)
        return Response(serializer.data)

    def put(self, request):
        pass

    def delete(self, request):
        pass
