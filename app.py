import string
import random
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from models import db, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create tables on first run
with app.app_context():
    db.create_all()


def generate_short_code(length=6):
    """Generate a random 6-character short code."""
    chars = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(chars, k=length))
        # Make sure it doesn't already exist in the DB
        if not URL.query.filter_by(short_code=code).first():
            return code


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form.get('url', '').strip()

        # Basic validation
        if not original_url:
            flash('Please enter a URL.', 'danger')
            return redirect(url_for('index'))

        if not original_url.startswith(('http://', 'https://')):
            original_url = 'https://' + original_url

        # Check if this URL was already shortened
        existing = URL.query.filter_by(original_url=original_url).first()
        if existing:
            flash('This URL was already shortened!', 'info')
            return render_template('index.html', short_url=request.host_url + existing.short_code)

        # Create new short URL
        short_code = generate_short_code()
        new_url = URL(original_url=original_url, short_code=short_code)
        db.session.add(new_url)
        db.session.commit()

        short_url = request.host_url + short_code
        flash('URL shortened successfully!', 'success')
        return render_template('index.html', short_url=short_url)

    return render_template('index.html')


@app.route('/<short_code>')
def redirect_url(short_code):
    """Redirect short URL to original and count the click."""
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if not url_entry:
        abort(404)

    url_entry.clicks += 1
    db.session.commit()
    return redirect(url_entry.original_url)


@app.route('/analytics/<short_code>')
def analytics(short_code):
    """Show analytics for a specific short URL."""
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if not url_entry:
        abort(404)
    return render_template('analytics.html', url=url_entry)


@app.route('/all')
def all_urls():
    """Show all shortened URLs."""
    urls = URL.query.order_by(URL.created_at.desc()).all()
    return render_template('all_urls.html', urls=urls)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)