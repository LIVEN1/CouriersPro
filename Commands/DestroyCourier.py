from CouriersPro.Commands.ICommand import ICommand
from CouriersPro.Courier.CourierManager import CourierManager

cmd = "DestroyCourier"

class DestroyCourier(ICommand):
    def execute_command(command):
        if command == cmd:
            CourierManager.destroy_courier()

    @staticmethod
    def get_command_name():
        return cmd