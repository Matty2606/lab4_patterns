from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    @abstractmethod
    def handle(self, request):
        pass

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            print("Handler A handled the request.")
        elif self.next_handler:
            self.next_handler.handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            print("Handler B handled the request.")
        elif self.next_handler:
            self.next_handler.handle(request)

if __name__ == "__main__":
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_a.set_next(handler_b)
    handler_a.handle("A")
    handler_a.handle("B")
