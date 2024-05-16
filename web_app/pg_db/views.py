from rest_framework.response import Response
from rest_framework.decorators import api_view
import os


@api_view()
def healthcheck(request):
    message = {}

    runn = ["web_app", "pg_app", "webapp_nginx"]
    # os.system(f"echo web_app > /docker-status-pipe")
    # "docker inspect web_app |jq '.[].State'"
    # for r in runn:
    #     # rr = f"docker inspect {r} |jq '.[].State'"
    #     rr = f"docker inspect {r}"

    #     # os.system(f"echo {rr} > /docker-status-pipe ")
    #     os.system(f"echo {rr} > /docker-status-pipe")
    with open("/docker-status-pipe", "w") as pipe:
        pipe.write("docker inspect web_app")

    with open("/out.sh", "r") as t:
        message.update({"web+app": t.read()})

    return Response({f"message": message})
