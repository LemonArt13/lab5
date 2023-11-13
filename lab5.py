file_name = "text.txt"

def find_tags(file_name, tag):
    with open(file_name, "r") as file:
        lines = file.readlines()
        found_lines = []
        for line in lines:
            if line.startswith("#" + tag):
                found_lines.append(line)
    return found_lines



while True:
    tag = input("Введіть назву тегу, який вам необхідний: ").lower()
    if tag == "exit":
        break
    else:
        found_lines = find_tags(file_name, tag)
        if found_lines:
            print("Знайдено наступні абзаци: \n")
            for line in found_lines:
                print(line.strip())
        else:
            print("Такого тегу не існує")