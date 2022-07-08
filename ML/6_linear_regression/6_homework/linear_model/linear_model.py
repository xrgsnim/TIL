import numpy as np

class LinearRegression(object):
    def __init__(self, fit_intercept=True, copy_X=True):
        self.fit_intercept = fit_intercept
        self.copy_X = copy_X

        self._coef = None
        self._intercept = None
        self._new_X = None
        self.w_hat = None

# 질문. 객체형식으로 코딩하는방법을 잘 모름. 아래 함수가 실행됐을 때 반환하는 값 어떻게 정해줘야하는지..

    def fit(self, X, y):
        self._new_X = X
        if self.fit_intercept == True:
            self._new_X = np.concatenate((np.ones((len(X), 1)), X), axis=1)        
        self.w_hat = np.linalg.inv((self._new_X.T).dot(self._new_X)).dot(self._new_X.T).dot(y)
        # else:
        #     self.w_hat = np.linalg.inv((self._new_X.T).dot(self._new_X)).dot(self._new_X.T).dot(y)

        self._coef = self.w_hat[1:]
        self._intercept = self.w_hat[0]
        return self._new_X, self._coef, self._intercept, self.w_hat
        

    def predict(self, X):
        if self.fit_intercept == True:
            y_predict = np.dot(self._new_X, self.w_hat)
        return y_predict

    @property
    def coef(self):
        return self._coef

    @property
    def intercept(self):
        return self._intercept



