import pandas as pd

def averagePrice(df):
    return df["preco"].mean()

def averagePricePerProduct(df):
    return df.groupby("medicamento_nome")["preco"].mean().reset_index()

def highestAveragePricePerProduct(df_avg):
    return df_avg.loc[df_avg["preco"].idxmax(), "medicamento_nome"]

def lessThan(num, df):
    return df[df["preco"] < num]

def largestInventory(df):
    return df.loc[df["estoque"].idxmax()]

def highestPriceVariation(df):
    dfCheaper = df.groupby("medicamento_nome")["preco"].min().reset_index()
    dfMoreExpensive = df.groupby("medicamento_nome")["preco"].max().reset_index()

    dfDifference = pd.DataFrame()

    dfDifference["medicamento_nome"] = dfCheaper["medicamento_nome"]
    dfDifference["difference"] = dfMoreExpensive["preco"] - dfCheaper["preco"]

    maxDiffIndex = dfDifference["difference"].idxmax()

    maxDiffMedicine = dfDifference.loc[maxDiffIndex, "medicamento_nome"]
    maxDiffValue = dfDifference.loc[maxDiffIndex, "difference"]

    return {"name": maxDiffMedicine, "value": maxDiffValue}

def betterPharmacies(df):
    lessThanAverageDistance = df[df["distancia_km"] < df["distancia_km"].mean()]
    lessThanAverageDistance

    dfCloserPharmacies = lessThanAverageDistance[["nome", "distancia_km"]].drop_duplicates().reset_index(drop=True)
    dfCloserPharmacies

    averagePricePerPharmacy = df.groupby("nome")["preco"].mean().reset_index()

    dfCheapPharmacies = averagePricePerPharmacy[averagePricePerPharmacy["preco"] < df["preco"].mean()].reset_index(drop=True)
    dfCheapPharmacies

    return [pharmacy for pharmacy in dfCheapPharmacies["nome"] if pharmacy in dfCloserPharmacies["nome"].values]