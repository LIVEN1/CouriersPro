from CouriersPro.Commands.ICommand import ICommand

cmd = "Test"


class TestCommand(ICommand):
    def execute_command(self):
        if cmd == self:
            print("123")

    @staticmethod
    def get_command_name():
        return cmd