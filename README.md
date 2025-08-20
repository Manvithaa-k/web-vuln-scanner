```markdown
# Web Application Vulnerability Scanner

## Project Overview
This project is a Python-based Web Application Vulnerability Scanner designed to detect common security vulnerabilities such as Cross-Site Scripting (XSS), SQL Injection (SQLi), and Cross-Site Request Forgery (CSRF) in web applications. It leverages the OWASP Top 10 checklist to provide a comprehensive security audit.

## Motivation
With the increasing number of web applications, security vulnerabilities pose critical risks. This tool aims to help developers and security professionals identify and understand vulnerabilities early in the development cycle, ensuring safer applications.

## Features
- Crawl input fields and URLs using Python `requests` and `BeautifulSoup`
- Inject payloads to test for XSS, SQLi, and CSRF vulnerabilities
- Pattern matching and regex to analyze responses for potential threats
- Flask web UI for easy management of scans and viewing detailed reports
- Logs each vulnerability with evidence and severity for audit purposes

## Tools & Technologies Used
- Python 3.x
- requests
- BeautifulSoup
- Flask (for the web interface)
- OWASP Top 10 Vulnerability Checklist

## Project Structure
```
/web-vuln-scanner
│
├── app.py                  # Main Flask application
├── scanner.py              # Core scanning logic
├── templates/              # HTML templates for Flask UI
│   ├── index.html
│   └── results.html
├── static/                 # Static files (CSS, JS if any)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Installation & Setup

1. **Clone the repository:**

```
git clone https://github.com/Manvithaa-k/web-vuln-scanner.git
cd web-vuln-scanner
```

2. **Create and activate a virtual environment (recommended):**

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install required packages:**

```
pip install -r requirements.txt
```

4. **Run the Flask app:**

```
python app.py
```

5. **Access the web interface:**
Open your browser and go to `http://127.0.0.1:5000/`

## Usage
- Enter the target URL in the web interface.
- Select the types of vulnerabilities to scan.
- Review the generated detailed report with evidence and severity.
- Use report logs for auditing and remediation.

## How to Contribute
Contributions are welcome! Please follow these steps:
- Fork the repository
- Create a new branch for your feature/fix
- Make your changes and commit with clear messages
- Submit a pull request describing your changes

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Project Report
See the [Project Report](./docs/Project_Report.pdf) for detailed documentation.

---

*Developed by Manvithaa-k as part of internship project*
```
