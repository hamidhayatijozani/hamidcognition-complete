# config.py - قلب تنظیمات HamidCognition v0
import os

SYMBOL = "EURUSD"
TIMEFRAME = "M1"    # M1, M5, M15
WINDOW = 300        # تعداد کندل برای snapshot

MEMORY_MAX = 1000
SHORT_MEMORY = 10
MID_MEMORY = 30
LONG_MEMORY = 100

ROLL_WINDOW = 20    # برای رفتار کوتاه‌مدت

SLEEP_SECONDS = 60
DB_PATH = "predictions.db"

# تنظیمات مدل
TRAIN_MIN_SAMPLES = 500   # حداقل لاگ برای آموزش
HORIZON = 5               # افق پیش‌بینی (۵ کندل بعدی)
THRESH_RETURN = 0.0005    # حد آستانه برای حرکت معنی‌دار

# تنظیمات سرور
PORT = int(os.getenv("PORT", 5000))
DEBUG = False
