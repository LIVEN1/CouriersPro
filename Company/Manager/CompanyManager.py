from CouriersPro.Company.Company import Company


class CompanyManager:
    __company = 0

    def start_program(self):
        self.check_weight()

    def check_distance(self, courier, best_weight_orders):
        if len(best_weight_orders) == 0:
            return
        best_orders = {}
        for order in best_weight_orders:
            result = (order.x_coord - courier.x_coord) ** 2 + (order.y_coord - courier.y_coord) ** 2
            best_orders[order] = result
        print(best_orders)
        min_distance = min(best_orders.values())
        best_order = [key for key in best_orders if best_orders[key] == min_distance]
        courier.attach_order(best_order)
        return

    def check_weight(self):
        orders = self.__company.get_orders()
        couriers = self.__company.get_couriers()
        for courier in couriers:
            best_weight_orders = []
            for order in orders:
                if courier.maxWeight >= order.weight:
                    best_weight_orders.append(order)
            self.check_distance(courier, best_weight_orders)

    def __init__(self, company):
        self.__company = company
        print(True)


company = Company()
company_manager = CompanyManager(company)
