from EmotionDetection.emotion_detection import emotion_detector

print('*****************************************************************')
print('I am glad this happened => ', emotion_detector('I am glad this happened'))
print('*****************************************************************')
print('I am really mad about this => ', emotion_detector('I am really mad about this'))
print('*****************************************************************')
print('I feel disgusted just hearing about this => ', emotion_detector('I feel disgusted just hearing about this'))
print('*****************************************************************')
print('I am so sad about this => ', emotion_detector('I am so sad about this'))
print('*****************************************************************')
print('I am really afraid that this will happen => ', emotion_detector('I am really afraid that this will happen'))