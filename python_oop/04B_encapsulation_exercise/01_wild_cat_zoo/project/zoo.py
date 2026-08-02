from project.animal import Animal
from project.worker import Worker

class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price: float) -> str:
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        worker = next((p for p in self.workers if p.name == worker_name), None)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salaries = sum(worker.salary for worker in self.workers)
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_animal_care_money = sum(a.money_for_care for a in self.animals)
        if self.__budget >= total_animal_care_money:
            self.__budget -= total_animal_care_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self):
        return self.__print_status(self.animals, "Lion", "Tiger", "Cheetah")

    def workers_status(self):
        return self.__print_status(self.workers, "Keeper", "Caretaker", "Vet")

    def __print_status(self, category_list: list[Animal | Worker], *args):
        elements = {arg: [] for arg in args}  # {"Lion"}: [], ...}
        for item in category_list:
            elements[item.__class__.__name__].append(repr(item))
        result = [f"You have {len(category_list)} {str(category_list[0].__class__.__bases__[0].__name__).lower()}s"]
        for key, value  in elements.items():
            result.append(f"----- {len(value)} {key}s:")
            result.extend(value)
        return "\n".join(result)

