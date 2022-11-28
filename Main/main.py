from CouriersPro.Commands.AddCourier import AddCourierCommand
from CouriersPro.Commands.AddOrder import AddOrder
from CouriersPro.Commands.DebugCommand import DebugCommand
from CouriersPro.Commands.DestroyOrder import DestroyOrder
from CouriersPro.Commands.HelpCommand import HelpCommand
from CouriersPro.Commands.StopCommand import StopCommand
from CouriersPro.Commands.TestCommand import TestCommand


ListOfCommands = [DebugCommand, AddCourierCommand, TestCommand, HelpCommand, StopCommand, DestroyOrder, AddOrder]
a = 1





def find_command():
    for i in range(len(ListOfCommands)):
     ListOfCommands[i].execute_command(inputUser)


while a == 1:
    inputUser = input()
    find_command()
