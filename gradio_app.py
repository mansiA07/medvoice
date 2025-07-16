import os
import gradio as gr

from brain import encode_image, analyze_image_with_query
from voice_of_the_patient import transcribe_with_groq
from voice_of_doctor import text_to_speech_with_gtts  # or use text_to_speech_with_elevenlabs

system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
What's in this image?. Do you find anything wrong with it medically? 
If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
Donot say 'In the image I see' but say 'With what I see, I think you have ....'
Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""

def process_inputs(audio_filepath, image_filepath):
    try:
        # Transcribe the patient's voice
        transcription = transcribe_with_groq(
            GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
            audio_filepath=audio_filepath,
            stt_model="whisper-large-v3"
        )
    except Exception as e:
        print("❌ Transcription failed:", e)
        transcription = "Sorry, I couldn't understand your voice input."

    try:
        # Generate doctor's response from image + query
        if image_filepath:
            doctor_response = analyze_image_with_query(
                query=system_prompt + transcription,
                encoded_image=encode_image(image_filepath),
                model="meta-llama/llama-4-scout-17b-16e-instruct"
            )
        else:
            doctor_response = "No image provided for me to analyze."
    except Exception as e:
        print("❌ Image analysis failed:", e)
        doctor_response = "I'm unable to analyze the image."

    # Convert text to voice (using gTTS or ElevenLabs)
    output_audio_path = "final.mp3"
    try:
        text_to_speech_with_gtts(input_text=doctor_response, output_filepath=output_audio_path)
    except Exception as e:
        print("❌ TTS failed:", e)
        output_audio_path = None

    # Verify audio file exists
    if not output_audio_path or not os.path.exists(output_audio_path) or os.path.getsize(output_audio_path) == 0:
        print("⚠️ Warning: final.mp3 is missing or empty.")
        output_audio_path = None

    return transcription, doctor_response, output_audio_path


# Gradio Interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(label="Doctor's Voice")
    ],
    title="AI Doctor with Vision and Voice"
)

iface.launch(debug=True)
