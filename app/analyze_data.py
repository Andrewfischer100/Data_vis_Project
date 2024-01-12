from data_analysis import get_data_from_csv, calculate_average_pph

csv_file_path = '/Users/andy/Downloads/UPS Scans - Sheet1.csv'

#gets the data
data = get_data_from_csv(csv_file_path)

#calc PPH

average_pph = calculate_average_pph(data)
print(f"average pph: {average_pph}")
