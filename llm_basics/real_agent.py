import ollama

def calculator(exp):
    try:
        return str(eval(exp))
    except:
        return "error in calculation"

SYSTEM_PROMPT = """
You are an AI agent.

You have access to a tool:

TOOL: calculator
Use it when math calculations are needed.

When you want to use the tool, reply EXACTLY like this:

USE_TOOL: calculator
INPUT: <math expression>

Otherwise reply:

FINAL_ANSWER: <your answer>
"""

messages=[{"role":"system","content":SYSTEM_PROMPT}]

print("Real AI Agent (type 'exit' to quit)\n")
while True:
    user_input=input("enter 'exit' to EXIT")

    if user_input.lower()=="exit":
        break

    messages.append({"role":"user","content":user_input})

    response=ollama.chat(
        model="llama3",
        messages=messages

    )
    reply=response['message']['content']

    print("Ai reply",reply)

    if "USE_TOOL" in reply:
        expression = reply.split("INPUT:")[1].strip()
        result=calculator(expression)

        print("AI (Tool Used):", result)

        messages.append({"role": "assistant", "content": reply})
        messages.append({"role": "system", "content": f"Tool result: {result}"})

    else:
        answer = reply.replace("FINAL_ANSWER:", "").strip()
        print("AI:", answer)
        messages.append({"role": "assistant", "content": reply})
























