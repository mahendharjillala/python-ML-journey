import ollama


print("type 'exit' to exit")

while True:
    user_input=input("enter: ")

    if user_input.lower()=="exit":
        break

    response=ollama.chat(
        model="llama3",
        messages=[
            {"role":"system","content":"You are a helpful AI assistant"},
            {"role":"user","content":user_input}
        ]
    )

    print(response['message']['content'])