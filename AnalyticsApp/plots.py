from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px

import pandas as pd
import numpy as np
import datetime
import logging

logger = logging.getLogger(__name__)

def plot_metro_table():
    metro_hotness = pd.read_csv(
        "https://econdata.s3-us-west-2.amazonaws.com/Reports/Hotness/RDC_Inventory_Hotness_Metrics_Metro_History.csv")
    metro_hotness['month_date_yyyymm'] = pd.to_datetime(metro_hotness['month_date_yyyymm'],format = '%Y%m',
                                                        errors = 'coerce')

    current_rankings_metro = metro_hotness.loc[
        metro_hotness['month_date_yyyymm'] == max(metro_hotness.month_date_yyyymm)]
    current_rankings_metro = current_rankings_metro.sort_values(by = 'hotness_rank').head(100)
    current_rankings_metro = current_rankings_metro[['hotness_rank','cbsa_title','hotness_score','supply_score',
                                                     'demand_score','median_days_on_market','median_listing_price',]]

    metro_hotness_table = go.Figure(data = [go.Table(
        header = dict(values = list(current_rankings_metro.columns),
                      # fill_color='paleturquoise',
                      align = 'left'),
        cells = dict(values = current_rankings_metro.transpose().values.tolist(),
                     # fill_color='lavender',
                     align = 'left'))
    ])

    plot_div = plot(metro_hotness_table,output_type = 'div',include_plotlyjs = False)

    return plot_div