# -*- coding: utf-8 -*-

import timeit
import matplotlib.pyplot as plt


def timeit_and_plot():
    timeit_sizes = [1, 5, 10, 20, 30]
    timeit_sizes += range(50, 2000, 50)
    timeit_repeat = [1]

    timings_for_verfication = [
        timeit.timeit(
            'verification(sol, prop)',
            setup='from mastermind import verification, tirage_aleatoire; sol = tirage_aleatoire(%d, %d); prop = tirage_aleatoire(%d, %d)' % (size, size, size, size),
            number=repeat)
        for size in timeit_sizes for repeat in timeit_repeat
    ]

    plt.title("Temps de calcul de la méthode verification()")
    plt.ylabel('Temps en secondes')
    plt.xlabel('Nb points/couleurs')
    plt.plot(timeit_sizes, timings_for_verfication, '-ro', label='Verification iteratif')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    timeit_and_plot()