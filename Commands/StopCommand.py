from CouriersPro.Commands.ICommand import ICommand

cmd = "Stop"


class StopCommand(ICommand):
    def execute_command(self):
        if self == cmd:
            exit()

    @staticmethod
    def get_command_name():
        return cmd