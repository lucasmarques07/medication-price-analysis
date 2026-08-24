import pandas as pd
from sqlalchemy import create_engine

jsonPath = "data/farmago.json"

try:
    df = pd.read_json(jsonPath, encoding="utf-8")
    dfFarmaGo = pd.json_normalize(
        df["medicamentos"],
        record_path="farmacias",
        meta=["nome", "categoria"],
        meta_prefix="medicamento_"
    )
    print("Data Frame created from the JSON.\n")
except Exception as e:
    print(f"Error processing the JSON file: {e}\n")

averagePrice = dfFarmaGo["preco"].mean()
print(f"Average price: {averagePrice:.2f}")

engine = create_engine("sqlite:///farmago.db")

try:
    dfFarmaGo.to_sql('medicamentos', con=engine, if_exists='replace', index=False)
    print("Data successfully exported")
except Exception as e:
    print(f"Error exporting the Data: {e}")

averagePricePerProduct = dfFarmaGo.groupby("medicamento_nome")["preco"].mean().reset_index()
highestAverage = averagePricePerProduct.loc[averagePricePerProduct["preco"].idxmax(), "medicamento_nome"]
print(f"Highest Average: {highestAverage}")

lessThan15 = dfFarmaGo[dfFarmaGo["preco"] < 15]
print(f"Medicine for less than R$15,00:\n {lessThan15[['medicamento_nome', 'nome', 'preco']]}")

largestInventory = dfFarmaGo.loc[dfFarmaGo["estoque"].idxmax()]
print(f"\nLargest medicine inventory: {largestInventory['medicamento_nome']} at {largestInventory['nome']} ({largestInventory['estoque']} units)")

dfCheaper = dfFarmaGo.groupby("medicamento_nome")["preco"].min().reset_index()
dfMoreExpensive = dfFarmaGo.groupby("medicamento_nome")["preco"].max().reset_index()

dfDifference = pd.DataFrame()

dfDifference["medicamento_nome"] = dfCheaper["medicamento_nome"]
dfDifference["difference"] = dfMoreExpensive["preco"] - dfCheaper["preco"]

maxDiffIndex = dfDifference["difference"].idxmax()

maxDiffMedicine = dfDifference.loc[maxDiffIndex, "medicamento_nome"]
maxDiffValue = dfDifference.loc[maxDiffIndex, "difference"]

print(f"\n5. Highest price variation: {maxDiffMedicine} (Difference of R$ {maxDiffValue:.2f})")

lessThanAverageDistance = dfFarmaGo[dfFarmaGo["distancia_km"] < dfFarmaGo["distancia_km"].mean()]
lessThanAverageDistance

dfCloserPharmacies = lessThanAverageDistance[["nome", "distancia_km"]].drop_duplicates().reset_index(drop=True)
dfCloserPharmacies

averagePricePerPharmacy = dfFarmaGo.groupby("nome")["preco"].mean().reset_index()

dfCheapPharmacies = averagePricePerPharmacy[averagePricePerPharmacy["preco"] < dfFarmaGo["preco"].mean()].reset_index(drop=True)
dfCheapPharmacies

betterPharmacies = [pharmacy for pharmacy in dfCheapPharmacies["nome"] if pharmacy in dfCloserPharmacies["nome"].values]
print(f"Pharmacies with the best balance between price and distance: {betterPharmacies}")

engine = create_engine("sqlite:///farmago.db")

try:
    dfFarmaGo.to_sql('medicamentos', con=engine, if_exists='replace', index=False)
    print("Data successfully exported to the medicines table")
except Exception as e:
    print(f"An error occurred while exporting data: {e}")