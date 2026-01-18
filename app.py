import gradio as gr
import joblib
import pandas as pd


# Load the brain (model) and translator (encoder)
model = joblib.load('mental_health_model.pkl')
le = joblib.load('label_encoder.pkl')

def mental_health_assistant(age, gender, course, year, cgpa, married, depression, anxiety, panic):
    # Prepare the input for the model

    input_data = [age, gender, course, year, cgpa, married, depression, anxiety, panic]
    



    encoded_data = []
    for val in input_data:
        if isinstance(val, str):
            try:
                encoded_data.append(le.transform([val])[0])
            except:
                encoded_data.append(0)
        else:
            encoded_data.append(val)




    # Get the numeric prediction (0 or 1)
    prediction = model.predict([encoded_data])[0]


    # --- LOGIC FOR EMPATHETIC RESPONSES ---
    if prediction == 0:
        status = "STATUS: NORMAL (No significant anxiety detected)"
        message = "🌟 You are doing great! It seems you are managing your stress levels effectively."
        tips = "✅ **Relaxation Tip:** Continue practicing 'Box Breathing' (4 seconds in, 4 hold, 4 out) to maintain your focus."
    else:
        status = "STATUS: ANXIOUS (High stress levels detected)"
        message = "💙 It's okay to feel overwhelmed sometimes. Remember, your mental health is as important as your grades."
        tips = "✅ **Relaxation Tip:** Try a 5-minute walk or a 'Grounding' exercise (identify 5 things you see, 4 you feel, and 3 you hear)."

    final_output = f"{status}\n\n{message}\n\n{tips}\n\n✨ **Motivational Quote:** 'Success is not final, failure is not fatal: it is the courage to continue that counts.'"
    return final_output

# Create the UI
demo = gr.Interface(
    fn=mental_health_assistant,
    inputs=[
        gr.Number(label="Age"),
        gr.Dropdown(["Female", "Male"], label="Gender"),
        gr.Textbox(label="Course"),
        gr.Dropdown(["year 1", "year 2", "year 3", "year 4"], label="Year of Study"),
        gr.Number(label="CGPA"),
        gr.Dropdown(["No", "Yes"], label="Married?"),
        gr.Dropdown(["No", "Yes"], label="Depression?"),
        gr.Dropdown(["No", "Yes"], label="Anxiety?"),
        gr.Dropdown(["No", "Yes"], label="Panic Attacks?")
    ],
    outputs="text",
    title="Student Mental Health Assistant",
    description="Your mental well-being matters. Enter your details for an AI-based analysis and support."
)

demo.launch()
