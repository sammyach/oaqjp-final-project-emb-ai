from flask import Flask, render_template, request
import json
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection App")

@app.route("/emotionDetector")
def detect_emotion():
    res = emotion_detector('I love my life')
    res_dict = json.loads(res)
    a = res_dict["anger"]
    return (str(a))



@app.route("/")
def render_index_page():
    return ("<b>Hello</b>", 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)