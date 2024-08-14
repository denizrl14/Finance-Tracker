import pandas as pd

# Load the data
df = pd.read_csv('data.csv')
info = df.columns.tolist()

grocery_stores = [
    "Edeka",
    "Lidl",
    "Kaufland",
    "REWE",
    "Aldi",
    "Netto",
    "Penny",
    "Real",
    "Globus",
    "Hit",
    "Tegut",
    "Denn's Biomarkt",
    "Alnatura",
    "Bio Company",
    "Marktkauf",
    "Metro Cash & Carry",
    "nah & frisch",
    "Norma",
    "Lekkerland",
    "Bela"
]

drugstores = [
    "dm-drogerie markt",
    "Rossmann",
    "Müller",
    "Budni",
]

pharmacies = [
    "Apotheke",
    "DocMorris",
    "Sanicare",
    "Shop-Apotheke",
    "Zur Rose",
    "Europa Apotheek",
    "medpex",
    "medikamente-per-klick",
    "apotal",
    "Volksversand",
    "Apo-Rot",
    "ApoDiscounter",
    "Apotheke.de",
    "Aliva",
    "pharmeo",
    "mycare",
    "pharmasana"
]

daily_costs = grocery_stores + drugstores + pharmacies


def categorize_expenses(expense, keywords, category):
    if isinstance(expense, str):
        for keyword in keywords:
            if keyword in expense:
                return category
    return ""
        





def recognize_daily_costs():
    my_list = []
    for i in range(0, len(df)):
        for column in df.columns:
            my_list.append(categorize_expenses(df.iloc[i][column], daily_costs, "Daily Costs"))
    return my_list

print(recognize_daily_costs())



 


