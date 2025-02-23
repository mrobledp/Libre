class VariableNoImprimible:
    def __init__(self, valor):
        self._ = valor
    
    def __str__(self):
        var = self._[:1].upper()+self._[1:]
        return var

# Uso de la clase
variable = VariableNoImprimible("good")
print(variable)  # Salida: Valor no imprimible
print(variable._)

"""
#### Enfoque 2: Encriptación simple

import base64

class VariableEncriptada:
    def __init__(self, valor):
        # Codificamos el valor en base64
        self._valor_encriptado = base64.b64encode(valor.encode('utf-8')).decode('utf-8')
    
    def imprimir_valor(self):
        return "Valor no imprimible"

    def obtener_valor(self):
        # Decodificamos el valor en base64
        return base64.b64decode(self._valor_encriptado.encode('utf-8')).decode('utf-8')

# Uso de la clase
variable = VariableEncriptada("Este es un valor secreto")
print(variable.imprimir_valor())  # Salida: Valor no imprimible
print(variable.obtener_valor())  # Salida: Este es un valor secreto
"""