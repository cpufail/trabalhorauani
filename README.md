1)fizemos a ontovinicola que é um chatbot que ira retirar todas as suas duvidas sobre vinhos e espumantes, consegue ler imagens de vinhos e espumantes que o usuario colocar e quiser saber sobre

1)para fazer o chatbot baixamos o ollama com o ubuntu para ser linux, ultiliza-se este codigo no ubuntu >> curl -fsSL https://ollama.com/install.sh | sh<< para baixar o ollama logo em seguida usar o comando>>ollama pull lama3.1<< e >>ollama pull llava<< um para texto e outro para ler a imagem, logo apos isso só usar >>ollama run llama3.1<< para ver se esta funcionado, mas antes certifique-se se esta rodando o ollama por esse site>> http://localhost:11434/
depois disso deve-se baixar o chatboxai muito facil a instalação e nas definiçoes vc pode colocar algum prompt para focar em um ramo em especifico seleciona o ollama e o modelo ai depois é só se divertir com o chat.


2)para o nosso gerador de imagem ultilizamos este codigo>gerador de imagem[.py com a api da openai basicamente ele da um input pedindo que modelo de imagem vc quer gerar e logo em seguida ele gera a imagem .jpg 
a api foi integrada logo no inicio do codigo para poder rodar o processo

3)para gif usamos a api da openia só que juntamente com o docker
3)para fazer esta pag na web vc precisa ter o docker instalado e seguir o comando que tem neste link https://docs.openwebui.com/ , da para fazer com o ollama tambem, porem preferimos fazer com api que nos facilitou
a api foi integrada no comando docker 

4)fizemos um leitor de audio  voce ira precisar iniciar primeiro o text_generator.py para gerar um arquivo .txt que o leitorcaudio.py ira criar o audio em cima deste texto 
