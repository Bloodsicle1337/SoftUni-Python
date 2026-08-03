from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    def add_customer(self, customer: Customer):
        self.__add_object(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.__add_object(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.__add_object(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__add_object(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.__add_object(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):
        subscription = self.__find_object(subscription_id, self.subscriptions)
        customer = self.__find_object(subscription.customer_id, self.customers)
        trainer = self.__find_object(subscription.trainer_id, self.trainers)
        plan = self.__find_object(subscription.exercise_id, self.plans)
        equipment = self.__find_object(plan.equipment_id, self.equipment)

        return "\n".join([
            str(subscription),
            str(customer),
            str(trainer),
            str(equipment),
            str(plan)
        ])

    @staticmethod
    def __add_object(obj, collection):
        if obj not in collection:
            collection.append(obj)

    @staticmethod
    def __find_object(obj_id, collection):
        return next((o for o in collection if o.id == obj_id), None)