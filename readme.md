# SnipURL — Flask URL Shortener

A full-stack URL shortener built with Python and Flask. Paste any long URL and get a short, shareable link with built-in click analytics.

## Features

- Shorten any URL instantly
- Redirect short links to original URLs
- Click tracking — see how many times each link was visited
- Analytics page per link (clicks, creation date, original URL)
- All links dashboard
- Clean, responsive UI with Bootstrap 5

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite (via Flask-SQLAlchemy)
- **Frontend:** HTML, Bootstrap 5
- **Deployment:** Render.com

## Run Locally

```bash
git clone https://github.com/mudassirabbasi1/url-shortener.git
cd url-shortener
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000` in your browser.

## Project Structure

```
url-shortener/
├── app.py              # Flask app and routes
├── models.py           # SQLite database model
├── requirements.txt    # Dependencies
├── templates/
│   ├── base.html       # Base layout
│   ├── index.html      # Homepage
│   ├── analytics.html  # Link stats
│   ├── all_urls.html   # All links
│   └── 404.html        # Error page
└── static/
    └── style.css       # Custom styles
```

## Live Demo

[View live on Render →](https://your-app.onrender.com)

---

Built by [Mudassir Ahmed](https://mudassirabbasi1.github.io) · Karachi, Pakistan
