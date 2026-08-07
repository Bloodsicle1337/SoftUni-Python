class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

    def __add__(self, other: "Person") -> "Person":
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: list[Person]) -> None:
        self.name = name
        self.people = people

    def __len__(self) -> int:
        return len(self.people)

    def __add__(self, other: "Group") -> "Group":
        new_name = f"{self.name} {other.name}"
        new_people = self.people + other.people

        return Group(new_name, new_people)

    def __str__(self) -> str:
        members = ", ".join(str(person) for person in self.people)

        return f"Group {self.name} with members {members}"

    def __getitem__(self, index: int) -> str:
        person = self.people[index]

        return f"Person {index}: {person}"