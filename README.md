# Analisador de Sentimentos com IA Gemini

> Uma aplicação web que utiliza a API do Google Gemini para realizar análises de sentimento detalhadas em textos fornecidos pelo usuário.

Esta aplicação permite que os usuários insiram frases ou textos para receber uma análise completa, incluindo a classificação do sentimento geral, a intensidade de emoções específicas como alegria e tristeza, uma sugestão de resposta e uma explicação do modelo de IA.

## 🖼️ Screenshot
<img width="1900" height="896" alt="image" src="https://github.com/user-attachments/assets/3eb8c9ee-e9ae-4ba1-bded-77c3209eccb6" />

## ✨ Funcionalidades

  * **Análise em Tempo Real:** Envie um texto e receba a análise instantaneamente.
  * **Classificação Geral:** Identifica se o sentimento é **Positivo**, **Negativo** ou **Neutro**.
  * **Sentimentos Detalhados:** Fornece um detalhamento de emoções específicas (ex: Alegria, Confiança, Decepção) com barras de intensidade.
  * **Resposta Recomendada:** A IA sugere uma resposta apropriada com base no sentimento do texto.
  * **Histórico de Análises:** Todas as análises são salvas no navegador (`localStorage`), permitindo que você as revise mais tarde.
  * **Interface Limpa:** UI moderna e intuitiva para uma ótima experiência de usuário.

## 🛠️ Tecnologias Utilizadas

  * **Backend:**
      * [Python](https://www.python.org/)
      * [Flask](https://flask.palletsprojects.com/)
      * [Google Gemini API](https://ai.google.dev/)
  * **Frontend:**
      * HTML5
      * CSS3
      * JavaScript
  * **Bibliotecas:**
      * [jQuery](https://jquery.com/)

## 🚀 Como Executar o Projeto

Siga os passos abaixo para executar o projeto em sua máquina local.

#### 1\. Pré-requisitos

  * [Python 3.8+](https://www.python.org/downloads/)
  * [Git](https://git-scm.com/downloads)

#### 2\. Clone o Repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
cd SEU-REPOSITORIO
```

*Substitua `SEU-USUARIO/SEU-REPOSITORIO` pela URL do seu projeto.*

#### 3\. Crie e Ative um Ambiente Virtual

É uma boa prática isolar as dependências do projeto.

```bash
# Criar o ambiente
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ativar no macOS/Linux
source venv/bin/activate
```

#### 4\. Crie o Arquivo de Dependências

Crie um arquivo chamado `requirements.txt` na raiz do projeto e adicione o seguinte conteúdo:

```txt
Flask
google-generativeai
```

#### 5\. Instale as Dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

#### 6\. Configure sua Chave de API

Você precisa de uma chave de API do Google AI Studio para usar o modelo Gemini.

1.  Acesse o [Google AI Studio](https://aistudio.google.com/app/apikey).

2.  Crie uma nova chave de API.

3.  Abra o arquivo `gemini.py` e insira sua chave na linha indicada:

    ```python
    # gemini.py

    # Passo 1: Insira sua chave de API aqui
    genai.configure(api_key="SUA_CHAVE_DE_API_AQUI") # type: ignore
    ```

    **Atenção:** Para projetos sérios, é altamente recomendado usar variáveis de ambiente para proteger sua chave, em vez de colocá-la diretamente no código.

#### 7\. Execute a Aplicação

Finalmente, execute o servidor Flask:

```bash
flask run
```

Abra seu navegador e acesse [http://127.0.0.1:5000](https://www.google.com/search?q=http://127.0.0.1:5000) para ver a aplicação funcionando\!

-----

Depois de salvar este arquivo, faça o `add`, `commit` e `push` para enviá-lo ao seu GitHub. A página do seu repositório ficará muito mais profissional e informativa\!
