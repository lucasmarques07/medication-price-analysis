import data_loader as dl
import analysis as an
import database as db

try:
    dfFarmaGo = dl.load_farma_go("data/farmago.json")
    print('Data Frame created from the JSON.')
except Exception as e:
    print(f'Error processing the JSON file: {e}')

try:
    db.dataBaseExport(dfFarmaGo, "output/farmago.db")
    print("Data successfully exported")
except Exception as e:
    print(f"Error exporting the Data: {e}")

print(f'\nAverage price: {an.averagePrice(dfFarmaGo):.2f}')

df_avg = an.averagePricePerProduct(dfFarmaGo)
print(f'\nHighest Average: {an.highestAveragePricePerProduct(df_avg)}')

print(f'\nMedicine for less than R$15,00:\n {an.lessThan(15, dfFarmaGo)[["medicamento_nome", "nome", "preco"]]}')

print(f'\nLargest medicine inventory: {an.largestInventory(dfFarmaGo)["medicamento_nome"]} at {an.largestInventory(dfFarmaGo)["nome"]} ({an.largestInventory(dfFarmaGo)["estoque"]} units)')

highestPriceVariation = an.highestPriceVariation(dfFarmaGo)
print(f'\nHighest price variation: {highestPriceVariation["name"]} (Difference of R$ {highestPriceVariation["value"]:.2f})')

print(f'\nPharmacies with the best balance between price and distance: {an.betterPharmacies(dfFarmaGo)}')

import visualization as vs

vs.plot_average_price_per_medicine(dfFarmaGo)
vs.plot_price_by_pharmacy(dfFarmaGo)
vs.plot_price_distance(dfFarmaGo)