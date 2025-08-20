from flask import Flask, request, render_template, redirect, url_for, flash
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong secret key for session security

scan_results = {}

def crawl_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return None, None, f"Error fetching URL: {e}"

    soup = BeautifulSoup(response.text, 'html.parser')

    inputs = soup.find_all('input')
    urls = [link.get('href') for link in soup.find_all('a', href=True)]
    return inputs, urls, None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form.get('url')
    if not url:
        flash("Please enter a URL to scan.", "error")
        return redirect(url_for('home'))

    inputs, urls, error = crawl_url(url)
    if error:
        flash(f"Failed to fetch URL: {error}", "error")
        return redirect(url_for('home'))

    # Simulated vulnerability detection (for demo - enhance with real logic)
    vulnerabilities = {
        'xss': 'No vulnerabilities found',
        'sqli': 'No vulnerabilities found',
        'csrf': 'No vulnerabilities found'
    }
    scan_results[url] = vulnerabilities

    # Render results with detected inputs, urls and vulnerabilities
    return render_template('results.html', target=url, inputs=inputs, urls=urls, results=vulnerabilities)

if __name__ == '__main__':
    app.run(debug=True)
