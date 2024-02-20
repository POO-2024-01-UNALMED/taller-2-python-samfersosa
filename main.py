class Asiento:
    def _init_(self, color, precio, registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor(self, color:str):
        if color=="rojo" or color =="verde" or color=="amarillo" or color=="negro" or color=="blanco":
            self.color=color

class Auto:
    cantidadCreados=0
    def _init_(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro

    def cantidadAsientos(self):
        contador=0
        for asiento in self.asientos:
            if (type(asiento)==Asiento):
                contador+=1
            else:
                pass
        return contador
    
    def verificarIntegridad(self):
        if self.registro==self.motor.registro:
            for asiento in self.asientos:
                if (type(asiento)==Asiento):
                    if asiento.registro!=self.registro:
                        return "Las piezas no son originales"
            return "Auto original" 
        else:
            return "Las piezas no son originales"
    
            
class Motor:
    def _init_(self, numeroCilindros, tipo, registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    def cambiarRegistro(self, int):
        self.registro=int
    def asignarTipo(self, String):
        if String=="electrico" or String== "gasolina":
            self.tipo=String