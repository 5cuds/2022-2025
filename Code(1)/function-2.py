def emojis(msg):
    words = msg.split(" ")
    emojis = {
        ":)": "😃",
        ":(": "🙁",
        ":D": "😄",
        "D:": "😫"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
        return output

msg = input(">")
print(emojis(msg))