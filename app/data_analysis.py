import pandas as pd
import numpy as np

def get_data_from_csv(file_path):
    data = pd.read_csv(file_path)
    return data

def calculate_average_pph(data):

    average_pph = data['PPH'].mean()
    return average_pph