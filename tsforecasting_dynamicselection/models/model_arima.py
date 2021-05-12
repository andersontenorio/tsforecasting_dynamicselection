from typing import Tuple

import numpy as np
from statsmodels.tsa.arima.model import ARIMA

from tsforecasting_dynamicselection.models.model_base import BaseModel


class Arima(BaseModel):

    def __init__(self, order: Tuple[int, int, int]):
        super().__init__()
        self._order = order
        self._model = None
        self._ts_history = None

    def fit(self, ts_train: np.ndarray):
        self._ts_history = [x for x in ts_train]

    def predict(self, ts_test: np.ndarray) -> np.ndarray:
        ts_pred = np.empty(len(ts_test))
        for t in range(len(ts_test)):
            self._model = ARIMA(self._ts_history, order=self._order)
            self._model.fit()
            output = self._model.forecast()
            yhat = output[0]
            ts_pred[t] = yhat
            self._ts_history.append(ts_test[t])
