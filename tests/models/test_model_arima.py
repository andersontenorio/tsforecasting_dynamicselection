from datetime import datetime
from pathlib import Path

import pandas as pd

from tsforecasting_dynamicselection.models.model_arima import Arima


def parser(x):
    return datetime.strptime('190' + x, '%Y-%m')


def test_fit_predict_arima():
    file_path = Path(Path(__file__).parent.parent, "data", 'shampoo_sales.csv')
    ts = pd.read_csv(file_path, header=0, index_col=0, parse_dates=True,
                     squeeze=True, date_parser=parser)
    ts.index = ts.index.to_period('M')
    # split into train and test sets
    X = ts.values
    size = int(len(X) * 0.66)
    ts_train, ts_test = X[0:size], X[size:len(X)]
    arima = Arima(order=(5, 1, 0))
    arima.fit_predict(ts_train, ts_test)
    assert True
