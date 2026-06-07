# 🚀 OptiCode-AI

An AI-powered Data Structures & Algorithms solver built with **Streamlit** and **Groq (LLaMA 3.3 70B)**. Paste any DSA problem and instantly get a brute force solution, optimal solution, complexity analysis, code translation, and a solution review.


<img width="1825" height="898" alt="Screenshot 2026-06-07 144659" src="https://github.com/user-attachments/assets/f03b1a7e-51ad-4214-b401-d63ac78eaa91" />


---

## ✨ Features

| Feature | Description |
|---|---|
| 📊 Problem Classification | Detects topic, pattern, and difficulty |
| 🔥 Brute Force Solution | Most straightforward approach with explanation |
| 🚀 Optimal Solution | Best algorithm with full explanation |
| ⚡ Complexity Analysis | Time and Space complexity of optimal solution |
| 🔍 Solution Review | Checks if a better algorithm exists |
| 🌍 Code Translator | Translates solution to any supported language |
| 💾 History | All solutions saved to local SQLite database |

---

## 🗂️ Project Structure

```
dsa_solver/
│
├── app.py                  # Main Streamlit app
├── p1.py                   # DB test script
├── test.py                 # API connectivity test
├── requirements.txt
├── .env                    # Your API key goes here
│
├── agents/                 # AI agent modules
│   ├── classifier.py       # Classifies topic, pattern, difficulty
│   ├── brute_force.py      # Generates brute force solution
│   ├── optimal.py          # Generates optimal solution
│   ├── complexity.py       # Analyzes time & space complexity
│   ├── reviewer.py         # Reviews solution quality
│   └── translator.py       # Translates code to other languages
│
├── services/
│   ├── gemini_service.py   # Groq API client (LLaMA 3.3 70B)
│   └── prompts.py          # All prompt templates
│
├── utils/
│   └── helpers.py          # Utility functions & language list
│
└── database/
    ├── db.py               # SQLite database manager
    └── history.db          # Auto-created on first run
```

---

## ⚙️ Setup & Installation

### 1. Clone or Download the Project

```powershell
cd C:\Users\YourName\Desktop
# Extract the zip folder here
cd dsa_solver
```

### 2. Create Virtual Environment

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Get a Free Groq API Key

1. Go to **https://console.groq.com/keys**
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the key — it starts with `gsk_`

### 5. Add API Key to `.env`

Open the `.env` file and replace the placeholder:

```
GROQ_API_KEY=gsk_your_actual_key_here
```

### 6. Run the App

```powershell
streamlit run app.py
```

The app will open automatically at **http://localhost:8501**

---

## ✅ Test Your Setup

Before running the full app, verify your API key works:

```powershell
python test.py
```

Expected output:
```
STEP 1: Loading .env file... Key found: True
STEP 2: Importing Groq... OK
STEP 3: Creating Groq client... OK
STEP 4: Sending test message... Response: WORKING
✅ GROQ IS WORKING!
```

---

## 🖥️ Supported Languages

- Python
- C++
- C
- Java
- JavaScript
- Go
- Rust

---

## 🧠 How It Works

1. You enter a DSA problem in plain English
2. **ClassifierAgent** detects the topic, pattern, and difficulty
3. **BruteForceAgent** generates the naive solution
4. **OptimalAgent** generates the best known algorithm
5. **ComplexityAgent** analyzes time and space complexity
6. **ReviewerAgent** checks if an even better solution exists
7. **TranslatorAgent** converts the solution to any language
8. Everything is saved to a local SQLite database

---

## 🛠️ Troubleshooting

| Problem | Fix |
|---|---|
| `GROQ_API_KEY not found` | Make sure `.env` file exists and has your key |
| `Client.__init__() got unexpected argument 'proxies'` | Run `pip uninstall groq httpx -y` then `pip install groq==0.13.0` |
| Blank output / no results | Run `python test.py` to diagnose the exact error |
| `ModuleNotFoundError` | Make sure venv is activated and `pip install -r requirements.txt` was run |

---

## 📦 Dependencies

```
streamlit==1.49.1
groq==0.13.0
python-dotenv==1.1.1
pydantic==2.11.7
pandas==2.3.2
sqlalchemy==2.0.43
markdown==3.9
pygments==2.19.2
```

---

## 📄 License

This project is for educational purposes.
