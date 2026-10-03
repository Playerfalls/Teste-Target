from src.questao1_comissao import calcular_comissao, processar_vendas


def test_comissao_para_valor_abaixo_de_100():
    assert calcular_comissao(50) == 0.0


def test_comissao_para_valor_entre_100_e_499():
    assert calcular_comissao(200) == 2.0


def test_comissao_para_valor_a_partir_de_500():
    assert calcular_comissao(500) == 25.0


def test_processar_vendas_agrupa_por_vendedor():
    vendas = [
        {"vendedor": "João", "valor": 100},
        {"vendedor": "João", "valor": 500},
        {"vendedor": "Maria", "valor": 200},
    ]

    resultado = processar_vendas(vendas)

    assert resultado["João"]["total_vendido"] == 600
    assert resultado["João"]["comissao"] == 26
    assert resultado["Maria"]["total_vendido"] == 200
    assert resultado["Maria"]["comissao"] == 2