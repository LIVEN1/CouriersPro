from CouriersPro.Company.Company import Company

order_query = []

dictionary = dict()


class CompanyManager(Company):
    def start_program(self):
        self.check_weight(CompanyManager)

    def check_distance(self, courier):
        orders = courier.get_best_orders_by_weight()
        if len(orders) == 0:
            return
        best_orders = {}
        for order in orders:
            result = (order.x_coord - courier.x_coord) ** 2 + (order.y_coord - courier.y_coord) ** 2
            best_orders[order] = result
        print(best_orders)
        min_distance = min(best_orders.values())
        best_order = [key for key in best_orders if best_orders[key] == min_distance]
        courier.attach_order(best_order)
        return

    def check_weight(self):
        orders = Company.get_orders()
        couriers = Company.get_couriers()
        for courier in couriers:
            for order in orders:
                if courier.maxWeight >= order.weight:
                    courier.attach_best_orders_by_weight(order)
            self.check_distance(self, courier)

