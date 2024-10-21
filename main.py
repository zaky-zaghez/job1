def draw_rectangle(width, height):
    print("|" + "-" * height + "|")

    for _ in range (width - 2):
        print("|" + " " * height + "|")

    print("|" + "-" * height + "|")

draw_rectangle(3, 10)