import openai
import re
import os
from gtts import gTTS
from api_key import API_KEY

openai.api_key = API_KEY

# Ler o arquivo de texto
with open("generated_text.txt", "r") as file:
    text = file.read()

# Dividir o texto em parágrafos e concatenar em uma única string
paragraphs = re.split(r"[,.]", text)
full_text = ' '.join(para.strip() for para in paragraphs if para.strip())

# Criar a pasta necessária para o áudio
os.makedirs("audio", exist_ok=True)

# Criar áudio a partir do texto completo
if full_text:  # Verifica se o texto não está vazio
    tts = gTTS(text=full_text, lang='pt', slow=False)
    tts.save("audio/voiceover.mp3")
else:
    print("O texto está vazio, não é possível criar o áudio.")

print("O áudio foi gerado com sucesso!")
