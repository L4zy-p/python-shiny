from pathlib import Path
import pandas as pd

import plotly.express as px
from shiny import reactive
from shiny.express import render, input, ui
from shinywidgets import render_plotly

ui.page_opts(title="Test shiny", fillable=True)

@reactive.calc
def dat():
    infile = Path(__file__).parent / "data/sales.csv"
    return pd.read_csv(infile)

with ui.layout_columns():

    @render_plotly
    def plot1():
        df = dat()
        top_sales = df.groupby('product')['quantity_ordered'].sum().reset_index()
        return px.bar(top_sales, x='product', y='quantity_ordered')
    
    @render.data_frame
    def data():
        return dat()