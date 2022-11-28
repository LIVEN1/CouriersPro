from CouriersPro.Commands.ICommand import ICommand

cmd = "Test"


class TestCommand(ICommand):
    def execute_command(self):
        if cmd == self:
            print("123")

    def get_command_name(self):
        return cmd