from typing import Tuple

import numpy as np
from statsmodels.tsa.arima.model import ARIMA

from tsforecasting_dynamicselection.models.model_base import BaseModel


class Arima(BaseModel):

    def __init__(self, order: Tuple[int, int, int]):
        super().__init__()
        self._order = order
        self._model = None

    def fit(self, ts_train: np.ndarray):
        self._model = ARIMA(ts_train, order=self._order)
        self._model.fit()

    def predict(self, ts_test: np.ndarray) -> np.ndarray:
        pass
