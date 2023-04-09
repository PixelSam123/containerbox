from docker import DockerClient
from fastapi import APIRouter, Depends

from .. import schemas
from ..dependencies import get_docker_client

router = APIRouter(prefix="/")


@router.post("/")
def root(
    code_exec_request: schemas.CodeExecRequest,
    docker_client: DockerClient = Depends(get_docker_client),
) -> dict[str, int | str]:
    lang_to_image = {
        "js": "node",
    }

    image = lang_to_image[code_exec_request.lang]

    if image not in docker_client.images.list():
        docker_client.images.pull(image)

    run_result = docker_client.containers.run(
        image,
        command=["node", "-e", code_exec_request.code],
        stderr=True,
        remove=True,
        mem_limit="8m",
        nano_cpus=100_000_000,  # 0.1 cores
        network_disabled=True,
        privileged=False,
    )

    return {
        "status": 0,
        "output": str(run_result),
    }
