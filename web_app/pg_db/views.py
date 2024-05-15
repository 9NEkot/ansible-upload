from rest_framework.response import Response
from rest_framework.decorators import api_view
import subprocess as sp
import os


@api_view()
def healthcheck(request):
    message = {}

    runn = ["web_app", "pg_app", "webapp_nginx"]
    "docker inspect web_app |jq '.[].State'"
    for r in runn:
        rr = f"docker inspect {r} |jq '.[].State'"

        os.system(f"echo {rr} > /docker-status-pipe ")
        
        with open("/out.sh", "r") as t:
            message.update({r: t.read()})
    return Response({f"message": message})
