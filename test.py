filePath = "index.js"
num = 1
offset = 24
numLimit = int(input("Enter total number to write for: "))
with open(filePath, 'r+') as file:
    while num <= numLimit:
        if num % 2 == 0:
            answer = True
        else:
            answer = False
        code = f"if(number === {num}) return {answer};\n"
        file.seek(offset,0)
        file.writelines(code)
        offset += 30 + len(str(num))
        num += 1
    file.seek(0,2)
    file.write("}")