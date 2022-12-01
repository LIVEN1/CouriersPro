from CouriersPro.Commands.CompanyCommands.Courier.AddCourier import AddCourier
from CouriersPro.Commands.CompanyCommands.Order.AddOrder import AddOrder
from CouriersPro.Commands.ICommand import ICommand
from CouriersPro.Commands.OtherCommands.StopCommand import StopCommand
from CouriersPro.Commands.CompanyCommands.Courier.GetCourierInfo import GetCourierInfo
from CouriersPro.Commands.CompanyCommands.Order.OrderStatsCommand import GetOrderInfo
from CouriersPro.Commands.CompanyCommands.Run import StartProgram

cmd = "Help"


class HelpCommand(ICommand):
    def execute_command(self, command):
        if cmd.casefold() == command.casefold():
            print(cmd + ", " + StopCommand.get_command_name() + ", " + AddOrder.get_command_name() + ", " + AddCourier.get_command_name() +
                  ", " + GetCourierInfo.get_command_name() + ", " + GetOrderInfo.get_command_name() + ", " + StartProgram.get_command_name())
            return

    @staticmethod
    def get_command_name():
        return cmd
