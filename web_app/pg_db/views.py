from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def healthcheck(request):
    return Response({"message": "Hello, world!"})
