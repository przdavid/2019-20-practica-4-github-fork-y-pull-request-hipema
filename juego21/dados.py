"""
Ejemplo de herencia en POO. Clases DadoSimple, DadoTrucado, DadoPoker, DadoPokerTrucado que heredarán de Dado.
Autor: Rafael del Castillo.
"""
from github.juego21.dado import Dado


class DadoSimple(Dado):
    """
    Simulará un dado normal con las caras del 1 al 6.
    """

    def __init__(self):
        super().__init__(1, 2, 3, 4, 5, 6)

if __name__ == "__main__":
    # Probamos dado simple
    d = DadoSimple()
    print("Tiramos dado simple 1000 veces con estos resultados:")
    tiradas = [d.tirada() for i in range(1000)]
    for i in d.caras:
        print(f"{i} ha salido {tiradas.count(i)} veces")

    # Probamos dado simple trucado
    d = DadoSimpleTrucado()
    print("\nTiramos dado simple trucado 1000 veces con estos resultados:")
    tiradas = [d.tirada() for i in range(1000)]
    for i in d.caras:
        print(f"{i} ha salido {tiradas.count(i)} veces")

    # Probamos dado póquer
    d = DadoPoker()
    print("\nTiramos dado de póquer 1000 veces con estos resultados:")
    tiradas = [d.tirada() for i in range(1000)]
    for i in d.caras:
        print(f"{i} ha salido {tiradas.count(i)} veces")

    # Probamos dado póquer trucado con doble probabilidad para el As
    d = DadoPokerTrucado()
    print("\nTiramos dado de póquer trucado con doble As 1000 veces con estos resultados:")
    tiradas = [d.tirada() for i in range(1000)]
    for i in d.caras:
        print(f"{i} ha salido {tiradas.count(i)} veces")

    # Probamos dado póquer trucado con triple probabilidad para el As
    d = DadoPokerTrucado(3)
    print("\nTiramos dado de póquer trucado con doble As 1000 veces con estos resultados:")
    tiradas = [d.tirada() for i in range(1000)]
    for i in d.caras:
        print(f"{i} ha salido {tiradas.count(i)} veces")