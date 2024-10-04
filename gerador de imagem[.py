import os
import requests
import openai
from PIL import Image
from dotenv import load_dotenv
from api_key import API_KEY


# Carregar variáveis de ambiente
load_dotenv()

# Definir a chave da API
openai.api_key = API_KEY

# Verifique se a chave da API foi carregada corretamente
if openai.api_key is None:
    raise ValueError("A chave da API não foi encontrada. Verifique o arquivo .env.")

# Definir o prompt
prompt = input('digite que imagem vc quer:')

# Gerar a imagem
resposta = openai.Image.create(
    model='dall-e-3',
    prompt=prompt,
    n=1,
    size='1024x1024'
)

# Baixar a imagem
image_url = resposta['data'][0]['url']
img_data = requests.get(image_url).content
with open('campo_pastagem.jpg', 'wb') as f:
    f.write(img_data)

# Mostrar a imagem
image = Image.open('campo_pastagem.jpg')
image.show()
