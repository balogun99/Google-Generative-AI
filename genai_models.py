import google.generativeai as genai

genai.configure(api_key="AIzaSyB54iz4Y8-3hkCaE0HHKkt2YSADwMjSuEM")
models = genai.list_models()

for model in models:
    print(model.name, model.supported_generation_methods)
