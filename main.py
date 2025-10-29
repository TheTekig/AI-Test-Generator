from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

try:
    Client = OpenAI(api_key=api_key)
except Exception as e:
    print("ERRO: Interrupção da conexão com OpenAI key - ", e)
def get_response(message,qtdTestes,valorToken):

    """ Função recebe o código da função para criação do pytest """

    system_prompt= (
                    "Você é um engenheiro de software sênior especialista em testes com pytest. Sua tarefa é criar testes completos e robustos para a função Python do usuário."

                    "\n\n### REGRAS INDISPENSÁVEIS ###"

                    "\n1. **IMPORTAÇÃO:** Sempre comece importando a função a ser testada do módulo 'main_app'. O nome da função é '{function_name}'."

                    "\n2. **ESTRUTURA AAA:** Para cada teste, siga RIGOROSAMENTE o padrão Arrange-Act-Assert:"

                     "\n   - **# Arrange:** PRIMEIRO, declare TODAS as variáveis de entrada e os resultados esperados. Nenhuma variável pode ser usada sem ser declarada nesta etapa."
                     "\n   - **# Act:** SEGUNDO, execute a função com as variáveis de entrada que você preparou."
                     "\n   - **# Assert:** TERCEIRO, use 'assert' para comparar o resultado da execução com o resultado esperado."

                    "\n3. **COBERTURA:** Crie testes para diferentes cenários: um caso de sucesso com dados típicos, um com dados extremos (ex: números negativos, listas vazias) e um teste para verificar se os erros esperados (Exceptions) são levantados corretamente (usando `pytest.raises`)."

                    "\n4. **SAÍDA LIMPA:** Retorne APENAS o código Python puro. Não inclua a função original, explicações, ou marcadores de markdown como ```python."

                    "\n5. O Arquivo que ira procurar é um python, logo ao importar utilize somente o nome do arquivo"

                    f"\n6. Faça no maximo {qtdTestes} testes"
                    "\n7. Não aceite outras respostas que não forem codigos"
                    "##EXEMPLO DE CODIGO##"
                    "from main import somar"
                    "import pytest"

                    "def test_somar_success():"
                        "# Arrange"
                        "a = 5"
                        "b = 3"
                        "expected = 8"
                        "# Act"
                        "result = somar(a, b)"
                        "# Assert"
                        "assert result == expected")

    try:
        response = Client.chat.completions.create(
            model="gpt-4o-mini",
            messages=
                [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message},
                ],
            max_tokens= valorToken
        )

    except Exception as e:
        print("ERROR: Não foi Possivel Escrever os Testes -", e)
        return None

    return response.choices[0].message.content

def add_test_to_file(test_code):
    """ Função recebe o teste feito pelo gpt -4o e adiciona ele aos testes """
    try:

        file_path = os.path.join( "Test", "test_function.py")
        os.makedirs("Test", exist_ok=True)

    except Exception as e:
        print("ERROR: Problema ao Salvar -",e)
        return None

    try:

        with open(file_path, "a") as file:
            file.write("\n\n")
            file.write(test_code)

    except Exception as e:
        print(f"ERROR: Não foi possivel a escrita em {file_path} - ",e)
        return None

    return True

def main():
    """ Função principal """

    """ Função a ser testada """
    token = 200

    function_to_test = "(Nome do arquivo = main.py)"
    function_to_test += input("Cole o seu código aqui abaixo:\n>")

    qtdTestes = input("Quantos Testes Serão Feitos? ")
    qtdTestes = int(qtdTestes)

    if qtdTestes > 3:
        token = qtdTestes * 100

    pytest_code = get_response(function_to_test, qtdTestes, token)

    result = add_test_to_file(pytest_code)

    if result:
        print("Teste adicionado com sucesso!")
    else:
        print("Erro ao adicionar o teste.")


if __name__ = "__main__": 
    main()

