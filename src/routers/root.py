from docker import DockerClient
from docker.models.containers import Container
from fastapi import APIRouter, Depends
from requests.exceptions import ReadTimeout

from .. import schemas
from ..dependencies import get_docker_client

router = APIRouter(prefix="/")


@router.post("/")
def root(
    code_exec_request: schemas.CodeExecRequest,
    docker_client: DockerClient = Depends(get_docker_client),
) -> dict[str, int | str]:
    timeout_seconds = 5

    lang_to_image = {
        "js": "node:18-alpine",
    }

    image = lang_to_image[code_exec_request.lang]

    container: Container = Container(
        docker_client.containers.run(
            image,
            detach=True,
            command=["node", "-e", code_exec_request.code],
            mem_limit="8m",
            nano_cpus=100_000_000,  # 0.1 cores
            network_disabled=True,
            privileged=False,
        )
    )

    try:
        run_result = container.wait(timeout=timeout_seconds)

        output = str(container.logs(stdout=True, stderr=True))

        return {
            "status": int(run_result["StatusCode"]),
            "output": output,
        }
    except ReadTimeout:
        output = f"Timeout after {timeout_seconds} seconds"

        return {
            "status": 1,
            "output": output,
        }
    finally:
        container.remove(force=True)
