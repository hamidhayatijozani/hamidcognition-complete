# core/model.py
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler

class PricePredictor:
    def __init__(self, horizon=5):
        self.horizon = horizon
        self.model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)
        self.scaler = StandardScaler()
        self.is_trained = False

    def prepare_features(self, df):
        """استخراج ویژگی‌های تکنیکال ساده"""
        df = df.copy()
        df['returns'] = df['close'].pct_change()
        df['volatility'] = df['returns'].rolling(window=10).std()
        df['ma_short'] = df['close'].rolling(window=10).mean()
        df['ma_long'] = df['close'].rolling(window=30).mean()
        df['momentum'] = df['close'] - df['close'].shift(10)
        return df.dropna()

    def train(self, df):
        """آموزش مدل روی داده‌های تاریخی"""
        data = self.prepare_features(df)
        if len(data) < 100: return False
        
        X = data[['returns', 'volatility', 'ma_short', 'ma_long', 'momentum']].values
        # هدف: قیمت در افق زمانی آینده
        y = data['close'].shift(-self.horizon).dropna().values
        X = X[:len(y)]
        
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        self.is_trained = True
        return True

    def predict(self, df):
        """پیش‌بینی قیمت آینده"""
        if not self.is_trained: return None
        
        data = self.prepare_features(df)
        last_row = data.iloc[-1:][['returns', 'volatility', 'ma_short', 'ma_long', 'momentum']].values
        last_row_scaled = self.scaler.transform(last_row)
        
        prediction = self.model.predict(last_row_scaled)[0]
        return float(prediction)
