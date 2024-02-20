class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, newcolor):
        if (newcolor == "blanco" or newcolor == "negro" or newcolor == "verde" or newcolor == "rojo" or newcolor == "amarillo"):
           self.color == newcolor

class Auto:
    cantidadCreados=0
    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        

    def cantidadAsientos(self):
        contador = 0 
        for i in range(len(self.asientos)-1):
            if self.asientos[i]!=None:
                contador+=1
            else:
                pass
        return contador
        
    def verificarIntegridad(self,):
        if self.registro == self.motor.registro:
            for asiento in self.asientos:
                if(type(asiento)==Asiento):
                    if asiento.registro!=self.registro:
                        return "Las piezas no son originales"
            return "Auto original"  
        else:
            return "Las piezas no son originales"
        if registroAuto == registroMotor and asientosOriginales:
            return "Auto original"
        else:
            return "Las piezas no son originales"

class Motor:
    def init(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
        def cambiarRegistro(self, newregistro):
            self.registro = newregistro
        
        def asignarTipo(self, newtipo):
            if (newtipo == "electrico" or newtipo == "gasolina"):
              self.tipo=newtipo