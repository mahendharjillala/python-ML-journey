import ollama

response=ollama.chat(
    model="llama3",
    messages=[
        {"role":"system","content":"you are a heplful AI assistance"},
        {"role":"user","content":"explain linear regression in small words"}
    ]
)

print(response['message']['content'])