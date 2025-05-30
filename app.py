from flask import Flask, render_template, request, send_file
import pandas as pd
import io
from scheduler import schedule_classes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    df = pd.read_excel(file)
    schedule, errors = schedule_classes(df)
    output_excel = io.BytesIO()
    schedule.to_excel(output_excel, index=False)
    output_excel.seek(0)
    return send_file(output_excel, download_name='program.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
