from abc import ABC, abstractmethod

class BaseGuildHall(ABC):
    def __init__(self, alias: str):
        self.alias = alias
        self.members = []

    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, value):
        stripped_value = value.strip()

        if len(stripped_value) < 2:
            raise ValueError("Guild hall alias is invalid!")

        if not all(char.isalpha() or char.isspace() for char in value):
            raise ValueError("Guild hall alias is invalid!")

        self.__alias = value

    @property
    @abstractmethod
    def max_member_count(self):
        pass

    def calculate_total_gold(self):
        return sum(member.gold for member in self.members)

    def status(self):
        if self.members:
            tags = sorted(member.tag for member in self.members)
            members_info = " *".join(tags)
        else:
            members_info = "N/A"

        total_gold = self.calculate_total_gold()

        return (
            f"Guild hall: {self.alias}; "
            f"Members: {members_info}; "
            f"Total gold: {total_gold}"
        )

    @abstractmethod
    def increase_gold(self, min_skill_level_value: int):
        pass





































