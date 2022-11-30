from CouriersPro.Commands.CompanyCommands.Run import StartProgram
from CouriersPro.Commands.CompanyCommands.Courier.AddCourier import AddCourierCommand
from CouriersPro.Commands.CompanyCommands.Order.AddOrder import AddOrder
from CouriersPro.Commands.OtherCommands.DebugCommand import DebugCommand
from CouriersPro.Commands.CompanyCommands.Order.DestroyOrder import DestroyOrder
from CouriersPro.Commands.OtherCommands.HelpCommand import HelpCommand
from CouriersPro.Commands.OtherCommands.StopCommand import StopCommand
from CouriersPro.Commands.OtherCommands.TestCommand import TestCommand
from CouriersPro.Commands.CompanyCommands.Courier.DestroyCourier import DestroyCourier
from CouriersPro.InputManager.InputManager import InputManager
from CouriersPro.Tests.CreateCouriers import CourierCreator
from CouriersPro.Tests.CreateOrders import OrderCreator
from CouriersPro.Commands.CompanyCommands.Courier.CourierStatsCommand import CourierStatsCommand


ListOfCommands = [DebugCommand, AddCourierCommand, TestCommand, HelpCommand, StopCommand, DestroyOrder, AddOrder,
                  DestroyCourier, StartProgram, OrderCreator, CourierCreator, CourierStatsCommand]


def find_command():
    for command in ListOfCommands:
        command.execute_command(command, inputUser)


while True:
    inputUser = InputManager.get_input()
    find_command()
