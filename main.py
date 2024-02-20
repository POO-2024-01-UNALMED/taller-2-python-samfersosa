class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, newregistro):
        self.registro = newregistro
        
    def asignarTipo(self, newtipo):
        if newtipo == "electrico" or newtipo == "gasolina":
            self.tipo = newtipo

class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, newcolor):
        if newcolor in ["blanco", "negro", "verde", "rojo", "amarillo"]:
            self.color = newcolor

class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados

    def cantidadAsientos(self):
        return len(self.asientos)
    
    def verificarIntegridad(self, motor):
        registroAuto = self.registro
        registroMotor = motor.registro
        asientosOriginales = all(asiento.registro == registroAuto for asiento in self.asientos)

        if registroAuto == registroMotor and asientosOriginales:
            return "Auto original"
        else:
            return "Las piezas no son originales"
print(auto.verificarIntegridad(motor)) 