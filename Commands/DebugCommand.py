from CouriersPro.Commands.ICommand import ICommand

cmd = "Debug"


class DebugCommand(ICommand):
    def execute_command(command):
        if command == cmd:
            print("Debug on")

    @staticmethod
    def get_command_name():
        return cmd