from rest_framework.response import Response
from rest_framework.decorators import api_view
import subprocess as sp


@api_view()
def healthcheck(request):
    return Response({f"message": f'{sp.run(["cat", "/opt/qwe"])}'})
