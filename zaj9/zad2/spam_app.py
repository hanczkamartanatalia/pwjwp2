import gradio as gr
import joblib

model = joblib.load("spam_classifier.pkl")


def predict_spam(text):
    prediction = model.predict([text])[0]
    return "📨 NIE-SPAM" if prediction == 0 else "🚫 SPAM"


demo = gr.Interface(
    fn=predict_spam,
    inputs=gr.Textbox(lines=6, placeholder="Wklej wiadomość e-mail tutaj..."),
    outputs=gr.Label(),
    title="📧 Klasyfikator E-maili (Spam Detection)",
    description="Model klasyfikuje wiadomości jako SPAM lub NIE-SPAM"
)

demo.launch()
