# 🤖 Chatbot – Generative AI ChatBot

A simple AI-powered chatbot built with **Streamlit**, **LangChain**, and **Groq LLMs**.
This project provides a clean chat interface where users can ask questions and receive AI-generated responses in real time.

---

## 🚀 Features

* Interactive chatbot UI using Streamlit
* Fast AI responses using Groq API
* Chat history support
* Environment variable support with `.env`
* Simple and beginner-friendly project structure

---

## 📂 Project Structure

```bash
.
├── chatbot.py          # Main Streamlit chatbot application
├── requirements.txt    # Project dependencies
├── env_template.txt    # Environment variable template
└── README.md           # Project documentation
```

---

## 🛠️ Technologies Used

* Python
* Streamlit
* LangChain
* Groq API
* Python Dotenv

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/chotu-chatbot.git
cd chotu-chatbot
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

Activate virtual environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

## 📥 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup Environment Variables

Create a `.env` file in the project root directory.

Copy content from `env_template.txt`:

```env
GROQ_API_KEY="your_api_key"
```

Replace `"your_api_key"` with your actual Groq API key.

---

## ▶️ Run the Application

```bash
streamlit run chatbot.py
```

---

## 💬 Example

Ask questions like:

* "What is Artificial Intelligence?"
* "Explain Python loops"
* "Write a simple SQL query"

---

## 📸 Preview

```text
🤖 CHOTU
Ask a question...
```

---

## 📌 Requirements

```txt
streamlit
python-dotenv
langchain-community
langchain-groq
```

---

## 🔮 Future Improvements

* Add memory support
* Add voice input/output
* Save chat history to database
* Multi-model support
* Dark mode UI

---

## 👨‍💻 Author
Abhishek Bhise

