class BaseAgent:
    def __init__(self, name, bus, memory):
        self.name = name
        self.bus = bus
        self.memory = memory

    def log(self, msg):
        print(f"[{self.name}] {msg}")
