import openai
import re
from api_key import API_KEY

openai.api_key = API_KEY

# Defina o modelo a ser usado
model_engine = "gpt-3.5-turbo"  # Atualize para gpt-3.5-turbo ou gpt-4 se você tiver acesso

# Defina o prompt para gerar texto
text = input("sobre qual topico voce quer escutar?: ")
prompt = text

print("O BOT DE IA está tentando gerar um novo texto para você...")

# Gere texto usando o modelo GPT-3.5 ou GPT-4
try:
    completions = openai.ChatCompletion.create(
        model=model_engine,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024,
        n=1,
        temperature=0.5,
    )
    generated_text = completions.choices[0].message['content']
except Exception as e:
    print(f"Erro ao gerar texto: {e}")
    exit()

# Salve o texto em um arquivo
with open("generated_text.txt", "w") as file:
    file.write(generated_text.strip())

print("O texto foi gerado com sucesso!")
