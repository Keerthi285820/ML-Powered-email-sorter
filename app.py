import streamlit as st
import pandas as pd

# Simple keyword-based classifier function
def classify_email(text):
    text = text.lower()
    if any(word in text for word in ["offer", "win", "click", "free", "urgent"]):
        return "Spam 🚨"
    elif any(word in text for word in ["meeting", "project", "deadline", "team", "update"]):
        return "Work 💼"
    elif any(word in text for word in ["unsubscribe", "newsletter", "subscription", "promo"]):
        return "Newsletter 📰"
    else:
        return "Personal 💬"

# Streamlit UI
st.title("📬 ML-Powered Email Sorter")
st.write("Paste multiple emails below (each separated by a blank line):")

user_input = st.text_area("📩 Enter Emails:", height=300)

if st.button("Sort Emails"):
    emails = [e.strip() for e in user_input.split('\n\n') if e.strip()]
    
    if not emails:
        st.warning("Please enter at least one email.")
    else:
        results = []
        for i, email in enumerate(emails, 1):
            label = classify_email(email)
            results.append({"Email #": i, "Category": label, "Text": email[:100] + "..."})
        
        st.success("Emails classified successfully!")
        df = pd.DataFrame(results)
        st.dataframe(df)
