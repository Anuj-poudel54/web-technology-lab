
with open("html.txt") as f:
    content = f.read()

i = 8
while input("Create: ").lower() != 'n':
    with open(f"./lab2/qns_js{i}.html", "w") as f2:
        f2.write(content)
    i+=1
