from typing import Literal

from pydantic import BaseModel


class CodeExecRequest(BaseModel):
    lang: Literal["js"]
    code: str
