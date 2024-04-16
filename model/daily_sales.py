from dataclasses import dataclass
from datetime import date


@dataclass
class DailySale:
    Retailer_code: int
    Product_number: int
    Order_method_code: int
    Date: date
    Quantity: int
    Unit_price: float
    Unit_sale_price: float

    def __str__(self):
        return f'{self.Product_number} venduto il {self.Date} da {self.Retailer_code}'
