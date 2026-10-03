from itertools import count

contador_movimentacao = count(1)

estoque = {
    101: {"descricao": "Caneta Azul", "quantidade": 150},
    102: {"descricao": "Caderno Universitário", "quantidade": 75},
    103: {"descricao": "Borracha Branca", "quantidade": 200},
    104: {"descricao": "Lápis Preto HB", "quantidade": 320},
    105: {"descricao": "Marcador de Texto Amarelo", "quantidade": 90},
}


def movimentar_estoque(
    codigo_produto: int,
    tipo: str,
    quantidade: int,
    descricao_movimentacao: str,
):
    if codigo_produto not in estoque:
        raise ValueError("Produto não encontrado.")

    produto = estoque[codigo_produto]

    if tipo.lower() == "entrada":
        produto["quantidade"] += quantidade

    elif tipo.lower() == "saida":
        if quantidade > produto["quantidade"]:
            raise ValueError("Estoque insuficiente.")

        produto["quantidade"] -= quantidade

    else:
        raise ValueError("Tipo deve ser 'entrada' ou 'saida'.")

    identificador = next(contador_movimentacao)

    print("\nMOVIMENTAÇÃO REGISTRADA")
    print(f"ID: {identificador}")
    print(f"Produto: {produto['descricao']}")
    print(f"Tipo: {tipo}")
    print(f"Descrição: {descricao_movimentacao}")
    print(f"Estoque final: {produto['quantidade']}")


if __name__ == "__main__":
    movimentar_estoque(
        codigo_produto=101,
        tipo="saida",
        quantidade=10,
        descricao_movimentacao="Venda para cliente"
    )