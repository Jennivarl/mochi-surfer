from genlayer import *

@gl.contract
class MochiLeaderboard:
    names: TreeMap[str, str]
    scores: TreeMap[str, int]

    def __init__(self) -> None:
        self.names = TreeMap()
        self.scores = TreeMap()

    @gl.public.write
    def submit_score(self, name: str, score: int) -> None:
        assert 1 <= len(name) <= 20
        assert score >= 0
        caller = str(gl.message.sender)
        existing = self.scores.get(caller)
        if existing is None or score > existing:
            self.names[caller] = name
            self.scores[caller] = score

    @gl.public.view
    def get_score(self, address: str) -> int:
        return self.scores.get(address) or 0
