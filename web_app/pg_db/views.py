from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
import os


@api_view()
def healthcheck(request):
    message = {}




    # os.system(f"echo web_app > /docker-status-pipe")
    # "docker inspect web_app |jq '.[].State'"
    # for r in runn:
    #     # rr = f"docker inspect {r} |jq '.[].State'"
    #     rr = f"docker inspect {r}"

    #     # os.system(f"echo {rr} > /docker-status-pipe ")
    #     os.system(f"echo {rr} > /docker-status-pipe")



    runn = ["web_app", "pg_app", "webapp_nginx"]
    with open("/docker-status-pipe", "w") as pipe:
        for r in runn:
            cmd = f"docker inspect {r} |jq '.[].State' "
            pipe.write(cmd)

            with open("/out.sh", "r") as t:
                message.update(
                    {
                        r: json.loads(t.read()),
                    }
                )

    return Response({f"message": message})
