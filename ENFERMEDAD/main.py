"""1. Hacer que una persona contraiga malaria y lupus,
y que dicha persona viva un día de su vida para que las enfermedades hagan su efecto.
2. Hacer que dicha malaria se atenúe en 5000 y el lupus en 500 
y preguntar si la persona está sana.
3. Hacer que la persona reciba una dosis de 300 ml de un medicamento las veces que haga falta hasta quedar sana.
4. Modelar una enfermedad que sea tanto infecciosa como autoinmune."""

from persona import Persona
from enfermedad import Enfermedad, Infeccion, Autoinmune, Mixta

if __name__ == "__main__":
    # Creo una persona con 0 días, 36°C y 3.000.000 de células
    persona = Persona(0, 36, 3_000_000)

    # Creo malaria (infección de 5000 células) y lupus (autoinmune de 10000 células)
    malaria = Infeccion(5000, "malaria")
    lupus = Autoinmune(10000, "lupus")

    # La persona contrae malaria y lupus
    persona.agregar_enfermedad(malaria)
    persona.agregar_enfermedad(lupus)

    # Estado inicial
    print("Estado inicial")
    print("Temperatura:", persona.mostrar_temperatura)
    print("Células buenas:", persona.mostrar_celulas_buenas)
    print("Malaria células:", malaria.mostrar_cant_celulas)
    print("Lupus células:", lupus.mostrar_cant_celulas)

    # La persona vive un día
    persona.vivir_un_dia()

    # Estado después de un día
    print("\n Después de un día")
    print("Temperatura:", persona.mostrar_temperatura)
    print("Células buenas:", persona.mostrar_celulas_buenas)
    print("Malaria células:", malaria.mostrar_cant_celulas)
    print("Lupus células:", lupus.mostrar_cant_celulas)
