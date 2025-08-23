emotions={"happy": "😊", "sad": "😢", "angry": "😠", "love": "❤️", "surprised": "😲", "confused": "😕", "bored": "😐",
         "excited": "🤩", "tired": "😴", "nervous": "😬"}
print(emotions)



emotion = input("Enter your message: ").strip().lower()
words = emotion.split()
converted = [emotions.get(word, word) for word in words]
new_message = " ".join(converted)

print(new_message)