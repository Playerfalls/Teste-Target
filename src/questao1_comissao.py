from collections import defaultdict


DADOS = {
    "vendas": [
        {"vendedor": "João Silva", "valor": 1200.50},
        {"vendedor": "João Silva", "valor": 950.75},
        {"vendedor": "João Silva", "valor": 1800.00},
        {"vendedor": "João Silva", "valor": 1400.30},
        {"vendedor": "João Silva", "valor": 1100.90},
        {"vendedor": "João Silva", "valor": 1550.00},
        {"vendedor": "João Silva", "valor": 1700.80},
        {"vendedor": "João Silva", "valor": 250.30},
        {"vendedor": "João Silva", "valor": 480.75},
        {"vendedor": "João Silva", "valor": 320.40},
        {"vendedor": "Maria Souza", "valor": 2100.40},
        {"vendedor": "Maria Souza", "valor": 1350.60},
        {"vendedor": "Maria Souza", "valor": 950.20},
        {"vendedor": "Maria Souza", "valor": 1600.75},
        {"vendedor": "Maria Souza", "valor": 1750.00},
        {"vendedor": "Maria Souza", "valor": 1450.90},
        {"vendedor": "Maria Souza", "valor": 400.50},
        {"vendedor": "Maria Souza", "valor": 180.20},
        {"vendedor": "Maria Souza", "valor": 90.75},
    ]
}


def calcular_comissao(valor: float) -> float:
    """Calcula a comissão de uma venda conforme sua faixa de valor."""
    if valor < 100:
        return 0.0

    if valor < 500:
        return valor * 0.01

    return valor * 0.05


def processar_vendas(vendas: list[dict]) -> dict:
    """Agrupa as vendas por vendedor e calcula os respectivos totais."""
    resumo = defaultdict(lambda: {"total_vendido": 0.0, "comissao": 0.0})

    for venda in vendas:
        vendedor = venda["vendedor"]
        valor = venda["valor"]

        resumo[vendedor]["total_vendido"] += valor
        resumo[vendedor]["comissao"] += calcular_comissao(valor)

    return dict(resumo)


def exibir_relatorio(resumo: dict) -> None:
    """Exibe o relatório de comissões no terminal."""
    print("\nRELATÓRIO DE COMISSÕES\n")

    for vendedor, dados in resumo.items():
        print(f"Vendedor: {vendedor}")
        print(f"Total vendido: R$ {dados['total_vendido']:.2f}")
        print(f"Comissão: R$ {dados['comissao']:.2f}")
        print("-" * 40)


def main() -> None:
    """Executa o processamento completo das vendas."""
    resumo = processar_vendas(DADOS["vendas"])
    exibir_relatorio(resumo)


if __name__ == "__main__":
    main()