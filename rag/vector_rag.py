import ollama
from sentence_transformers import SentenceTransformer
import numpy as np

model=SentenceTransformer('all-MiniLM-L6-v2')

with open("knowledge.txt","r") as f:
    knowledge=f.read()

chunks=knowledge.split("\n")

chunk_embeddings=model.encode(chunks)

def retrieve(exp):
    exp_embeddings=model.encode([exp])[0]
    similarities=np.dot(chunk_embeddings,exp_embeddings)
    best_index=np.argmax(similarities)
    return chunks[best_index]

print("Vector RAG AI (type 'exit' to quit)\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    context = retrieve(question)

    prompt = f"""
Use the following information to answer the question.

Context:
{context}

Question:
{question}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    print("AI:", response['message']['content'])



