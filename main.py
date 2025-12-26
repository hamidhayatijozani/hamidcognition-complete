# main.py - مدیریت چرخه حیات سیستم
import time
import threading
from datetime import datetime
import pandas as pd
import os

from config import *
from market_feed import get_candles
from core.hamid_cognition import HamidCognition
from model import PricePredictor

class HamidSystem:
    def __init__(self):
        self.cognition = HamidCognition()
        self.predictor = PricePredictor(horizon=HORIZON)
        self.current_data = None
        self.last_prediction = None
        self.is_running = False

    def update_cycle(self):
        print("🚀 HamidCognition Cycle Started...")
        while self.is_running:
            try:
                # 1. دریافت داده
                df = get_candles(SYMBOL, TIMEFRAME, WINDOW)
                if df.empty:
                    time.sleep(10)
                    continue
                
                self.current_data = df
                
                # 2. تحلیل شناختی
                returns = df['close'].pct_change().dropna()
                pressure = returns.std() * 100
                novelty = abs(returns.iloc[-1]) * 100 if len(returns) > 0 else 0
                
                cog_state = self.cognition.step(pressure, novelty)
                bias = self.cognition.get_bias_adjustment()
                
                # 3. آموزش و پیش‌بینی
                if not self.predictor.is_trained:
                    self.predictor.train(df)
                
                raw_pred = self.predictor.predict(df)
                
                if raw_pred:
                    current_price = df['close'].iloc[-1]
                    diff = raw_pred - current_price
                    adjusted_pred = current_price + (diff * bias['volatility_multiplier'])
                    
                    self.last_prediction = {
                        "timestamp": datetime.now().isoformat(),
                        "current_price": round(current_price, 5),
                        "predicted_price": round(adjusted_pred, 5),
                        "horizon_mins": HORIZON,
                        "confidence": round(bias['confidence'], 2),
                        "phase": bias['phase'],
                        "cog_state": cog_state
                    }
                    print(f"✅ Prediction: {self.last_prediction['predicted_price']} | Phase: {bias['phase']}")
                
            except Exception as e:
                print(f"❌ Error in cycle: {e}")
            
            time.sleep(SLEEP_SECONDS)

    def start(self):
        self.is_running = True
        self.thread = threading.Thread(target=self.update_cycle, daemon=True)
        self.thread.start()

# نمونه جهانی برای استفاده در API
system = HamidSystem()
