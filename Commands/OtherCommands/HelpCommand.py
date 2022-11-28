from CouriersPro.Commands.CompanyCommands.AddCourier import AddCourierCommand
from CouriersPro.Commands.CompanyCommands.AddOrder import AddOrder
from CouriersPro.Commands.OtherCommands.DebugCommand import DebugCommand
from CouriersPro.Commands.CompanyCommands.DestroyOrder import DestroyOrder
from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Commands.OtherCommands.StopCommand import StopCommand
from CouriersPro.Commands.CompanyCommands.DestroyCourier import DestroyCourier

cmd = "Help"


class HelpCommand(ICommand):
    def execute_command(self, command):
        if cmd == command:
            print(cmd, StopCommand.get_command_name(), AddOrder.get_command_name(), DebugCommand.get_command_name(),
                  DestroyOrder.get_command_name(), AddCourierCommand.get_command_name(), DestroyCourier.get_command_name())

    @staticmethod
    def get_command_name():
        return cmd
