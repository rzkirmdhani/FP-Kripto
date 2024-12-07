from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os
import time
from encryption_module import encrypt_with_tent_map, encrypt_with_logistic_map, decrypt_file  # Simulasi modul enkripsi dan dekripsi

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    file = request.files['pdf']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Encryption
        tent_start = time.time()
        tent_enc_file = encrypt_with_tent_map(filepath, app.config['OUTPUT_FOLDER'])
        tent_end = time.time()

        logistic_start = time.time()
        logistic_enc_file = encrypt_with_logistic_map(filepath, app.config['OUTPUT_FOLDER'])
        logistic_end = time.time()

        return render_template(
            'index.html',
            tent_time=tent_end - tent_start,
            logistic_time=logistic_end - logistic_start,
            enc_filename=os.path.basename(logistic_enc_file)
        )

@app.route('/decrypt', methods=['POST'])
def decrypt():
    file = request.files['enc_pdf']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Decryption
        dec_start = time.time()
        dec_file = decrypt_file(filepath, app.config['OUTPUT_FOLDER'])
        dec_end = time.time()

        return render_template(
            'index.html',
            dec_time=dec_end - dec_start,
            dec_filename=os.path.basename(dec_file)
        )

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

