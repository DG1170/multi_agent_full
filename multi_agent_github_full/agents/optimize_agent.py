from .base import BaseAgent

class OptimizeAgent(BaseAgent):
    def handle(self, msg):
        code = msg["code"]
        opt = code.replace("def solution(x):","def solution(x:int)->int:")
        self.log("Optimized")
        print("\n=== FINAL CODE ===\n", opt)
