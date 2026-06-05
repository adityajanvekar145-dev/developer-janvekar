# Password Generator Web App

A modern web-based password generator built with Flask and deployed on Heroku.

## Features

✅ Generate strong passwords with:
- Uppercase letters (A-Z)
- Lowercase letters (a-z)
- Numbers (0-9)
- Special characters (!@#$%^&*)

✅ Customizable password length (4-128 characters)
✅ Copy to clipboard functionality
✅ Responsive design
✅ Beautiful UI with gradient styling

## Local Setup

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/adityajanvekar145-dev/developer-janvekar.git
cd developer-janvekar
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and visit: `http://localhost:5000`

## Deployment

### Deploy to Heroku

1. **Create a Heroku account** at https://www.heroku.com

2. **Install Heroku CLI** from https://devcenter.heroku.com/articles/heroku-cli

3. **Login to Heroku:**
```bash
heroku login
```

4. **Create a new Heroku app:**
```bash
heroku create your-app-name
```

5. **Add secrets for GitHub Actions** (if using CI/CD):
   - Go to your GitHub repo → Settings → Secrets and variables → Actions
   - Add `HEROKU_API_KEY` (get from Heroku account settings)
   - Add `HEROKU_APP_NAME` (your app name)

6. **Deploy manually:**
```bash
git push heroku main
```

Or use GitHub Actions for automatic deployment on every push.

### Deploy with Docker

```bash
docker build -t password-generator .
docker run -p 5000:5000 password-generator
```

### Deploy to AWS

1. Use AWS Elastic Beanstalk
2. Use AWS EC2 with Docker
3. Use AWS Lambda with Zappa

### Deploy to Google Cloud

```bash
gcloud app deploy
```

### Deploy to Azure

```bash
az webapp up --name password-generator
```

## File Structure

```
developer-janvekar/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── Procfile               # Heroku configuration
├── .github/
│   └── workflows/
│       └── deploy.yml     # GitHub Actions CI/CD
└── templates/
    └── index.html         # Web UI
```

## Technology Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Heroku, Docker, GitHub Actions

## License

This project is open source and available under the MIT License.

## Author

Created by [@adityajanvekar145-dev](https://github.com/adityajanvekar145-dev)
