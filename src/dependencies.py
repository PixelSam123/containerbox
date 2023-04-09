from collections.abc import Generator

from docker import DockerClient, from_env


def get_docker_client() -> Generator[DockerClient, None, None]:
    client = from_env()
    try:
        yield client
    finally:
        client.close()
