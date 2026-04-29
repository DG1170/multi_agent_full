from .base import BaseAgent

class CodeAgent(BaseAgent):
    def generate_code(self, task):
        return '''
def solution(x):
    return x * 2
'''

    def handle(self, msg):
        code = self.generate_code(msg["task"])
        self.memory.set("code", code)
        self.log("Generated")
        self.bus.publish("code.generated", {"code": code})
