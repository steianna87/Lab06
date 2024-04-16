from database.DAO import DAO

class Model:
    def __init__(self):
        self.daily_sales = DAO.get_daily_sales()
        self.years = set()
        self.get_years()
        self.daily_sales_filtrato = []

        self.products = DAO.get_products()
        self.brands = set()
        self.get_brands()
        self.products_filtrato = []

        self.retailers = DAO.get_retailers()
        self.retailers_filtrato = []

    def get_years(self):
        for vendita in self.daily_sales:
            self.years.add(vendita.Date.year)


    def get_brands(self):
        for prodotto in self.products:
            self.brands.add(prodotto.Product_brand)

    def get_product_by_number(self, Product_number):
        for prodotto in self.products:
            if prodotto.Product_number == Product_number:
                return prodotto
