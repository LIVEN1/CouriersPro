from CouriersPro.Commands.ICommand import ICommand
from CouriersPro.Company.Company import Company

cmd = "AddCourier"
company = Company


class AddCourierCommand(ICommand):
    def execute_command(command):
        if (command == cmd):
            print("Введите количество курьеров")
            count_of_couriers = input()
            company.start_program(count_of_couriers)


    @staticmethod
    def get_command_name():
        return cmd
