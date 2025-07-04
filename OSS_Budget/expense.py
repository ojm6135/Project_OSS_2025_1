
class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        if self.date is not None:
            return f"[{self.date}] {self.category} - {self.description}: {self.amount}원"
        return f"{self.category} - {self.description}: {self.amount}원"  # 고정 지출