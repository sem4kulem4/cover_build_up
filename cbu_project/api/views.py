from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Curve
from .serializers import CurveSerializer


class CurveAPI(APIView):
    def get(self, request):
        curves = Curve.objects.filter(user=self.request.user)
        serializer = CurveSerializer(curves, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CurveSerializer(many=True, data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
