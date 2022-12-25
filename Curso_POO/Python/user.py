from account import Account
class User(Account):
    def __init__(name, document):
        super().__init__(name, document)