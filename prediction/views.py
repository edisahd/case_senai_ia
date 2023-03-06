import traceback
from django.db import DatabaseError
from rest_framework.views import APIView
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from rest_framework import status
from core.utils import error_response, response
from prediction.models import Prediction
from prediction.message import Message
import pickle
from sklearn.ensemble import AdaBoostClassifier
import numpy as np
import pandas as pd
from prediction.serializers import PredictionSerializer, PredictionInputSerializer, PredictionOutputSerializer

class PredictionView(APIView):
    message = Message()

    def post(self, request: HttpRequest) -> HttpResponse:
        serialized_input = PredictionInputSerializer(data=request.data)
        if serialized_input.is_valid():
            try:
                prediction = Prediction()
                prediction.V1 = serialized_input.data['V1']
                prediction.V2 = serialized_input.data['V2']
                prediction.V3 = serialized_input.data['V3']
                prediction.V4 = serialized_input.data['V4']
                prediction.V5 = serialized_input.data['V5']
                prediction.V6 = serialized_input.data['V6']
                prediction.V7 = serialized_input.data['V7']
                prediction.V8 = serialized_input.data['V8']
                prediction.V9 = serialized_input.data['V9']
                prediction.V10 = serialized_input.data['V10']
                prediction.V11 = serialized_input.data['V11']
                prediction.V12 = serialized_input.data['V12']
                prediction.V13 = serialized_input.data['V13']
                prediction.V14 = serialized_input.data['V14']
                prediction.V15 = serialized_input.data['V15']
                prediction.V16 = serialized_input.data['V16']
                prediction.V17 = serialized_input.data['V17']
                prediction.V18 = serialized_input.data['V18']
                prediction.V19 = serialized_input.data['V19']
                prediction.V20 = serialized_input.data['V20']
                prediction.V21 = serialized_input.data['V21']
                prediction.V22 = serialized_input.data['V22']
                prediction.V23 = serialized_input.data['V23']
                prediction.V24 = serialized_input.data['V24']
                prediction.V25 = serialized_input.data['V25']
                prediction.V26 = serialized_input.data['V26']
                prediction.V27 = serialized_input.data['V27']
                prediction.V28 = serialized_input.data['V28']
                prediction.Amount = serialized_input.data['Amount']
                loaded_model = pickle.load(open('prediction/best_model.sav', 'rb'))
                df = pd.DataFrame(
                    {
                        'V1': [prediction.V1], 
                        'V2': [prediction.V2], 
                        'V3': [prediction.V3], 
                        'V4': [prediction.V4], 
                        'V5': [prediction.V5], 
                        'V6': [prediction.V6], 
                        'V7': [prediction.V7], 
                        'V8': [prediction.V8], 
                        'V9': [prediction.V9], 
                        'V10': [prediction.V10], 
                        'V11': [prediction.V11], 
                        'V12': [prediction.V12], 
                        'V13': [prediction.V13], 
                        'V14': [prediction.V14], 
                        'V15': [prediction.V15], 
                        'V16': [prediction.V16], 
                        'V17': [prediction.V17], 
                        'V18': [prediction.V18], 
                        'V19': [prediction.V19], 
                        'V20': [prediction.V20], 
                        'V21': [prediction.V21], 
                        'V22': [prediction.V22], 
                        'V23': [prediction.V23], 
                        'V24': [prediction.V24], 
                        'V25': [prediction.V25], 
                        'V26': [prediction.V26], 
                        'V27': [prediction.V27], 
                        'V28': [prediction.V28], 
                        'Amount': [prediction.Amount],
                    }
                )
                print(df)
                x = np.array(df.iloc[0, :]).reshape(1, -1)
                print(x)
                result = loaded_model.predict(x)
                res = {
                    'Class': result[0],
                }
                prediction.Class = result[0]
                prediction.save()

                serialized_output = PredictionOutputSerializer(data=res)
                return response(
                    data=serialized_output.initial_data, 
                    status_response=status.HTTP_200_OK
                )
            except DatabaseError:
                traceback.print_exc()
                return error_response(
                    msg=self.message.server_error, 
                    status_response=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            except Exception:
                traceback.print_exc()
                return error_response(
                    msg=self.message.server_error, 
                    status_response=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        traceback.print_exc()
        return error_response(
            msg=self.message.invalid_input,
            status_response=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request: HttpRequest) -> HttpRequest:
        try:
            preditions = Prediction.objects.all()
            serialized_output = PredictionSerializer(preditions, many=True)
            return response(
                data=serialized_output.data, 
                status_response=status.HTTP_200_OK
            )
        except DatabaseError:
            return error_response(
                msg=self.message.server_error, 
                status_response=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception:
            return error_response(
                msg=self.message.server_error, 
                status_response=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class PredictionResourceView(APIView):
    message = Message()

    def get(self, request: HttpRequest, id: int) -> HttpRequest:
        try:
            predition = Prediction.objects.get(id=id)
            serialized_output = PredictionSerializer(predition)
            return response(
                data=serialized_output.data, 
                status_response=status.HTTP_200_OK
            )
        except Prediction.DoesNotExist:
            traceback.print_exc()
            return error_response(
                msg=self.message.predict_not_found, 
                status_response=status.HTTP_404_NOT_FOUND
            )
        except DatabaseError:
            traceback.print_exc()
            return error_response(
                msg=self.message.server_error, 
                status_response=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception:
            traceback.print_exc()
            return error_response(
                msg=self.message.server_error, 
                status_response=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request: HttpRequest, id: int) -> HttpResponse:
        try:
            predition = Prediction.objects.get(id=id)
            predition.delete()
            return response(
                data={'msg': self.message.successfully_deleted}, 
                status_response=status.HTTP_200_OK
            )
        except Prediction.DoesNotExist:
            traceback.print_exc()
            return error_response(
                msg=self.message.predict_not_found, 
                status_response=status.HTTP_404_NOT_FOUND
            )
        except DatabaseError:
            traceback.print_exc()
            return error_response(
                msg=self.message.server_error, 
                status_response=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception:
            traceback.print_exc()
            return error_response(
                msg=self.message.server_error, 
                status_response=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class PredictionLimitedView(APIView):
    message = Message()

    def get(self, request: HttpRequest, limit: int, offset: int) -> HttpResponse:
        if limit < 0:
            return error_response(
                msg=self.message.limit_error, 
                status_response=status.HTTP_400_BAD_REQUEST
            )
        if offset < 0:
            return error_response(
                msg=self.message.offset_error, 
                status_response=status.HTTP_400_BAD_REQUEST
            )
        try:
            preditions = Prediction.objects.all()[offset:offset+limit]
            serialized_output = PredictionSerializer(preditions, many=True)
            return response(
                data=serialized_output.data, 
                status_response=status.HTTP_200_OK
            )
        except DatabaseError:
            return error_response(
                msg=self.message.server_error, 
                status_response=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception:
            return error_response(
                msg=self.message.server_error, 
                status_response=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
