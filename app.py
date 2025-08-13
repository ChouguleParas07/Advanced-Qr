from flask import Flask, render_template, request, redirect, send_from_directory, flash
import os
from utils.url_shortener import UrlShortener
from utils.qr_generator import QRGenerator

app = Flask(__name__)
app.secret_key = 'change_me'  # For flash messages

url_shortener = UrlShortener()
qr_generator = QRGenerator()

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = qr_code_file = ''
    if request.method == 'POST':
        url = request.form.get('url')
        action = request.form.get('action')
        if not url:
            flash('Please enter a valid URL.', 'error')
        elif action == 'shorten':
            short_code = url_shortener.shorten(url)
            short_url = f'{request.host_url}{short_code}'
        elif action == 'generate_qr':
            filename = qr_generator.generate_qr_code(url)
            qr_code_file = filename
    return render_template('index.html', short_url=short_url, qr_code_file=qr_code_file)

@app.route('/qr_codes/<filename>')
def qr_file(filename):
    return send_from_directory('static/qr_codes', filename)

@app.route('/<short_code>')
def redirect_short_url(short_code):
    url = url_shortener.get_original_url(short_code)
    if url:
        return redirect(url)
    flash('Invalid short URL.', 'error')
    return redirect('/')

if __name__ == '__main__':
    url_shortener.init_db()
    app.run(debug=True)
