import emoji

emoji_to_emotion = {
    ":grinning_face:": "happy",
    ":red_heart:": "love",
    ":angry_face:": "angry",
    ":crying_face:": "sad",
    ":face_with_open_mouth:": "surprised"
}

string = "I am feeling 😀 today. ❤️ you all! "

# Convert emojis to emotions
emotion_string = ""
for word in string.split():
    if word in emoji_to_emotion:
        emotion_string += emoji_to_emotion[word]
    else:
        emotion_string += word
    emotion_string += " "

print(emotion_string)
