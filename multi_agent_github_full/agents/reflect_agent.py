from .base import BaseAgent

class ReflectAgent(BaseAgent):
    def handle(self, msg):
        print("\n=== REFLECTION ===")
        for h in self.memory.history():
            print(h)
