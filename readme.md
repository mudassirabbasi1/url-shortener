# URL Shortener

A Flask URL shortener with redirect handling, click tracking, and simple analytics pages. It is built as a compact full-stack project that demonstrates routing, persistence, and server-rendered UI.

## Features

- Shorten long URLs into compact shareable links.
- Redirect short links to their original destination.
- Track click counts for each short link.
- View link analytics and all stored URLs.
- Use a responsive Bootstrap-based interface.

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Bootstrap 5

## Run Locally

```bash
git clone https://github.com/mudassirabbasi1/url-shortener.git
cd url-shortener
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Project Structure

```text
url-shortener/
├── app.py
├── models.py
├── requirements.txt
├── static/
└── templates/
```
