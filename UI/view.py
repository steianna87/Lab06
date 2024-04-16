import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

        self.retailer = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        '''self.txt_name = ft.TextField(
            label="name",
            width=200,
            hint_text="Insert a your name"
        )

        # button for the "hello" reply
        self.btn_hello = ft.ElevatedButton(text="Hello", on_click=self._controller.handle_hello)
        row1 = ft.Row([self.txt_name, self.btn_hello],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        '''
        # ROW 1
        self.seleziona_anno = ft.Dropdown(label='anno', options=[ft.dropdown.Option('Nessun filtro')])
        self.popola_anni()
        self.seleziona_brand = ft.Dropdown(label='brand', options=[ft.dropdown.Option('Nessun filtro')])
        self.popola_brand()
        self.seleziona_retailer = ft.Dropdown(label='retailer', options=[ft.dropdown.Option('Nessun filtro')])
        self.popola_retailers()
        row1 = ft.Row([self.seleziona_anno, self.seleziona_brand, self.seleziona_retailer], alignment=ft.MainAxisAlignment.CENTER)

        # ROW 2
        self.btn_top_vendite = ft.ElevatedButton(text='Top vendite', on_click=self.controller.get_top_vendite)
        self.btn_analizza_vendite = ft.ElevatedButton(text='Analizza vendite')
        row2 = ft.Row([self.btn_top_vendite, self.btn_analizza_vendite], alignment=ft.MainAxisAlignment.CENTER)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        # Aggiungi le righe
        self._page.add(row1, row2, self.txt_result)

        '''# List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()'''

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def popola_anni(self):
        anni = self.controller._model.years
        for anno in anni:
            self.seleziona_anno.options.append(ft.dropdown.Option(anno))
        self.update_page()

    def popola_brand(self):
        brands = self.controller._model.brands
        for brand in brands:
            self.seleziona_brand.options.append(ft.dropdown.Option(brand))
        self.update_page()

    def read_retailer(self, e):
        self.retailer = e.control.data


    def popola_retailers(self):
        retailers = self.controller._model.retailers
        for retailer in retailers:
            self.seleziona_retailer.options.append(ft.dropdown.Option(key=retailer.Retailer_code,
                                                                      text=retailer.Retailer_name,
                                                                      data=retailer,
                                                                      on_click=self.read_retailer))
        self.update_page()
