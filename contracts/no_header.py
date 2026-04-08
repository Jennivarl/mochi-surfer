from genlayer import *

@gl.contract
class NoHeader:
    msg: str

    def __init__(self) -> None:
        self.msg = "hello"

    @gl.public.view
    def get(self) -> str:
        return self.msg
