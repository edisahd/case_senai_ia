from typing import Any, NoReturn
from django.db import DatabaseError
from django.http import HttpResponse
from rest_framework.response import Response
from authentication.models import LogSystem
import traceback

def error_response(msg: str, status_response: int) -> HttpResponse:
    return Response(data={'msg': msg}, status=status_response)

def response(data: Any, status_response: int) -> Response:
    return Response(data=data, status=status_response)


def logger(location: str, log: str) -> NoReturn:
    try:
        log_system = LogSystem()
        log_system.location = location
        log_system.log = log
        log_system.save()
        pass
    except DatabaseError:
        traceback.print_exc()
        pass
    except Exception:
        traceback.print_exc()
        pass
    pass