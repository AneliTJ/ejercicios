from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Maestro(Usuario):
    rfc: str
    sueldo: float

    def __init__(self, numero_control:str, nombre:str, apellido:str, rfc:str, sueldo:float,ano_nacimiento:int, contrasena:str):
        super(). __init__ (
            numero_control=numero_control, 
            nombre=nombre, 
            apellido=apellido, 
            contrasena=contrasena, 
            rol=Rol.MAESTRO)
        self.rfc=rfc
        self.sueldo=sueldo
        self.ano_nacimiento= ano_nacimiento

    def mostrar_info_maestro(self):
        nombre_completo= f"{self.nombre} {self.apellido}"
        print(f"Numero de control: {self.numero_control}, Nombre completo: {nombre_completo}, RFC: {self.rfc}, Sueldo: {self.sueldo}, Año de nacimiento: {self.ano_nacimiento}")