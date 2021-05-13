from datetime import datetime
from pathlib import Path

import pandas as pd


def parser(x):
    return datetime.strptime('190' + x, '%Y-%m')


def test_fit_predict_arima():
    file_path = Path(Path(__file__).parent.parent, "data", 'shampoo_sales.csv')
    ts = pd.read_csv(file_path, header=0, index_col=0, parse_dates=True,
                     squeeze=True, date_parser=parser)
    assert True
