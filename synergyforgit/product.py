#name
#category
#color
#release year
#engine capacity

class Product:
    __MAX_ID = 0
    
    def __init__(self, name: str,
                category: str,
                color: str,
                release_year: int,
                engine_capacity: bool):
        self.id = Product.__MAX_ID
        Product.__MAX_ID += 1
        #pol9 in class
        self.name = name
        self.category = category
        self.color = color
        self.release_year = release_year
        self.engine_capacity = engine_capacity




#products = [Product("Mazda", "car", "blue", 2019, 1.6)] + [Product("BMW", "car", "white", 2020, 2)] + [Product("Tyota", "car","cyan", 2022, 3.5)] + [Product("Mercedes", "car", "red", 2018, 2.6)] + [Product("Audi", "car", "black", 2015, 1.6)]

#print(*[
#    product.name 
#    for product in products
#    if len(product.name) > 5
#], sep="\n")