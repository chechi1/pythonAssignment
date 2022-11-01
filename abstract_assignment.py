from abc import ABC, abstractmethod
class Product:
    weight = ""
    material = ""
    price = ""

class ProductAbstract(ABC):
    @abstractmethod
    def create_product(item, product:Product):
        pass

    @abstractmethod
    def edit_product(item,):
        pass

    @abstractmethod
    def get_all_prodcut_by_id(item, product_id):
        pass

    @abstractmethod
    def get_all_product(item):
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

   def get_prodcut_by_id(item, product_id):
        print("Id codes")

   def get_all_products(item, all_products):
        print("All products")
        g
   def upload_product_image(item, product_image):
       print("product images")

   def delete_product(item):
       print ("image deleted")