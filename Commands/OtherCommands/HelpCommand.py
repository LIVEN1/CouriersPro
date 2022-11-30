from CouriersPro.Commands.CompanyCommands.Courier.AddCourier import AddCourierCommand
from CouriersPro.Commands.CompanyCommands.Order.AddOrder import AddOrder
from CouriersPro.Commands.CompanyCommands.Order.DestroyOrder import DestroyOrder
from CouriersPro.Commands.CompanyCommands.ICommand import ICommand
from CouriersPro.Commands.OtherCommands.StopCommand import StopCommand
from CouriersPro.Commands.CompanyCommands.Courier.DestroyCourier import DestroyCourier
from CouriersPro.Commands.CompanyCommands.Courier.CourierStatsCommand import CourierStatsCommand

cmd = "Help"


class HelpCommand(ICommand):
    def execute_command(self, command):
        if cmd.casefold() == command.casefold():
            print(cmd + ", " + StopCommand.get_command_name() + ", " + AddOrder.get_command_name() + ", " +
                  DestroyOrder.get_command_name() + ", " + AddCourierCommand.get_command_name() + ", " + DestroyCourier.get_command_name() + ", " + CourierStatsCommand.get_command_name())
            return

    @staticmethod
    def get_command_name():
        return cmd
