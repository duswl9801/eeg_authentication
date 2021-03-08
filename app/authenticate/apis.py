import random
from json import dumps

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from authenticate.serializers import EEGSerializer


class CheckUserAPIView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        serializer = EEGSerializer(data=request.data)
        if serializer.is_valid():
            token = request.data['token']
            user = Token.objects.get(key=token).user
            model = user.model
            EEG = request.data['EEG']

            # 모델과 EEG 데이터를 통해 유저 인증 진행
            result = random.choice([True, False])

            if result:
                data = {
                    'detail': '인증 성공',
                }
            else:
                data = {
                    'detail': '인증 실패',
                }
            return Response(data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
