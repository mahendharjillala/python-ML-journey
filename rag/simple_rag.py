import ollama
import re

with open("knowledge.txt","r") as f:
    knowledge = f.read()

chunks=knowledge.split("\n")



def retrieve(query):
    query = re.sub(r"[^\w\s]", "", query.lower())

    for chunk in chunks:
        chunk_clean = chunk.lower()
        if any(word in chunk_clean for word in query.split()):
            return chunk

    return "No relevant information found."

print("RAG AI (type 'exit' to quit)\n")

while True:
    user_input=input("enter: ")

    if user_input.lower()=="exit":
        break

    context=retrieve(user_input)

    prompt=f"""
     Use the following information to answer the question
     context:{context}
     question:{user_input}
    """

    res=ollama.chat(
        model="llama3",
        messages=[{"role":"user" ,"content":prompt}]

    )
    print("AI:", res['message']['content'])
