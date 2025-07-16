# 🩺 medvoice – Your Virtual Health Companion

Imagine walking into a clinic where the doctor greets you with warmth, listens carefully to your symptoms, examines your condition, and speaks back in a comforting voice — all in seconds.

That’s the experience **AI Doctor** aims to recreate.

---

## 🧠 What is AI Doctor?

**AI Doctor** is a multimodal AI-powered assistant that:
- Listens to your voice, transcribes your health concerns
- Looks at your medical image (e.g., a face with acne or swelling)
- Understands your symptoms and visuals using advanced LLMs
- Speaks back like a real doctor — calm, concise, and helpful

This is more than a chatbot. It's a voice- and vision-enabled healthcare companion.

---

## 🚀 Why This Project?

We built AI Doctor with one goal in mind:
> *To give users an intelligent, human-like interaction with technology in the context of healthcare.*

It’s built using:
- 🧠 **Groq LLMs** for fast and powerful reasoning
- 🎙️ **Whisper STT** for understanding your voice
- 🖼️ **Multimodal Vision Model** to interpret medical images
- 🔊 **gTTS / ElevenLabs** to talk back to you like a real doctor
- 🌐 **Gradio** to wrap it all in a simple, elegant web interface

---

## 🎯 How It Works – Behind the Scenes

1. **You speak.**  
   Your voice is recorded and sent to the **Whisper** model via **Groq** for transcription.

2. **You upload an image.**  
   It could be a facial image, skin condition, or visible symptom. We encode and analyze it with a **Groq multimodal LLM**.

3. **AI Doctor responds.**  
   The AI combines both inputs and generates a short, friendly medical explanation — almost like a real human doctor.

4. **You hear the result.**  
   Using **gTTS** or **ElevenLabs**, the AI voice speaks directly to you.

---

## 🛠️ Getting Started

### 🧬 Prerequisites
- Python 3.8+
- A mic and a webcam/image for input
- API key from [Groq](https://groq.com/)
- (Optional) API key from [ElevenLabs](https://www.elevenlabs.io/)

---

### 🚦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/ai-doctor.git
cd ai-doctor

# 2. Set up virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API keys
touch .env
Inside .env, add:


GROQ_API_KEY=your_groq_key_here
ELEVEN_API_KEY=your_elevenlabs_key_here  # Optional
🚀 Launch the App

python app.py
The interface will open in your browser at:
http://localhost:7860

🧾 File Structure
bash
Copy
Edit
ai-doctor/
├── app.py                  # Gradio app launcher
├── brain.py                # Image encoding + LLM response
├── voice_of_patient.py     # Voice recording + transcription
├── voice_of_doctor.py      # AI Doctor's voice output
├── requirements.txt
├── .env                    # API keys (keep it secret!)
└── README.md
```
🎥 Live in Action
Stay tuned for a short demo video showing the AI Doctor in real use.

https://github.com/user-attachments/assets/091b72cb-8322-4c79-8b2c-1ab2a2d3c14d


🙋🏻‍♀️ Made By
Mansi Arora
Data + AI enthusiast | Final-year B.Tech

⚠️ Disclaimer
This application is for educational and demonstration purposes only. It is not intended to diagnose, treat, or replace professional medical advice. Always consult a licensed healthcare provider.

💡 Future Plans
Add symptom-checker flow

Multilingual voice support

Better emotional tone in voice generation

Integration with real health databases
