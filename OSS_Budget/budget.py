import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.counts = {}
        self.fixed_expenses = []

    def add_expense(self, category, description, amount):
        self.counts[category] = self.counts.get(category, 0) + 1
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")
        
    def add_fixed_expense(self, category, description, amount):
        fixed_expense = Expense(None, category, description, amount)
        self.fixed_expenses.append(fixed_expense)
        print("고정 지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()
        
        if not self.fixed_expenses:
            return
        print("(월 고정 지출)")
        for idx, e in enumerate(self.fixed_expenses, 1):
            print(f"{idx}. {e}")
        print()
        
    def list_expenses_by_freq(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[카테고리별 지출 빈도]")
        for ctg, freq in sorted(self.counts.items(), key=lambda x: x[1], reverse=True):
            print(f"{ctg} - {freq}회")
        print()
            
    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


