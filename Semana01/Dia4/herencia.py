
class Empresa:
    def __init__(self,ruc,rz,tel):
        self.ruc =ruc
        self.razonsocial = rz
        self.telefono = tel
        
    def mostrar(self):
        print("Ruc : ",self.ruc, " - ",self.razonsocial)
        
class Cliente (Empresa):
    def __init__(self,ruc,rz,tel,credito):
        super().__init__(ruc,rz,tel)
        self.credito = 1000
    
    def mostrar(self):
        print("Ruc: ",self.ruc, "linea de credito1", self.credito)
        
class Proveedor(Empresa):
    def __init__(self,ruc,rz,tel,cal):
        super().__init__(ruc,rz,tel)
        self.calificacion=cal
        
pepitoEirl = Cliente('123456789','Pepito Eirl','1234567',1000)
pepitoEirl.mostrar()