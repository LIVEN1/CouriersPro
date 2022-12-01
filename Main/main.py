from CouriersPro.Commands.CompanyCommands.Run import StartProgram
from CouriersPro.Commands.CompanyCommands.Courier.AddCourier import AddCourier
from CouriersPro.Commands.CompanyCommands.Order.AddOrder import AddOrder
from CouriersPro.Commands.OtherCommands.DebugCommand import DebugCommand
from CouriersPro.Commands.OtherCommands.HelpCommand import HelpCommand
from CouriersPro.Commands.OtherCommands.StopCommand import StopCommand
from CouriersPro.Commands.OtherCommands.TestCommand import TestCommand
from CouriersPro.InputManager.InputManager import InputManager
from CouriersPro.Tests.CreateCouriers import CourierCreator
from CouriersPro.Tests.CreateOrders import OrderCreator
from CouriersPro.Commands.CompanyCommands.Courier.GetCourierInfo import GetCourierInfo
from CouriersPro.Commands.CompanyCommands.Order.OrderStatsCommand import GetOrderInfo

list_of_commands = [DebugCommand, AddCourier, TestCommand, HelpCommand, StopCommand, AddOrder,
                    StartProgram, OrderCreator, CourierCreator, GetCourierInfo, GetOrderInfo]


def find_command():
    for command in list_of_commands:
        command.execute_command(command, inputUser)


while True:
    inputUser = InputManager.get_input()
    find_command()
