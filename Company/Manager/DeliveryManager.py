from CouriersPro.Company.Company import Company


class DeliveryManager:

    def start_program(self):
        if company.get_orders_count() < 1 and company.get_couriers_count() < 1:
            print("Error")
            return
        self.check_weight(None, None, None)

    def check_distance(self, courier, best_weight_orders):
        if len(best_weight_orders) == 0:
            return
        best_orders = {}
        for order in best_weight_orders:
            result = (int(order.x_coord) - int(courier.x_coord)) ** 2 + (int(order.y_coord) - int(courier.y_coord)) ** 2
            best_orders[order] = result
        min_distance = min(best_orders.values())
        best_order = [key for key in best_orders if best_orders[key] == min_distance]
        courier.attach_order(best_order[0])
        company.try_to_destroy_order(best_order[0])
        best_weight_orders.remove(best_order[0])
        self.check_weight(courier, best_weight_orders, best_order[0])
        return

    def check_weight(self, delivery_boy, best_orders, previous_order):
        if delivery_boy is None and best_orders is None:
            orders = self.__company.get_orders()
            couriers = self.__company.get_couriers()
            for courier in couriers:
                best_weight_orders = []
                for order in orders:
                    if int(courier.maxWeight) >= int(order.weight):
                        best_weight_orders.append(order)
                self.check_distance(courier, best_weight_orders)
        else:
            best_weight_orders = []
            for order in best_orders:
                if int(delivery_boy.maxWeight) - int(previous_order.weight) > int(order.weight):
                    best_weight_orders.append(order)
            self.check_distance(delivery_boy, best_weight_orders)

    def __init__(self, company):
        self.__company = company
        print(True)


company = Company()
delivery_manager = DeliveryManager(company)
