class Personaje:
    def __init__(self, id, nombre, nano, vuela) -> None:
        self.id = id
        self.nombre = nombre
        self.usa_nanotecnologia = nano
        self.puede_volar = vuela

    def retornar_descripcion(self):
        descripcion = f"{self.id} - {self.nombre} - {self.usa_nanotecnologia} - {self.puede_volar}"
        return descripcion