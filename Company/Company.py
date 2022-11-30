class Company:
    __list_of_orders__ = []
    __list_of_couriers__ = []

    def add_order(self, order):
        self.__list_of_orders__.append(order)
        print(self.__list_of_orders__)

    def try_to_destroy_order(self, id):
        if int(id) <= len(self.__list_of_orders__):
            self.__list_of_orders__.pop(int(id) - 1)
            print(self.__list_of_orders__)
        else:
            print("Id Больше Максимального")

    def try_to_destroy_courier(self, id):
        if int(id) <= len(self.__list_of_couriers__):
            self.__list_of_couriers__.pop(int(id) - 1)
            print(self.__list_of_couriers__)
        else:
            print("Id Больше Максимального")

    def get_orders_count(self):
        return len(self.__list_of_orders__)

    def get_couriers_count(self):
        return len(self.__list_of_couriers__)

    def get_orders(self):
        return self.__list_of_orders__

    def get_couriers(self):
        return self.__list_of_couriers__

    def add_courier(self, courier):
        self.__list_of_couriers__.append(courier)
        print(self.__list_of_couriers__)

    def __init__(self):
        self.__list_of_orders = []
        self.__list_of_couriers__ = []
