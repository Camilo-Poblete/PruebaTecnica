class Rele:
    def __init__(self, estado=False):
        self.estado = estado

    def activar(self):
       self.estado = True
       
    def desactivar(self):
        self.estado = False    


def obtener_estado(self):
    return self.estado



def circuito(rele1, rele2):
    # El circuito se activa si cualquiera de los relés se activa (conexión en paralelo)
    if rele1.obtener_estado() or rele2.obtener_estado():
        return "El circuito está activado."
    else:
        return "El circuito está desactivado."


# Crear dos relés
rele1 = Rele()  
rele2 = Rele()  

# Verificar estado inicial del circuito
print(circuito(rele1, rele2))  # El circuito debería estar desactivado

# Activar el relé 1
rele1.activar()
print(circuito(rele1, rele2))  # El circuito debería estar activado

# Desactivar el relé 1 y activar el relé 2
rele1.desactivar()
rele2.activar()
print(circuito(rele1, rele2))  

# Desactivar ambos relés
rele1.desactivar()
rele2.desactivar()
print(circuito(rele1, rele2))  
