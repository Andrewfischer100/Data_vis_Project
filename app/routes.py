from flask import render_template
from . import app
from .data_analysis import get_data_from_csv, calculate_average_pph

import matplotlib.pyplot as plt
import seaborn as sns

from io import BytesIO
import base64

from flask import send_file

import plotly.express as px


csv_file_path = '/Users/andy/Downloads/UPS Scans - Sheet1.csv'
data = get_data_from_csv

def visualizations():
    # Your data retrieval and visualization code goes here
    average_pph = calculate_average_pph
    
    # Example Matplotlib visualization
    fig, ax = plt.subplots()
    sns.histplot(average_pph['PPH'], ax=ax, kde=True)
    plt.title('pph for andrew')
    plt.xlabel('pph')
    plt.ylabel('freq')

#save to bytes
    img = BytesIO
    fig.savefig(img, format='png')
    img.seek(0)
    plt.close()

    img_url =  base64.b64encode(img.getvalue()).decode()

    return render_template('visualization.html', average_pph=average_pph, img_url=img_url)


@app.route('/download_data')
def download_data():
    # Example Seaborn visualization
    sns.scatterplot(data=data, x='x', y='y')
    plt.savefig('static/seaborn_plot.png')

    # Example Plotly visualization
    fig = px.scatter(data, x='x', y='y', title='Plotly Scatter Plot')
    fig.write_html('templates/plotly_plot.html')

    return render_template('visualizations.html')