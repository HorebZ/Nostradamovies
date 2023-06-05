import os
import pandas as pd

def get_dataframe():
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'static', 'data', 'poster')
    # Charger le CSV dans un DataFrame pandas
    df = pd.read_csv(csv_path)

    # Convertir le DataFrame en une liste de dictionnaires
    films = df.to_dict('records')