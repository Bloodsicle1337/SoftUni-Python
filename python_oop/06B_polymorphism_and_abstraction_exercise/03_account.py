class Account:
    def __init__(self, owner: str, amount: int = 0) -> None:
        self.owner = owner
        self.amount = amount
        self._transactions = []

    @property
    def balance(self) -> int:
        return self.amount + sum(self._transactions)

    def handle_transaction(self, transaction_amount: int) -> str:
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")

        self._transactions.append(transaction_amount)

        return f"New balance: {self.balance}"

    def add_transaction(self, amount: int) -> str:
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        return self.handle_transaction(amount)

    def __str__(self) -> str:
        return (
            f"Account of {self.owner} "
            f"with starting amount: {self.amount}"
        )

    def __repr__(self) -> str:
        return f"Account({self.owner}, {self.amount})"

    def __len__(self) -> int:
        return len(self._transactions)

    def __getitem__(self, index: int) -> int:
        return self._transactions[index]

    def __iter__(self):
        return iter(self._transactions)

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other: "Account") -> bool:
        return self.balance > other.balance

    def __ge__(self, other: "Account") -> bool:
        return self.balance >= other.balance

    def __lt__(self, other: "Account") -> bool:
        return self.balance < other.balance

    def __le__(self, other: "Account") -> bool:
        return self.balance <= other.balance

    def __eq__(self, other: "Account") -> bool:
        return self.balance == other.balance

    def __ne__(self, other: "Account") -> bool:
        return self.balance != other.balance

    def __add__(self, other: "Account") -> "Account":
        new_owner = f"{self.owner}&{other.owner}"
        new_amount = self.amount + other.amount

        new_account = Account(new_owner, new_amount)
        new_account._transactions = (
            self._transactions + other._transactions
        )

        return new_account