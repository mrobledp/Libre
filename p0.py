import datetime
print("Son las", datetime.datetime.now())

print("Este código se ejecuta desde el módulo P0")

import subprocess

try:
    # Execute the .exe file
    result = subprocess.run(['./hola.exe'], check=True, capture_output=True, text=True)
    
    var = result.stdout

    # Output the result
    print("Output:", result.stdout)
    print("Error:", result.stderr)
except subprocess.CalledProcessError as e:
    print("An error occurred:", e)

class li:
    def __init__(self, valor):
        self._ = valor
    
    def __str__(self):
        var = chr(ord(self._[:1])+1)+self._[1:]
        return var

# Uso de la clase
variable = li(var)
