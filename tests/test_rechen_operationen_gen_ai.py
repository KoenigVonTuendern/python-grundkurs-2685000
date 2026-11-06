import pytest

from aufgaben_package.rechen_operation import (
    erhoehe_um_zwei,
    multipliziere_mit_drei,
    subtrahiere_zehn,
    teile_durch_vier,
)


def test_erhoehe_um_zwei_positive_integer():
    zahl = 3

    assert erhoehe_um_zwei(zahl) == 5


def test_erhoehe_um_zwei_zero_integer():
    zahl = 0

    assert erhoehe_um_zwei(zahl) == 2


def test_erhoehe_um_zwei_negative_integer():
    zahl = -2

    assert erhoehe_um_zwei(zahl) == 0


def test_erhoehe_um_zwei_positive_float():
    zahl = 2.5
    erwartetes_ergebnis = 4.5

    assert erhoehe_um_zwei(zahl) == pytest.approx(erwartetes_ergebnis)


def test_erhoehe_um_zwei_negative_float():
    zahl = -3.7
    erwartetes_ergebnis = -1.7

    assert erhoehe_um_zwei(zahl) == pytest.approx(erwartetes_ergebnis)


def test_multipliziere_mit_drei_positive_integer():
    zahl = 3

    assert multipliziere_mit_drei(zahl) == 9


def test_multipliziere_mit_drei_zero_integer():
    zahl = 0

    assert multipliziere_mit_drei(zahl) == 0


def test_multipliziere_mit_drei_negative_integer():
    zahl = -2

    assert multipliziere_mit_drei(zahl) == -6


def test_multipliziere_mit_drei_positive_float():
    zahl = 2.5
    erwartetes_ergebnis = 7.5

    assert multipliziere_mit_drei(zahl) == pytest.approx(erwartetes_ergebnis)


def test_multipliziere_mit_drei_negative_float():
    zahl = -3.7
    erwartetes_ergebnis = -11.1

    assert multipliziere_mit_drei(zahl) == pytest.approx(erwartetes_ergebnis)


def test_subtrahiere_zehn_positive_integer():
    zahl = 20

    assert subtrahiere_zehn(zahl) == 10


def test_subtrahiere_zehn_zero_integer():
    zahl = 0

    assert subtrahiere_zehn(zahl) == -10


def test_subtrahiere_zehn_negative_integer():
    zahl = -5

    assert subtrahiere_zehn(zahl) == -15


def test_subtrahiere_zehn_positive_float():
    zahl = 10.5
    erwartetes_ergebnis = 0.5

    assert subtrahiere_zehn(zahl) == pytest.approx(erwartetes_ergebnis)


def test_subtrahiere_zehn_negative_float():
    zahl = -9.2
    erwartetes_ergebnis = -19.2

    assert subtrahiere_zehn(zahl) == pytest.approx(erwartetes_ergebnis)


def test_teile_durch_vier_positive_integer():
    zahl = 8

    assert teile_durch_vier(zahl) == 2


def test_teile_durch_vier_negative_integer():
    zahl = -4

    assert teile_durch_vier(zahl) == -1


def test_teile_durch_vier_zero():
    zahl = 0

    with pytest.raises(ZeroDivisionError):
        teile_durch_vier(zahl)


def test_teile_durch_vier_non_divisible_integer():
    zahl = 5

    with pytest.raises(ValueError):
        teile_durch_vier(zahl)


def test_teile_durch_vier_float():
    zahl = 8.0
    erwartetes_ergebnis = 2.0

    assert teile_durch_vier(zahl) == pytest.approx(erwartetes_ergebnis)

