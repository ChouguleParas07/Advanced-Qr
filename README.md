# 🔗 URL Shortener & QR Generator

A simple Flask web app to shorten long URLs and generate downloadable QR codes. Built to be fast, minimal, and easy to deploy.

---

## ✨ Features

- Shorten long URLs into clean, shareable links
- Generate QR codes for any URL
- Faster and more reliable
- Download generated QR codes as image files
- Flash messages for validation and feedback

---

## 🛠️ Tech Stack

- Backend: Flask (Python)
- Storage: SQLite (via a simple URL shortener utility)
- QR: `qrcode` and `Pillow`
- Templating/Static: Jinja2, HTML, CSS

---

## 📦 Requirements

- Python 3.9+
- pip

Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Run Locally

```bash
# 1) Create & activate a virtual environment (recommended)
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Start the app
python app.py
```

The app will start in development mode with debug enabled. Open your browser at `http://127.0.0.1:5000/`.

---

## ▶️ Usage

1. Enter a valid URL in the input field.
2. Click "Shorten URL" to get a short link.
3. Click "Generate QR Code" to create and download a QR image.

---

## 📁 Project Structure

```text
QR-Generator/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── qr_codes/
└── utils/
    ├── __init__.py
    ├── qr_generator.py
    └── url_shortener.py
```

---

## 🔌 Endpoints

- `GET /` – Render the main page
- `POST /` – Handle URL shorten and QR generation actions
- `GET /qr_codes/<filename>` – Serve generated QR images
- `GET /<short_code>` – Redirect short URL to its original URL

---

## ⚙️ Configuration

- `app.secret_key` in `app.py` is set for flash messages. Replace `'change_me'` in production.

---

## 🧪 Notes

- Generated QR images are saved to `static/qr_codes/`.
- Short codes are managed by `utils/url_shortener.py`.

---

## 📄 License

MIT License

---

## 👤 Author

**paras**  
🔗 GitHub: https://github.com/<your-username>

---

> Built to make sharing easier and faster.
