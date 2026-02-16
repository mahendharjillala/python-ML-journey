import ollama
import re

def cal(exp):
    try:
        return str(eval(exp))
    except:
        return "Error in calculation."

def need_cal(exp):
    return bool(re.search(r"\d+\s*[\+\-\*\/]\s*\d+",exp))

print("Enter 'exit' to EXIT")

messages=[
    {"role":"system","content":"You are a helpFul AI assistant, if math needed calculate it"}
]

while True:
    user_input=input("Enter: ")
    if user_input.lower()=="exit":
        break
    if need_cal(user_input):
        result=cal(user_input)
        print("result(tool): ",result)
        continue
    messages.append({"role":"user","content":user_input})
    response=ollama.chat(
        model="llama3",
        messages=messages
    )
    ai_reply=response['message']['content']
    print("AI: ",ai_reply)
    messages.append({"role":"assistant","content":ai_reply})
