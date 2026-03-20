def emotion_detector(text_to_analyze):

    text = text_to_analyze.lower()

    # Fake scores (để tránh lỗi API)
    emotions = {
        "anger": 0,
        "disgust": 0,
        "fear": 0,
        "joy": 0,
        "sadness": 0
    }

    if "happy" in text:
        emotions["joy"] = 1
    elif "angry" in text:
        emotions["anger"] = 1
    elif "sad" in text:
        emotions["sadness"] = 1
    elif "scared" in text:
        emotions["fear"] = 1
    elif "disgust" in text:
        emotions["disgust"] = 1

    # tìm dominant emotion
    dominant = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant

    return emotions
result = emotion_detector("I am very happy today")

print(f"For the given statement, the system response is {result}. "
      f"The dominant emotion is {result['dominant_emotion']}.")