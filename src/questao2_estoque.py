from itertools import count


class Estoque:
    """Controla produtos, movimentações e histórico do estoque."""

    def __init__(self, produtos: dict):
        self._produtos = produtos
        self._historico = []
        self._contador_movimentacao = count(1)

    def movimentar(
        self,
        codigo_produto: int,
        tipo: str,
        quantidade: int,
        descricao_movimentacao: str,
    ) -> dict:
        """Registra uma entrada ou saída no estoque."""

        if codigo_produto not in self._produtos:
            raise ValueError("Produto não encontrado.")

        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")

        tipo = tipo.lower()

        if tipo not in ("entrada", "saida"):
            raise ValueError("Tipo deve ser 'entrada' ou 'saida'.")

        produto = self._produtos[codigo_produto]

        if tipo == "saida":
            if quantidade > produto["quantidade"]:
                raise ValueError("Estoque insuficiente.")

            produto["quantidade"] -= quantidade
        else:
            produto["quantidade"] += quantidade

        movimentacao = {
            "id": next(self._contador_movimentacao),
            "codigo_produto": codigo_produto,
            "produto": produto["descricao"],
            "tipo": tipo,
            "quantidade": quantidade,
            "descricao": descricao_movimentacao,
            "estoque_final": produto["quantidade"],
        }

        self._historico.append(movimentacao)

        return movimentacao

    def consultar_estoque(self, codigo_produto: int) -> dict:
        """Retorna os dados de um produto sem permitir alteração direta."""

        if codigo_produto not in self._produtos:
            raise ValueError("Produto não encontrado.")

        return self._produtos[codigo_produto].copy()

    def consultar_historico(self) -> list[dict]:
        """Retorna uma cópia do histórico de movimentações."""

        return [movimentacao.copy() for movimentacao in self._historico]


ESTOQUE_INICIAL = {
    101: {"descricao": "Caneta Azul", "quantidade": 150},
    102: {"descricao": "Caderno Universitário", "quantidade": 75},
    103: {"descricao": "Borracha Branca", "quantidade": 200},
    104: {"descricao": "Lápis Preto HB", "quantidade": 320},
    105: {"descricao": "Marcador de Texto Amarelo", "quantidade": 90},
}


def exibir_movimentacao(movimentacao: dict) -> None:
    """Exibe os dados de uma movimentação."""

    print("\nMOVIMENTAÇÃO REGISTRADA")
    print(f"ID: {movimentacao['id']}")
    print(f"Produto: {movimentacao['produto']}")
    print(f"Tipo: {movimentacao['tipo']}")
    print(f"Quantidade: {movimentacao['quantidade']}")
    print(f"Descrição: {movimentacao['descricao']}")
    print(f"Estoque final: {movimentacao['estoque_final']}")


def main() -> None:
    """Executa um exemplo de movimentação."""

    estoque = Estoque(ESTOQUE_INICIAL.copy())

    movimentacao = estoque.movimentar(
        codigo_produto=101,
        tipo="saida",
        quantidade=10,
        descricao_movimentacao="Venda para cliente",
    )

    exibir_movimentacao(movimentacao)


if __name__ == "__main__":
    main()