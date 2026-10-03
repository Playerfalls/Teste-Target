from datetime import datetime


def calcular_juros(valor: float, data_vencimento: str):
    hoje = datetime.now().date()

    vencimento = datetime.strptime(
        data_vencimento,
        "%d/%m/%Y"
    ).date()

    dias_atraso = (hoje - vencimento).days

    if dias_atraso <= 0:
        return {
            "dias_atraso": 0,
            "juros": 0,
            "valor_final": valor,
        }

    juros = valor * 0.025 * dias_atraso
    valor_final = valor + juros

    return {
        "dias_atraso": dias_atraso,
        "juros": juros,
        "valor_final": valor_final,
    }


if __name__ == "__main__":
    resultado = calcular_juros(
        valor=1000,
        data_vencimento="20/09/2026"
    )

    print("\nCÁLCULO DE JUROS\n")
    print(f"Dias de atraso: {resultado['dias_atraso']}")
    print(f"Juros: R$ {resultado['juros']:.2f}")
    print(f"Valor final: R$ {resultado['valor_final']:.2f}")