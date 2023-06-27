import gptworldAi

# single completion
for chunk in gptworldAi.Completion.create("你是谁", "127.0.0.1:7890"):
    print(chunk, end="", flush=True)
print()

# chat completion
message = []
while True:
    prompt = input("请输入问题：")
    message.append({"role": "user", "content": prompt})
    text = ""
    for chunk in gptworldAi.ChatCompletion.create(message, '127.0.0.1:7890'):
        text = text + chunk
        print(chunk, end="", flush=True)
    print()
    message.append({"role": "assistant", "content": text})
