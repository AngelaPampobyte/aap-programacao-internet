## Sobre
Aqui vou deixar anotações minhas ao longo dos estudos, para fixar e poder consultar posteriormente

## Outras anotações
Também posso retornar uma página html na própria função, ao acessar a rota. Só escrever entre """ """
Fiz um pequeno teste, e consigo usar a tag <a> para navegar entre as rotas que criei na aplicação! até então eu havia usado apenas para acesso de arquivos salvos

## Anotações de comandos!

- comando para rodar: python -m flask --app app run --debug
- acessar 127.0.0.1:5000 (endereço que apareceu pós o comando ser executado)


Nessa aula estamos estudando estrutura básica, e realizando a instalação do microframework necessário.
Ao acessar o endereço, já receberemos o return da função inicio().

- @app.route("/sobre")
agora vamos criar mais algumas rotas para o arquivo do backend. Muito mais simples do que esperava e vi em outras linguagens! 
Basta apenas nomear as rotas e criar funções de retorno para cada uma, este é o mais básico, por enquanto.
Para acessar, basta colocar o nome que eu criei após o endereço

# Parâmetros de rota: 
Dentro do endereço da rota e do parâmetro posso, posso já definir o tipo da variável de entrada, para converter automaticamente a informação recebida. Isso provavelmente já evita erros
exemplo:
app.route("/media/<float:nota1:>/<float:nota2>")

(os testes estão sendo feitos por enquanto inserindo os dados diretamente ao link)

## problemas:
Um pequeno detalhe no tipo da variavel. Por colocar o tipo "float" ele não aceita qualquer valor que não possua .0 ou qualquer número