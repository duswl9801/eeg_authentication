from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .EEG_CNN import *
from tensorflow import keras

from authenticate.serializers import EEGSerializer

from scipy import signal


# 처음 가입했을 때 사용
class MakeEEGModelAPIView(APIView):
    parser_classes = (MultiPartParser,)  # 파일을 받기 위해 사용

    def post(self, request):
        serializer = EEGSerializer(data=request.data)
        if serializer.is_valid():
            token = request.data['token']
            user = Token.objects.get(key=token).user
            eeg = request.data['EEG']

            train_data, train_label = make_train_dataset(eeg)
            input_shape = train_data.shape[-2:]
            model = make_model(input_shape)
            model.fit(train_data, train_label, batch_size=20, epochs=1, verbose=0)

            save_file = f'../media/{user.username}.h5'
            model.save(save_file)
            user.model = save_file
            user.save()

            return Response({
                'detail': '저장완료.'
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 가입 후 인증할 때 사용
class CheckUserAPIView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        serializer = EEGSerializer(data=request.data)
        if serializer.is_valid():
            token = request.data['token']
            user = Token.objects.get(key=token).user

            # 저장된 model load
            saved_model = user.model
            model = keras.models.load_model(str(saved_model))

            eeg = request.data['EEG']  # 받아온 결과
            eeg, _ = make_data(eeg)

            test_predict = model.predict(eeg)
            right_cnt = sum(test_predict >= 0.5)[0]

            test_case = len(eeg)
            result = right_cnt / test_case

            # 모델에 EEG 데이터 retraining

            data = {
                '전체 Test': test_case,
                '맞은 Test': right_cnt,
                '맞은 비율': result,
            }
            if result >= 0.85:
                data['detail'] = '인증 성공'
            else:
                data['detail'] = '인증 실패'
            return Response(data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
