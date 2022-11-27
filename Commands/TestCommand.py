from CouriersPro.Commands.ICommand import ICommand

cmd = "test"


class TestCommand(ICommand):
    def execute_command(self):
        if cmd == self:
            print("123")