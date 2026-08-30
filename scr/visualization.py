import matplotlib.pyplot as plt


def plot_average_price_per_medicine(df):
    average_price = (
        df.groupby("medicamento_nome")["preco"]
        .mean()
        .reset_index()
    )

    plt.figure(figsize=(9, 5))

    plt.bar(
        average_price["medicamento_nome"],
        average_price["preco"]
    )

    plt.title("Preço médio por medicamento")
    plt.xlabel("Medicamento")
    plt.ylabel("Preço médio (R$)")

    plt.xticks(rotation=20)
    plt.tight_layout()

    plt.show()


def plot_price_by_pharmacy(df):
    plt.figure(figsize=(10, 6))

    for medicine in df["medicamento_nome"].unique():
        medicine_data = df[
            df["medicamento_nome"] == medicine
        ]

        plt.plot(
            medicine_data["nome"],
            medicine_data["preco"],
            marker="o",
            label=medicine
        )

    plt.title("Comparação de preços entre farmácias")
    plt.xlabel("Farmácia")
    plt.ylabel("Preço (R$)")

    plt.xticks(rotation=20)
    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_price_distance(df):
    plt.figure(figsize=(9, 5))

    plt.scatter(
        df["distancia_km"],
        df["preco"]
    )

    plt.title("Relação entre preço e distância")
    plt.xlabel("Distância (km)")
    plt.ylabel("Preço (R$)")

    plt.tight_layout()
    plt.show()