from django.shortcuts import render

# Create your views here.
class persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()

def index(request):
    hijo=persona("Juan Perez", "7")


    lista=["lasaña", "charquican", "porotos granados"]

    context={"hijo":hijo, "nombre":"Claudia Andrea", "comida":lista}

    return render(request, 'alumnos/index.html', context)
