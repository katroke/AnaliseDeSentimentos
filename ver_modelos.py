import json
from flask import Flask, request, render_template, jsonify

# Importa a biblioteca do Google Generative AI
import google.generativeai as genai

# Substitua pela sua API Key do Google AI Studio
genai.configure(api_key="AIzaSyDmHirV1y83ZPcDsSapjHbYrY6GIjXxKKA") 

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
        