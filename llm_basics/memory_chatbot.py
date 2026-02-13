from pyexpat.errors import messages

import ollama



print("--------type 'exit' to exit-----")

messages = [
    {"role": "system", "content": "You are a helpful AI assistant."}
]

while True:
    user_input=input("enter: ")

    if user_input.lower()=="exit":
        break

    messages.append({"role":"user","content":user_input})

    response=ollama.chat(
        model="llama3",
        messages=messages
    )

    reply=response['message']['content']

    print(reply)

    messages.append({"role":"system","content":reply})