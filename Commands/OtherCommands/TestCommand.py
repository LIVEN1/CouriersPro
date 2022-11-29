from CouriersPro.Commands.CompanyCommands.ICommand import ICommand

cmd = "Test"


class TestCommand(ICommand):
    def execute_command(self, command):
        if cmd == command:
            print("123")
            return

    @staticmethod
    def get_command_name():
        return cmd