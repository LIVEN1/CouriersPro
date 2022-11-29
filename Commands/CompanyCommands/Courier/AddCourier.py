from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Courier.Manager.CourierManager import CourierManager

cmd = "AddCourier"


class AddCourierCommand(ICommand):
    def execute_command(self, command):
        if (command == cmd):
            CourierManager.add_courier()
            return


    @staticmethod
    def get_command_name():
        return cmd
