
from flask import Flask, render_template, request, send_file
import pandas as pd
import os
from io import BytesIO
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if not file:
        return 'فایل یافت نشد'
    
    df = pd.read_excel(file)

    output = []
    for index, row in df.iterrows():
        start_hour = row['ساعت شروع']
        duration = row['مدت کلاس (دقیقه)']
        end_time = (datetime.strptime(str(start_hour), '%H:%M') + timedelta(minutes=int(duration))).strftime('%H:%M')
        output.append({
            'کد کلاس': row['کد کلاس'],
            'نام درس': row['نام درس'],
            'نام استاد': row['نام استاد'],
            'ساعت کلاس': f"{start_hour} تا {end_time}"
        })

    result_df = pd.DataFrame(output)
    result_df.to_excel("output.xlsx", index=False)
    
    return render_template('result.html', tables=[result_df.to_html(classes='table')])

@app.route('/download/excel')
def download_excel():
    try:
        return send_file("output.xlsx", as_attachment=True)
    except Exception as e:
        return f"خطا در دانلود فایل: {e}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
