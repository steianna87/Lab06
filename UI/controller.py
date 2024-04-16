import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def filtra_parametri(self):
        self._model.daily_sales_filtrato = []
        self._model.products_filtrato = []
        self._model.retailers_filtrato = []

        filtro_anno = self._view.seleziona_anno.value
        filtro_brand = self._view.seleziona_brand.value
        filtro_retail = self._view.seleziona_retailer.value

        if filtro_anno == 'Nessun filtro':
            self._model.daily_sales_filtrato = self._model.daily_sales
        if filtro_brand == 'Nessun filtro':
            self._model.products_filtrato = self._model.products
        if filtro_retail == 'Nessun filtro':
            self._model.retailers_filtrato = self._model.retailers

        for vendita in self._model.daily_sales:
            if (vendita.Date.year == filtro_anno
                    and self._model.get_product_by_number(vendita.Product_number).Product_brand == filtro_brand
                    and vendita.Retailer_code == self._view.retailer.Retailer_code):
                self._model.daily_sales_filtrato.append(vendita)

        for prodotto in self._model.products:
            if prodotto.Product_brand == filtro_brand:
                self._model.products_filtrato.append(prodotto)

        for retailer in self._model.retailers:
            if retailer.Retailer_code == self._view.retailer.Retailer_code:
                self._model.retailers_filtrato.append(retailer)

    def get_top_vendite(self, e):
        self.filtra_parametri()
        for vendita in self._model.daily_sales_filtrato:
            self._view.txt_result.controls.append(ft.Text(vendita))
            print(vendita)
