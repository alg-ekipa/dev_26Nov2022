
stolovi_rjecnik = {
    '0186': ['stol Jack', 700.00, True, 'smeđa', 'drvo', 4],
    '0203': ['stol Kathy', 880.00, True, 'smeđa', 'staklo', 3],
    '1234': ['stol Tomy', 1250.00, True, 'bijela', 'staklo', 4],
    '4002': ['stol Ohm', 940.00, True, 'crna', 'metal', 1],
    '0923': ['stol Heda', 940.00, False, 'crna', 'drvo', 1],
    '1773': ['stol Lucas', 940.00, True, 'crna', 'drvo', 4]
}

svjetiljka_rjecnik = {
    '0001': ['svjetiljka Zadar', 1200.00, True, 'zlatna', 'zlato', 'zarulja'],
    '0002': ['svjetiljka Zagreb', 2800.00, True, 'plava', 'staklo', 'zarulja'],
    '0003': ['svjetiljka Dubrava', 800.00, False, 'zelena', 'srebro', 'bez'],
    '0004': ['svjetiljka Rijeka', 400.00, False, 'roza', 'zlato', 'bez'],
    '0005': ['svjetiljka Dubrovnik', 5400.00, True, 'magenta', 'platina', 'zarulja'],
    '0006': ['svjetiljka Madrid', 55950.00, True, 'crvena', 'platina', 'bez']
}

tepisi_rjecnik = {
    '0007': ['tepih Melita', 8000.00, True, 'zlatna', 'pamuk', 'okrugao'],
    '0008': ['tepih Lana', 7200.00, True, 'plava', 'svila', 'pravokutni'],
    '0009': ['tepih Sanja', 480.00, False, 'zelena', 'pamuk', 'okrugao'],
    '0010': ['tepih Emina', 525.00, False, 'roza', 'plastika', 'pravokutni'],
    '0011': ['tepih Laura', 320.00, True, 'magenta', 'plastika', 'okrugao'],
    '0012': ['tepih Tea', 12524.00, True, 'crvena', 'svila', 'pravokutni']
}


class Product:
    def __init__(self, code: str, name: str, price: float, available: bool, color: str, material: str):
        self.code = code
        self.name = name
        self.price = price
        self.available = available
        self.color = color
        self.material = material

    @property
    def is_affordable(self) -> bool:
        return self.price < 1000

    @property
    def is_available(self) -> bool:
        return self.available

    def __str__(self) -> str:
        return f'{self.name} ({self.code})'


class Table(Product):
    def __init__(self, code: str, name: str, price: float, available: bool, color: str, material: str, legs: int):
        super().__init__(code, name, price, available, color, material)
        self.legs = legs

    def __str__(self) -> str:
        return f'{super().__str__()}, {self.color}, {self.material}, {self.legs} legs'


class Lamp(Product):
    def __init__(self, code: str, name: str, price: float, available: bool, color: str, material: str, bulb: str):
        super().__init__(code, name, price, available, color, material)
        self.bulb = bulb

    @property
    def has_bulb(self) -> bool:
        return self.bulb == 'zarulja'

    def __str__(self) -> str:
        return f'{super().__str__()}, {self.color}, {self.material}, bulb: {self.bulb}'


class Carpet(Product):
    def __init__(self, code: str, name: str, price: float, available: bool, color: str, material: str, shape: str):
        super().__init__(code, name, price, available, color, material)
        self.shape = shape

    def __str__(self) -> str:
        return f'{super().__str__()}, {self.color}, {self.material}, {self.shape} shape'



    