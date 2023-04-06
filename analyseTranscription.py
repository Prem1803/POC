from textblob import TextBlob
with open('transcript.txt', 'r') as f:
    text = f.read()
    blob = TextBlob(text)

    for sentence in blob.sentences:
        print(sentence)
        print(f"Polarity - {sentence.sentiment.polarity}\n")