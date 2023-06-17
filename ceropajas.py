class Persona:
    def __init__ (self,nombre,apellido):
        self.nombre = nombre 
        self.apellido = apellido

    def hablar(self):
        return "hablando",+"hola"

    def caminar (self):
        return "caminando"

    def imprimirDatos(self):
        return f"Nombre: {self.nombre} {self.apellido}"


Persona = Persona("fg", "zerok")

mensajeHablar = Persona.hablar()
mensajeCaminar = Persona.caminar()
datosPersona = Persona.imprimirDatos()

print(mensajeHablar)
print(mensajeCaminar)
print(datosPersona)








