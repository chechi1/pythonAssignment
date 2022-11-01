from abc import ABC, abstractmethod
class User:
    first_name =""
    last_name = ""
    email = ""


class UserAbstract(ABC):
    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def get_all_users(self):
        pass

    def get_user_by_id(self, user_id):
        pass


class ProductAbstract(UserAbstract):
    product_name = ""
    weight = ""
    price = ""

class UserManager(UserAbstract):
    def create_user(self, user: User):
        print("user information")

    def get_all_users(self):
        print("hello Chechi! we are getting all users here")

    def get_user_by_id(self, user_id):
        print("hello world")

user_manager = UserManager()
user_manager.get_all_users()