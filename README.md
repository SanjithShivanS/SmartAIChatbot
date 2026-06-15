# SKASC Smart Assistant (SmartAIChatbot)

An intelligent, hybrid AI chatbot designed specifically for **Sri Krishna Arts and Science College (SKASC)**. The system dynamically resolves college-specific queries using a local pre-approved FAQ database, and seamlessly routes general inquiries to Google's Gemini LLM.

---

## 🚀 Key Features

- **Hybrid NLP Engine**: Utilizes local TF-IDF cosine similarity matching for precise, pre-approved FAQ answers. If similarity is below a certain threshold (e.g., `0.3`), the query is answered by **Google Gemini Flash** with college-specific persona context.
- **Contextual Multi-turn Memory**: Maintains context by remembering the last 3 message exchanges using Django sessions.
- **Modern Branded UI**: A responsive, full-screen interactive UI with Sri Krishna Arts and Science College branding (Yellow & Blue theme), quick-action buttons, and smooth typing animations.
- **Secure & Robust**: Powered by Django 5.x, backed by MySQL, and protected with environment-based secrets (like the Gemini API Key).
- **Audit Logging**: Every interaction is logged into a database table (`ChatLog`) for analytics, training, and administration purposes.

---

## 🛠️ Tech Stack

- **Backend**: Python, Django 5.x
- **Database**: MySQL
- **AI & NLP Engine**: Scikit-Learn (`TfidfVectorizer` + Cosine Similarity), Google Generative AI (`gemini-1.5-flash-latest` model)
- **Frontend**: HTML5, CSS3 (Custom theme), JavaScript (AJAX for asynchronous requests)
- **Configuration**: `python-dotenv` for secure environment variables

---

## 📂 Project Structure

```text
SmartAIChatbot/
│
├── chatbot/                # Chatbot application logic
│   ├── management/         # Management commands (e.g. data seeding)
│   ├── templates/          # HTML templates
│   ├── nlp_engine.py       # Local Matcher & Gemini Integrator
│   ├── models.py           # Database entities (Category, FAQ, ChatLog)
│   └── views.py            # Chat message routing and history manager
│
├── college_bot/            # Django project settings
│   ├── settings.py         # Global settings and database configs
│   └── urls.py             # Main routing registry
│
├── manage.py               # Django CLI management entry point
├── .env.example            # Template for required environment variables
├── .gitignore              # Ignored local runtime files
└── README.md               # Project documentation
```

---

## 💾 Database Schema (Entity-Relationship)

The system manages data with three main models:

1. **Category**: Defines domains of query types (e.g., Academics, Placements, Admissions).
2. **FAQ**: Contains custom-curated questions and answers linked to a category.
3. **ChatLog**: Stores audit logs for every query (user question, generated answer, and timestamp).

---

## ⚙️ Setup & Installation Instructions

Follow these steps to set up the project locally:

### 1. Clone & Navigate
```bash
git clone https://github.com/SanjithShivanS/SmartAIChatbot.git
cd SmartAIChatbot
```

### 2. Configure Virtual Environment
Create and activate a Python virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

Key packages include: `django`, `scikit-learn`, `mysqlclient`, `python-dotenv`, `google-generativeai`.

### 4. Setup Environment Variables
Create a file named `.env` in the root directory and configure the following variables:
```env
# Django Settings
SECRET_KEY=your_django_secret_key
DEBUG=True

# Database Configuration (MySQL)
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=127.0.0.1
DB_PORT=3306

# API Configuration
GEMINI_API_KEY=your_google_gemini_api_key
```

### 5. Apply Migrations & Seed Data
Run database migrations and seed the custom SKASC data:
```bash
python manage.py migrate
python manage.py seed_data
```

### 6. Run the Server
```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser to test the assistant!

---

## 🔮 Future Goals

- **Cloud Deployment**: Moving backend to *PythonAnywhere* and utilizing a cloud-managed MySQL instance.
- **Interactive Admin Analytics**: Building visual dashboards to analyze `ChatLog` trends and identify commonly asked queries.
