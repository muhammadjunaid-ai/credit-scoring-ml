🏦 Credit Scoring ML App
Live Demo: https://muhammadjunaid.streamlit.app
Predict an individual’s creditworthiness using financial data with a Random Forest model and interactive Streamlit interface.
🔍 About the Project
Builds a credit scoring model to classify applicants as good or bad credit risks based on financial and personal attributes using a Random Forest classifier.
📂 Project Structure

credit-scoring-ml-project/
│
├─ model/
│   ├─ credit_model.pkl      # Trained model
│   ├─ mappings.pkl          # Categorical encodings
├─ dataset.csv               # Credit dataset
├─ train_model.py            # Train & save model
├─ app.py                    # Streamlit application
├─ requirements.txt          # Dependencies
└─ README.md
🧠 Model Overview
Algorithm: Random Forest Classifier
Encoding: Categorical mappings saved in mappings.pkl
Saved Model: credit_model.pkl
Prediction: Good or Bad credit risk
⚙️ Setup & Installation
Clone repository:
Bash
git clone https://github.com/muhammadjunaid-ai/credit-scoring-ml.git
cd credit-scoring-ml
Create & activate virtual environment:
Bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies:
Bash
pip install -r requirements.txt
🏗️ Training the Model
Bash
python train_model.py
Generates:
model/credit_model.pkl
model/mappings.pkl
🌐 Running the App
Bash
streamlit run app.py
Access locally: http://localhost:8501
🧪 How to Use the App
Select categorical fields: Status Account, Credit History, Purpose, Status Savings
Enter numeric values: Loan duration (months), Credit amount
Click Predict Creditworthiness
View result: Good or Bad
💡 Key Features
Interactive Streamlit UI
Live predictions with probability
Automatic handling of categorical mappings
Easy retraining & deployment
📌 Dependencies
pandas
scikit-learn
streamlit
joblib
Listed in requirements.txt
📜 Dataset Information
Columns:
status_account
month_duration
credit_history
purpose
credit_amount
status_savings
target (good/bad credit)
✨ Live App
https://muhammadjunaid.streamlit.app⁠
