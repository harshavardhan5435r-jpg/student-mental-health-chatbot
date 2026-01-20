# 🤖 Student Mental Health Assistant

An AI-powered web application designed to help students identify and manage stress, anxiety, and depression. The system uses a **Neural Network (MLP Classifier)** to provide personalized mental health assessments and empathetic coping strategies.

---

## 📌 Project Overview
Academic pressure and personal challenges often lead to high stress among students. This project aims to provide an intelligent, private, and student-centric platform for early mental health detection using data-driven insights.

---

## ✨ Features
* 🧠 **AI-Based Stress Prediction**: Uses a trained model to categorize mental health status.
* 📝 **Instant Assessment**: A fast interface for students to check their well-being.
* 💡 **Personalized Wellness Tips**: Delivers specific advice based on the AI's findings.
* 🌐 **Cloud Deployment**: Hosted live on Hugging Face for 24/7 accessibility.
* 📱 **User-Friendly Interface**: Simple and clean UI built with Gradio.

---

## 🛠️ Tools & Technologies Used

| Component | Technology |
| :--- | :--- |
| **Frontend** | Gradio |
| **Backend** | Python |
| **AI Models** | Neural Network (MLP Classifier) |
| **Data Handling** | Pandas & Scikit-learn |
| **Deployment** | Hugging Face Spaces |

---
## 🧠 System Approach
The application follows a modular AI pipeline to ensure fast and accurate mental health assessments:

* **Step 1: Data Acquisition** 📝
    The system collects 9 specific inputs from the student, including age, academic year, CGPA, and emotional state (anxiety, panic, depression).
* **Step 2: Feature Encoding** ⚙️
    Raw text inputs (like "Engineering" or "Male") are transformed into numeric values using the **LabelEncoder** so the AI can process them.
* **Step 3: Neural Analysis (MLP)** 🤖
    The processed data is sent to a **Multilayer Perceptron (MLP)** Neural Network. This "brain" analyzes the complex relationship between academic pressure and emotional health to make a prediction.
* **Step 4: Empathetic Output** ✨
    Based on the result (0 or 1), the system generates a tailored response including a stress level assessment and specific motivational tips.

​
---

## 📂 Project Structure
Below is the organization of the repository. Each file serves a critical role in the deployment of the AI assistant:

```text
student-mental-health-chatbot/
├── 📄 app.py                   # Main logic & Gradio interface
├── 🧠 mental_health_model.pkl   # The trained MLP Classifier "Brain"
├── 🏷️ label_encoder.pkl        # Data translator for student inputs
├── 📦 requirements.txt         # Library dependencies (Scikit-learn, Gradio, etc.)
├── 📊 Student Mental health.csv # The dataset used for model training
├── 📓 project_notebook.ipynb    # Google Colab code used for development
└── 📘 README.md                # Project documentation & overview

---

