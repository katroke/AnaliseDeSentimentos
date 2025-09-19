## python gemini.py


import json
from flask import Flask, request, render_template, jsonify
import google.generativeai as genai

# Adicionado para configurar o timeout
from google.generativeai.types import GenerationConfig# type: ignore

# Passo 1: Insira sua chave de API aqui
genai.configure(api_key="SUA_API") # type: ignore

app = Flask(__name__)

try:
    model = genai.GenerativeModel('models/gemini-1.5-flash') # type: ignore # ou 'models/gemini-1.5-pro'
    print("Modelo Gemini inicializado com sucesso.")
except Exception as e:
    model = None
    print(f"ERRO: Não foi possível inicializar o modelo do Gemini. Verifique sua chave de API e instalação. Detalhe: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse', methods=['POST'])
def analyse():
    if not model:
        return jsonify({"error": "O modelo de IA não foi inicializado corretamente. Verifique o console do servidor."}), 500

    try:
        print("\n--- PONTO DE VERIFICAÇÃO 1: Servidor recebeu o pedido de análise.")
        
        frase = request.form.get('frase')
        if not frase:
            return jsonify({"error": "Nenhuma frase foi fornecida."}), 400

        prompt = f"""
        Analise o sentimento da seguinte frase: "{frase}"

        Retorne sua análise como um objeto JSON com a seguinte estrutura:
        - "classe": "positivo", "negativo", ou "neutro".
        - "sentimentos": Um objeto onde cada chave é um sentimento (ex: "Alegria") e seu valor é um objeto com "intensidade" (0-100) e "descricao" (uma frase curta).
        - "resposta_recomendada": Uma sugestão de resposta.
        - "explicacao_modelo": Uma breve explicação da sua análise.
        """
        
        print("--- PONTO DE VERIFICAÇÃO 2: Tentando contatar a IA (com timeout de 60 segundos)...")

        # Adiciona um timeout para evitar o carregamento infinito
        request_options = {"timeout": 60}
        
        response = model.generate_content( # type: ignore
            prompt,
            request_options=request_options# type: ignore
        )
        
        print("--- PONTO DE VERIFICAÇÃO 3: A IA respondeu com sucesso.")
        
        if not response.parts:
            print("--- ERRO: A resposta da IA veio vazia ou foi bloqueada.")
            return jsonify({"error": "A resposta da IA foi bloqueada ou retornou vazia. Tente outra frase."}), 500

        response_text = response.text.strip().replace("```json", "").replace("```", "")
        
        response_json = json.loads(response_text)
        
        print("--- PONTO DE VERIFICAÇÃO 4: Resposta processada e pronta para ser enviada.")
        return jsonify(response_json)

    except json.JSONDecodeError:
        print(f"--- ERRO: A IA retornou um texto que não é um JSON válido: {response_text}") # type: ignore
        return jsonify({"error": "A IA retornou um formato de dados inválido. Por favor, tente novamente."}), 500
    except Exception as e:
        print(f"--- ERRO INESPERADO: Ocorreu uma exceção: {e}")
        return jsonify({"error": f"Ocorreu um erro no servidor ao contatar a IA. Detalhe: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5050)