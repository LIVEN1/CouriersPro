from CouriersPro.Commands.ICommand import ICommand

cmd = "AddCourier"


class AddCourierCommand(ICommand):
    def execute_command(self):
        if (self == cmd):
            print("Courier has Added")

    def get_command_name(self):
        return cmd
