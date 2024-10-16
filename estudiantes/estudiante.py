from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol


class Estudiante(Usuario):  #se ocupa poner entre los parentesis cual es la clase padre
    curp: str
    fecha_nacimiento: datetime
    

    def __init__(self, numero_control:str, nombre: str, apellido: str, curp:str, fecha_nacimiento: datetime,contrasena: str):
        super(). __init__(
            numero_control=numero_control, 
            nombre=nombre, 
            apellido=apellido, 
            contrasena=contrasena,
            rol= Rol.ESTUDIANTE

            )  #es para hacer las herencias de otra clase padre.
        self.curp=curp
        self.fecha_nacimiento=fecha_nacimiento

    def mostrar_info_estudiante(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info =f"Numero de control: {self.numero_control},nombre completo: {nombre_completo}, curp: {self.curp}, fecha de nacimiento: {self.fecha_nacimiento}, Rol: {self.rol.value}"
        return info
        
        
    
    