import requests
import json

url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

def emotion_detector(text_to_analyze):
    data = {
        'raw_document' : {
            'text' : text_to_analyze
        }
    }
    res = requests.post(url, headers = headers, json = data)
    if res.status_code == 200:
        res_dict = json.loads(res.text)
        emotion_dict = res_dict["emotionPredictions"][0]["emotion"]
        max_pair = max(emotion_dict.items(), key = lambda x: x[1])
        emotion_dict["dominant_emotion"] = max_pair[0]
        return emotion_dict
    else:
        print('failed to make request', res.status_code)    
