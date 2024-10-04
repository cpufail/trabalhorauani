OBS: para gerar sua chave da OpenAI você deve acessar este site>>https://platform.openai.com/api-keys e fazer o cadastro, logo após isso terá que cadastrar também um cartão de crédito e colocar alguns créditos para rodar normalmente 

  

1)fizemos a ontovinicola que é um chatbot que irá retirar todas as suas dúvidas sobre vinhos e espumantes, consegue ler imagens de vinhos e espumantes que o usuário colocar e quiser saber sobre 

1)para fazer o chatbot baixamos o ollama com o ubuntu para ser Linux, utiliza-se este código no ubuntu >> curl -fsSL https://ollama.com/install.sh | sh<< para baixar o ollama logo em seguida usar o comando>>ollama pull lama3.1<< e >>ollama pull llava<< um para texto e outro para ler a imagem, logo após isso só usar >>ollama run llama3.1<< para ver se está funcionado, mas antes certifique-se se está rodando o ollama por esse site>> http://localhost:11434/ 
depois disso deve-se baixar o chatboxai muito fácil a instalação e nas definições você pode colocar algum prompt para focar em um ramo em específico seleciona o ollama e o modelo aí depois é só se divertir com o chat. 

  
2)para o nosso gerador de imagem utilizamos este código>gerador de imagem[.py com a api da OpenAI basicamente ele dá um input pedindo que modelo de imagem você quer gerar e logo em seguida ele gera a imagem .jpg a api foi integrada logo no início do código para poder rodar o processo 

  
3)para gif usamos a api da OpenAI só que juntamente com o Docker 
3)para fazer esta pág. na web você precisa ter o Docker instalado e seguir o comando que tem neste link https://docs.openwebui.com/ , dá para fazer com o ollama também, porém preferimos fazer com api que nos facilitou a api foi integrada no comando Docker  

4)fizemos um leitor de áudio, você irá precisar iniciar primeiro o text_generator.py para gerar um arquivo .txt que o leitorcaudio.py irá criar o áudio em cima deste texto 

 
