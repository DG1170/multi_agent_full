from .base import BaseAgent

class DebugAgent(BaseAgent):
    def handle(self, msg):
        self.log("Debugging...")
        new_code = '''
def solution(x:int)->int:
    return int(x)*2
'''
        self.memory.set("code", new_code)
        self.bus.publish("code.generated", {"code": new_code})
