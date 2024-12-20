from groq import Groq

client = Groq()
models = client.models.list().data

print("Available Groq Models:")
for model in models:
    print(f"- {model.id}")
