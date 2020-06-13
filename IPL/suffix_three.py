num_sentences = int(input())


for s in range(num_sentences):
    sentence = input()

    if sentence[-2:] == "po":
        print("FILIPINO")
    elif sentence[-4:] in ["desu", "masu"]:
        print("JAPANESE")
    else:
        print("KOREAN")
