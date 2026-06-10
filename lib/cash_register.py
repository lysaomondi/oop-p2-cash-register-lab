#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []   # ✅ MUST BE LIST

    # ---------------- DISCOUNT PROPERTY ----------------
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            self._discount = 0   # safe fallback

    # ---------------- ADD ITEM ----------------
    def add_item(self, item, price, quantity=1):
        self.items.extend([item] * quantity)

        transaction_total = price * quantity
        self.total += transaction_total

        # ✅ store FULL transaction (important for tests)
        self.previous_transactions.append(transaction_total)

    # ---------------- APPLY DISCOUNT ----------------
    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total * (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    # ---------------- VOID LAST TRANSACTION ----------------
    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last = self.previous_transactions.pop()
        self.total -= last