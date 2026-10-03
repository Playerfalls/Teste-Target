from datetime import date

import pytest

from src.questao3_juros import calcular_juros


def test_calcula_juros_para_pagamento_em_atraso():
    resultado = calcular_juros(
        valor=1000,
        data_vencimento="20/09/2026",
        data_referencia=date(2026, 9, 30),
    )

    assert resultado["dias_atraso"] == 10
    assert resultado["juros"] == 250
    assert resultado["valor_final"] == 1250


def test_nao_calcula_juros_antes_do_vencimento():
    resultado = calcular_juros(
        valor=1000,
        data_vencimento="30/09/2026",
        data_referencia=date(2026, 9, 20),
    )

    assert resultado["dias_atraso"] == 0
    assert resultado["juros"] == 0
    assert resultado["valor_final"] == 1000


def test_nao_calcula_juros_no_dia_do_vencimento():
    resultado = calcular_juros(
        valor=1000,
        data_vencimento="20/09/2026",
        data_referencia=date(2026, 9, 20),
    )

    assert resultado["dias_atraso"] == 0
    assert resultado["juros"] == 0
    assert resultado["valor_final"] == 1000


def test_nao_permite_valor_negativo():
    with pytest.raises(ValueError, match="não pode ser negativo"):
        calcular_juros(
            valor=-100,
            data_vencimento="20/09/2026",
            data_referencia=date(2026, 9, 30),
        )