while True:
    tag = input("Введіть назву тегу, який вам необхідний: ").lower()
    tagged_input = "#" + tag
    file = open("text.txt", "r")

    try:
        with file:
            found_lines = [line for line in file if tagged_input in line.lower()]

        if found_lines:
            print("Знайдено наступні рядки: \n")
            for line in found_lines:
                print(line)
        elif tag == "exit":
            break
        else:
            print("Такого тегу не існує")
    except:
        print("Помилка")

