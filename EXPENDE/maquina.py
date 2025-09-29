class MaquinaExpendedora:
    def __init__(self):
        self.bebidas = []
        self.recaudacion = 0

    def agregar_bebida(self, bebida):
        self.bebidas.append(bebida)

    def preparar_bebida(self, nombre_bebida):
        for bebida in self.bebidas:
            if bebida.nombre == nombre_bebida:
                print(f"Se preparó {bebida.nombre}")
                return bebida
        print("Bebida no disponible")
        return None

    def cobrar(self, bebida):
        if bebida:
            return bebida.calcular_precio()
        return 0

    def registrar_cobro(self, precio):
        self.recaudacion += precio

    def recaudacion_total(self):
        return self.recaudacion

    def bebida_mas_cara(self):
        mas_cara = None
        for bebida in self.bebidas:
            if mas_cara is None or bebida.calcular_precio() > mas_cara.calcular_precio():
                mas_cara = bebida
        return mas_cara
