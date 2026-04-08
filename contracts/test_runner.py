# { "Depends": "py-genlayer:test" }
from genlayer import *

@gl.contract
class TestRunner:
    msg: str

    def __init__(self) -> None:
        self.msg = "hello"

    @gl.public.view
    def get(self) -> str:
        return self.msg
