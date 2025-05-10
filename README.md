# 🔐 Secure Access Flow

A clean and fully functional OAuth2 authentication demo built with Django and deployed on Railway. This project showcases modern login flows with proper production deployment practices and secure handling of credentials.

## 🚀 Live Demo

🌐 [https://secureaccessflow-production.up.railway.app](https://secureaccessflow-production.up.railway.app)

---

## ⚙️ Technologies Used

- **Backend**: Django 5.2 (Python 3.11)
- **Authentication**: Google OAuth2 via `social-auth-app-django`
- **Frontend**: Classic Django Templating (HTML/CSS)
- **Deployment**: Railway
- **Static Files**: WhiteNoise
- **Version Control**: Git + GitHub

---

## ✨ Key Features

- Google OAuth 2.0 authentication flow
- Secure credential management via environment variables
- Deployed with HTTPS and CSRF protection enabled
- Minimalist welcome screen with user profile integration
- Proper use of `SECURE_PROXY_SSL_HEADER`, `ALLOWED_HOSTS`, and `SECURE_SSL_REDIRECT`

---

## 🧠 Challenges Encountered

- OAuth 400/401 errors due to mismatched or malformed redirect URIs
- Improperly quoted environment variables causing `JSONDecodeError`
- `AuthCanceled` exceptions due to missing token or invalid session state
- Railway auto-wrapping values in quotes during ENV injection
- Debugging OAuth errors without full production traceback visibility

---

## ✅ Solutions Applied

- Ensured all `redirect_uri` values matched exactly in Google Cloud Console
- Used `json.loads()` to safely parse JSON-style ENV arguments
- Moved critical settings directly into `settings.py` to avoid ENV parsing issues
- Clean separation of development and production variables
- Manual redeploys triggered via empty commits after ENV updates

---

## 🧪 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/yourusername/secure-access-flow.git
cd secure-access-flow

# Set up virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add your .env variables
touch .env
# Fill in GOOGLE_OAUTH2_CLIENT_ID, GOOGLE_OAUTH2_CLIENT_SECRET, etc.

# Run migrations and start the server
python manage.py migrate
python manage.py runserver
secure_access_flow/
├── auth_demo/                  # Main authentication app
├── templates/                  # HTML templates
├── static/                     # Static files (if used)
├── secure_access_flow/        # Project settings
├── manage.py
└── requirements.txt
🤝 License
This project is open source and available under the MIT License.

💬 Author
Developed by Half-Half Man,
Synthesis of Code and Water.

🔗 Portfolio Website - TBA
📧 nmihajlovic.dev@gmail.com
