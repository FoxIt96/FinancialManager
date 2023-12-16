class Transaction:
    def __init__(self, description, amount, category_id):
        self.description = description
        self.amount = amount
        self.category_id = category_id

class Category:
    def __init__(self, name):
        self.name = name
