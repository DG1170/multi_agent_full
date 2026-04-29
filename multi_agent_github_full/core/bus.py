class MessageBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, topic, handler):
        self.subscribers.setdefault(topic, []).append(handler)

    def publish(self, topic, message):
        for h in self.subscribers.get(topic, []):
            h(message)
