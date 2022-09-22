#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number *= -1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'

    return [letter + suffixe for letter in prefixes]


def prime_integer_summation() -> int:
    list_nombre_premier = [2, 3, 5]
    nombre = 6

    while len(list_nombre_premier) < 100:
        is_nombre_premier = True
        for nombre_premier in list_nombre_premier:
            if nombre % nombre_premier == 0:
                is_nombre_premier = False
                break

        if is_nombre_premier:
            list_nombre_premier.append(nombre)
        nombre += 1

    somme = sum(list_nombre_premier)
    return somme


def factorial(number: int) -> int:
    factorielle = 1
    for i in range(number):
        factorielle *= (i+1)
    return factorielle


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    list_dacceptation = []
    for group in groups:
        acceptable = True
        if len(group) > 10 or len(group) <= 3:
            acceptable = False
        else:
            if 25 in group:
                pass
            else:
                for age in group:
                    if age < 18 or (age > 70 and 50 in group):
                        acceptable = False
                        break

        list_dacceptation.append(acceptable)

    return list_dacceptation


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
