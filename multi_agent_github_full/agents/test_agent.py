import subprocess, tempfile, os
from .base import BaseAgent

class TestAgent(BaseAgent):
    def handle(self, msg):
        code = msg["code"]
        test_code = code + '''
assert solution(2)==4
assert solution(5)==10
'''
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
            f.write(test_code.encode())
            fname = f.name
        try:
            r = subprocess.run(["python", fname], capture_output=True)
            if r.returncode==0:
                self.log("Test OK")
                self.bus.publish("test.passed", {"code": code})
            else:
                err = r.stderr.decode()
                self.log("Test fail")
                self.bus.publish("test.failed", {"error": err})
        finally:
            os.unlink(fname)
