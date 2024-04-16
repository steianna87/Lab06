from database.DB_connect import DBConnect
from model.daily_sales import DailySale
from model.products import Product
from model.retailers import Retail


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_daily_sales():
        connessione = DBConnect.get_connection()
        cursore = connessione.cursor(dictionary=True)

        query = '''select *
                        from go_daily_sales'''

        cursore.execute(query)
        risultato = []
        for row in cursore:
            risultato.append(DailySale(row['Retailer_code'],
                                       row['Product_number'],
                                       row['Order_method_code'],
                                       row['Date'],
                                       row['Quantity'],
                                       row['Unit_price'],
                                       row['Unit_sale_price']))
        cursore.close()
        connessione.close()
        return risultato

    @staticmethod
    def get_products():
        connessione = DBConnect.get_connection()
        cursore = connessione.cursor(dictionary=True)

        query = '''select *
                from go_products'''

        cursore.execute(query)
        risultato = []
        for row in cursore:
            risultato.append(Product(row['Product_number'],
                                     row['Product_line'],
                                     row['Product_type'],
                                     row['Product'],
                                     row['Product_brand'],
                                     row['Product_color'],
                                     row['Unit_cost'],
                                     row['Unit_price']))
        cursore.close()
        connessione.close()
        return risultato

    @staticmethod
    def get_retailers():
        connessione = DBConnect.get_connection()
        cursore = connessione.cursor(dictionary=True)

        query = '''select *
                    from go_retailers'''

        cursore.execute(query)
        risultato = []
        for row in cursore:
            risultato.append(Retail(row['Retailer_code'],
                                    row['Retailer_name'],
                                    row['Type'],
                                    row['Country']))
        cursore.close()
        connessione.close()
        return risultato
