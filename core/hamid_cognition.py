# core/behavior.py
import numpy as np
from datetime import datetime

class HamidCognition:
    """موتور شناختی P/S/T: مغز متفکر سیستم"""
    
    def __init__(self, P=0.88, S=0.78, T=0.40):
        self.P = P  # Penetration (نفوذ)
        self.S = S  # Creative Connection (اتصال خلاق)
        self.T = T  # Stabilization (تثبیت)
        self.history = []
        
    def calculate_energy(self):
        """محاسبه انرژی شناختی برای تعیین قدرت روند"""
        creativity = (self.P * self.S) / (1.1 - self.T + 1e-9)
        stability = self.T / (self.P + self.S + 1e-9)
        energy = creativity * (1 - stability)
        return min(max(energy, 0), 1.5)
    
    def step(self, market_pressure, market_novelty):
        """گام شناختی: تطبیق ذهن با واقعیت بازار"""
        # P: واکنش به فشار بازار (نوسان)
        P_change = 0.05 * market_pressure * (1 - self.T)
        self.P = min(max(self.P + P_change, 0.1), 0.95)
        
        # S: واکنش به نوآوری (حرکات غیرمنتظره)
        S_change = 0.04 * market_novelty * (1 - abs(self.P - self.S))
        self.S = min(max(self.S + S_change, 0.1), 0.95)
        
        # T: تلاش برای تثبیت
        T_change = 0.03 * (self.S / (self.P + 1e-9)) * (1 + market_pressure)
        self.T = min(max(self.T + T_change, 0.1), 0.8)
        
        phase = self.detect_phase()
        state = {
            "timestamp": datetime.now().isoformat(),
            "P": round(self.P, 4),
            "S": round(self.S, 4),
            "T": round(self.T, 4),
            "energy": round(self.calculate_energy(), 4),
            "phase": phase
        }
        self.history.append(state)
        if len(self.history) > 1000: self.history.pop(0)
        return state
    
    def detect_phase(self):
        """تشخیص فاز روانی بازار"""
        diff = abs(self.P - self.S)
        if diff < 0.15:
            return "RUPTURE_IMMINENT"
        elif self.T < 0.45:
            return "UNSTABLE_CREATIVITY"
        elif self.P > 0.85 and self.S > 0.8:
            return "SYNTHESIS_PEAK"
        else:
            return "STEADY_EXPLORATION"

    def get_bias_adjustment(self):
        """تبدیل وضعیت ذهنی به اعداد ریاضی برای اصلاح قیمت"""
        phase = self.detect_phase()
        energy = self.calculate_energy()
        
        adjustments = {
            "RUPTURE_IMMINENT": 1.5,
            "UNSTABLE_CREATIVITY": 1.2,
            "SYNTHESIS_PEAK": 1.0,
            "STEADY_EXPLORATION": 0.8
        }
        
        return {
            "volatility_multiplier": adjustments.get(phase, 1.0),
            "confidence": min(energy * 100, 95),
            "phase": phase
        }
