# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *


class MochiLeaderboard(gl.Contract):
    names:  TreeMap[str, str]
    scores: TreeMap[str, u256]

    @gl.public.write
    def submit_score(self, name: str, score: int) -> None:
        assert 1 <= len(name) <= 20, "Name must be 1-20 characters"
        assert score >= 0, "Score must be non-negative"
        moderation_result = gl.eq_principle.prompt_comparative(
            lambda: gl.nondet.exec_prompt(
                f'Is the username {repr(name)} appropriate for a family-friendly '
                f'cyberpunk skateboarding game leaderboard? '
                f'Reject if: profanity, slurs, sexual content, cheat-references, or attacks. '
                f'Respond only: yes or no.'
            ),
            principle="yes if appropriate, no if it should be rejected",
        )
        assert moderation_result.lower().strip().startswith("yes"), "Username rejected by AI moderation"
        caller = str(gl.message.sender_address)
        existing = self.scores.get(caller)
        if existing is None or score > existing:
            self.names[caller]  = name
            self.scores[caller] = u256(score)

    @gl.public.view
    def get_top_scores(self, n: int) -> list:
        assert 1 <= n <= 100
        entries = [{"address": a, "name": self.names[a], "score": int(self.scores[a])} for a in self.scores]
        entries.sort(key=lambda x: x["score"], reverse=True)
        return entries[:n]

    @gl.public.view
    def get_score(self, address: str) -> dict:
        s = self.scores.get(address)
        return {} if s is None else {"name": self.names[address], "score": int(s)}

    @gl.public.view
    def get_total_players(self) -> int:
        return len(self.scores)
