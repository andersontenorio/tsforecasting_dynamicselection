from abc import ABC, abstractmethod

import numpy as np


class BaseModel(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def fit(self, ts_train: np.ndarray):
        """

        :param ts_train:
        :return:
        """

    @abstractmethod
    def predict(self, ts_test: np.ndarray) -> np.ndarray:
        """

        :param ts_test:
        :return:
        """

    def fit_predict(self, ts_train: np.ndarray, ts_test: np.ndarray):
        self.fit(ts_train)
        return self.predict(ts_test)
