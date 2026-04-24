def emotion_detector(text_to_analyze):

    # simulasi hasil dari API
    emotions = {
        "anger": 0.1,
        "disgust": 0.05,
        "fear": 0.1,
        "joy": 0.6,
        "sadness": 0.15
    }

    # cari emosi dominan
    dominant_emotion = max(emotions, key=emotions.get)

    # tambahkan ke dictionary
    emotions["dominant_emotion"] = dominant_emotion

    return emotions
