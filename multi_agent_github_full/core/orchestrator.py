from core.bus import MessageBus
from core.memory import SharedMemory

from agents.code_agent import CodeAgent
from agents.review_agent import ReviewAgent
from agents.test_agent import TestAgent
from agents.debug_agent import DebugAgent
from agents.optimize_agent import OptimizeAgent
from agents.reflect_agent import ReflectAgent

class Orchestrator:
    def __init__(self):
        self.bus = MessageBus()
        self.memory = SharedMemory()

        self.code = CodeAgent("CodeAgent", self.bus, self.memory)
        self.review = ReviewAgent("ReviewAgent", self.bus, self.memory)
        self.test = TestAgent("TestAgent", self.bus, self.memory)
        self.debug = DebugAgent("DebugAgent", self.bus, self.memory)
        self.optimize = OptimizeAgent("OptimizeAgent", self.bus, self.memory)
        self.reflect = ReflectAgent("ReflectAgent", self.bus, self.memory)

        self.max_retry = 3
        self.retry = 0

        self._register()

    def _register(self):
        self.bus.subscribe("task.start", self.code.handle)
        self.bus.subscribe("code.generated", self.review.handle)
        self.bus.subscribe("review.passed", self.test.handle)
        self.bus.subscribe("test.passed", self.optimize.handle)
        self.bus.subscribe("test.passed", self.reflect.handle)
        self.bus.subscribe("test.failed", self.on_fail)

    def on_fail(self, msg):
        self.retry += 1
        if self.retry > self.max_retry:
            print("❌ Max retries reached")
            return
        self.debug.handle(msg)

    def run(self, task):
        self.bus.publish("task.start", {"task": task})
