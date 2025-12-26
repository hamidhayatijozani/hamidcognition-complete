# app.py - فایل اصلی وب‌سایت (شسته و رفته)
from flask import Flask, render_template, jsonify
import os
from main import system
from config import PORT, DEBUG

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    return jsonify({
        "prediction": system.last_prediction,
        "status": "active" if system.is_running else "initializing"
    })

if __name__ == '__main__':
    system.start()
    # استفاده از پورت متغیر محیطی برای سازگاری با تمام پلتفرم‌های Deploy
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
