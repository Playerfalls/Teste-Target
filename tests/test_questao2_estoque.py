import pytest

from src.questao2_estoque import Estoque


@pytest.fixture
def estoque():
    return Estoque(
        {
            101: {"descricao": "Caneta Azul", "quantidade": 100},
        }
    )


def test_saida_reduz_estoque(estoque):
    resultado = estoque.movimentar(
        codigo_produto=101,
        tipo="saida",
        quantidade=10,
        descricao_movimentacao="Venda",
    )

    assert resultado["estoque_final"] == 90
    assert estoque.consultar_estoque(101)["quantidade"] == 90


def test_entrada_aumenta_estoque(estoque):
    resultado = estoque.movimentar(
        codigo_produto=101,
        tipo="entrada",
        quantidade=20,
        descricao_movimentacao="Reposição",
    )

    assert resultado["estoque_final"] == 120


def test_nao_permite_saida_maior_que_estoque(estoque):
    with pytest.raises(ValueError, match="Estoque insuficiente"):
        estoque.movimentar(
            codigo_produto=101,
            tipo="saida",
            quantidade=150,
            descricao_movimentacao="Venda",
        )


def test_nao_permite_quantidade_zero(estoque):
    with pytest.raises(ValueError, match="maior que zero"):
        estoque.movimentar(
            codigo_produto=101,
            tipo="entrada",
            quantidade=0,
            descricao_movimentacao="Reposição",
        )


def test_nao_permite_produto_inexistente(estoque):
    with pytest.raises(ValueError, match="Produto não encontrado"):
        estoque.movimentar(
            codigo_produto=999,
            tipo="saida",
            quantidade=10,
            descricao_movimentacao="Venda",
        )


def test_registra_historico_das_movimentacoes(estoque):
    estoque.movimentar(
        codigo_produto=101,
        tipo="saida",
        quantidade=10,
        descricao_movimentacao="Venda",
    )

    estoque.movimentar(
        codigo_produto=101,
        tipo="entrada",
        quantidade=30,
        descricao_movimentacao="Reposição",
    )

    historico = estoque.consultar_historico()

    assert len(historico) == 2
    assert historico[0]["id"] == 1
    assert historico[0]["tipo"] == "saida"
    assert historico[1]["id"] == 2
    assert historico[1]["tipo"] == "entrada"


def test_consulta_nao_permite_alterar_estoque_diretamente(estoque):
    produto = estoque.consultar_estoque(101)

    produto["quantidade"] = 999

    assert estoque.consultar_estoque(101)["quantidade"] == 100