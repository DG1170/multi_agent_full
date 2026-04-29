import ast
from .base import BaseAgent

class ReviewAgent(BaseAgent):
    def handle(self, msg):
        code = msg["code"]
        try:
            ast.parse(code)
            self.log("Review OK")
            self.bus.publish("review.passed", {"code": code})
        except Exception as e:
            self.log(f"Review fail: {e}")
