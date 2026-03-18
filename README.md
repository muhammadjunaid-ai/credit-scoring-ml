# 🏦 Credit Scoring ML App

https://muhammadjunaid.streamlit.app

An AI-powered application that predicts an individual’s **creditworthiness** using financial data. The app classifies applicants as **good** or **bad credit risks** using **Random Forest** and provides an interactive **Streamlit web interface**.  

---

## 🔹 Features

- Predicts creditworthiness based on financial history  
- Handles both **categorical and numerical features** automatically  
- Displays probability and classification (**Good/Bad**)  
- Interactive **Streamlit web interface** for easy input  
- Can be extended to include more financial features or datasets  

---

## 🛠 Technologies Used

- **Python** – Core programming language  
- **Pandas** – Data preprocessing and management  
- **Scikit-learn** – Random Forest model & preprocessing  
- **Joblib** – Saving model and mappings  
- **Streamlit** – Web app interface  

---

## 📂 Project Structure

```text
credit-scoring-ml-project/
│
├─ model/
│   ├─ credit_model.pkl      # Trained Random Forest model
│   ├─ mappings.pkl          # Encodings for categorical features
├─ dataset.csv               # Credit dataset
├─ train_model.py            # Script to train the model
├─ app.py                    # Streamlit application
├─ requirements.txt          # Python dependencies
└─ README.md                 # Project documentation

## Author
Muhammad Junaid
BS Artificial Intelligence
GitHub: https://github.com/muhammadjunaid-ai
