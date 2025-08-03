📬 ML-Powered Email Sorter

A lightweight and intuitive Streamlit web app that automatically classifies raw email texts into meaningful categories using simple NLP-based keyword detection.

Paste multiple emails into the input box (each separated by a blank line), and the app will instantly sort them into:

💼 Work

📰 Newsletter

🚨 Spam

💬 Personal

🔍 Key Features
📩 Bulk paste support — handle multiple emails at once

🧠 Rule-based NLP logic — no heavy models required

🧾 Instant tagging with emojis for easy visual filtering

⚡️ Lightweight, fast, and beginner-friendly

🛠️ Built With
Python

Streamlit

Pandas

🚀 Getting Started

git clone https://github.com/yourusername/email-sorter.git
cd email-sorter
pip install -r requirements.txt
streamlit run app.py
💡 Example Input
Hey Team,
We have a project deadline this Friday..

Congratulations! You've won a free gift card...

Thanks for subscribing to our newsletter...

Hey bro, let's meet up this weekend...
📊 Output Preview
Email #	Category	Snippet
1	Work 💼	"Hey Team, We have a..."
2	Spam 🚨	"Congratulations! You've..."
3	Newsletter 📰	"Thanks for subscribing..."
4	Personal 💬	"Hey bro, let's meet..."

