from abc import ABC, abstractmethod

from abstract_classes import UserManager
class Product:
    description = ""
    item = ""
    material = ""
    product = ""
    product_image = ""
    product_id = 0
    all_products = ""



class ProductAbstract(ABC):
    @abstractmethod
    def create_product(item, product:Product):
        pass

    @abstractmethod
    def edit_product(item):
        pass

    @abstractmethod
    def get_product_by_id(item, product_id):
        pass

    @abstractmethod
    def get_all_products(item):
        pass

    @abstractmethod
    def upload_product_image(item, product_image):
        pass
    @abstractmethod
    def delete_product(item):
        pass

    @abstractmethod
    def get_all_products(item, all_products):
        pass

class ProductManager(ProductAbstract):
 
    
   def create_product(item, product:Product):
        print("product information")

   def edit_product(item):
        print("product description")

   def get_product_by_id(item, product_id):
        print("Id codes")

   def get_all_products(item, all_products):
        print("All products listed here")
        
   def upload_product_image(item, product_image):
       print("product images")

   def delete_product(item):
       print ("image deleted")


product_manager = ProductManager()
product = Product()
product.product = "Dress"
product.product_id = 78256
product.description = "Long black dress"
product.material = "Cotton"

product_manager = ProductManager()
product_manager.create_user(product)
product_manager.edit_product("Change description")



