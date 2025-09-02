from adoptante import Adoptante

class AdoptanteNovato(Adoptante):
    # solo 1 mascota total
    def puede_adoptar(self, mascota):
        return len(self.mascotas) < 1
