import random

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .EEG_CNN import *
from config.settings import ROOT_DIR

from authenticate.serializers import EEGSerializer

from scipy import signal


def fir_filter(data, lowcut, highcut, fs, order=29):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    if low == 0 and high == 1:
        return data
    elif low == 0 and high != 1:
        coeff = signal.firwin(order, highcut / nyq)
    elif low != 0 and high == 1:
        coeff = signal.firwin(order, lowcut / nyq, pass_zero=False)
    elif low != 0 and high != 1:
        coeff = signal.firwin(order, [low, high], pass_zero=False)
    output = signal.lfilter(coeff, 1.0, data)
    return output


# def EEG_CNN_Network(eeg_data):
#     train_data, train_label = make_train(eeg_data)
#     input_shape = train_data.shape[-2:]
#     model = make_model(input_shape)
#     res = model.fit(train_data, train_label, batch_size=20, epochs=20, verbose=0)
#
#     return res


# 처음 가입했을 때 사용
class MakeEEGModelAPIView(APIView):
    parser_classes = (MultiPartParser,)  # 파일을 받기 위해 사용

    def post(self, request):
        serializer = EEGSerializer(data=request.data)
        if serializer.is_valid():
            token = request.data['token']
            user = Token.objects.get(key=token).user
            eeg = request.data['EEG']

            train_data, train_label = make_train(eeg)
            input_shape = train_data.shape[-2:]
            model = make_model(input_shape)
            model.fit(train_data, train_label, batch_size=20, epochs=1, verbose=0)

            save_file = f'../media/{user.username}.h5'
            model.save(save_file)
            user.model = save_file
            user.save()

            return Response({
                'detail': 'Success.'
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 가입 후 인증할 때 사용
class CheckUserAPIView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        # 재학습

        # 결과 return

        serializer = EEGSerializer(data=request.data)
        if serializer.is_valid():
            token = request.data['token']
            user = Token.objects.get(key=token).user
            model = user.model  # 저장된 모델
            eeg = request.data['EEG']  # 받아온 결과

            # 모델에 EEG 데이터 retraining

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
