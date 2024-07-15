from transformers import pipeline
from config.parametres import VERSIONS
from model.prompt import Prompt

def traduire(prompt:Prompt) :
    if prompt.version == VERSIONS[0] :
        translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")

    prompt.traduction = translator(prompt.atraduire)[0]['translation_text']
    with open('S:\École\ISEN\py-traducteur\query_log.txt', 'a') as file:
        file.write(f"{prompt}\n")
    return(prompt)