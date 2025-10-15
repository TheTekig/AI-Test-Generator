# Gerador de Testes com IA
Um script simples em Python que utiliza a API da OpenAI para gerar automaticamente casos de teste em pytest para funções Python.

***🎯 Objetivo do Projeto***

    Este projeto representa um dos meus primeiros estudos práticos integrando duas tecnologias fundamentais: a automação de testes com pytest e o poder de geração de código de Large Language Models (LLMs) através da API da OpenAI.
    
    O objetivo era explorar como a IA poderia acelerar o processo de desenvolvimento, criando uma ferramenta simples para auxiliar na criação de testes unitários e, ao mesmo tempo, aprofundar meus conhecimentos em engenharia de prompt.

***⚙️ Como Funciona***
    O usuário informa o nome de um arquivo .py que contém as funções a serem testadas.
    
    O script lê o conteúdo do arquivo.
    
    Este conteúdo é enviado para a API da OpenAI com um system prompt detalhado, instruindo a IA a agir como um engenheiro de software sênior especialista em testes.
    
    A IA retorna o código pytest completo, seguindo o padrão Arrange-Act-Assert e cobrindo diferentes cenários.
    
    O script salva os testes gerados em um novo arquivo padronizado na pasta tests/.

***🚀 Como Usar***
    Clone este repositório.
    
    Crie e ative um ambiente virtual:
    
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    .\venv\Scripts\activate   # Windows
    
    Instale as dependências:
    
    pip install -r requirements.txt
    
    Crie um arquivo .env na raiz do projeto e adicione sua chave da OpenAI:
    
    OPENAI_API_KEY="sua_chave_secreta_aqui"
    
    Execute o script:
    
    python gerador_testes.py
    
    Siga as instruções no terminal.

***⚠️ Nota de Aprendizado sobre Segurança***

    Esta foi uma das minhas primeiras implementações de integração com API. A versão inicial deste código continha uma falha de segurança crítica, onde a chave da API era colocada diretamente no código-fonte.
    
    Lição Aprendida: Nunca se deve expor credenciais ou segredos no código. A versão atual foi refatorada para utilizar a biblioteca python-dotenv, que carrega a chave de forma segura a partir de um arquivo .env local (que é ignorado pelo Git), seguindo as melhores práticas de desenvolvimento.
