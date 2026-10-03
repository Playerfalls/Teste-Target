from datetime import date, datetime


TAXA_JUROS_DIARIA = 0.025


def calcular_juros(
    valor: float,
    data_vencimento: str,
    data_referencia: date | None = None,
) -> dict:
    """Calcula os juros de uma dívida em atraso."""

    if valor < 0:
        raise ValueError("O valor não pode ser negativo.")

    vencimento = datetime.strptime(
        data_vencimento,
        "%d/%m/%Y",
    ).date()

    if data_referencia is None:
        data_referencia = date.today()

    dias_atraso = max(
        0,
        (data_referencia - vencimento).days,
    )

    juros = valor * TAXA_JUROS_DIARIA * dias_atraso
    valor_final = valor + juros

    return {
        "dias_atraso": dias_atraso,
        "juros": juros,
        "valor_final": valor_final,
    }


def exibir_resultado(resultado: dict) -> None:
    """Exibe o resultado do cálculo no terminal."""

    print("\nCÁLCULO DE JUROS\n")
    print(f"Dias de atraso: {resultado['dias_atraso']}")
    print(f"Juros: R$ {resultado['juros']:.2f}")
    print(f"Valor final: R$ {resultado['valor_final']:.2f}")


def main() -> None:
    """Executa um exemplo de cálculo de juros."""

    resultado = calcular_juros(
        valor=1000,
        data_vencimento="20/09/2026",
    )

    exibir_resultado(resultado)


if __name__ == "__main__":
    main()