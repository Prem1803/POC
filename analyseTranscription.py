from textblob import TextBlob
with open('transcript.txt', 'r') as f:
    text = f.read()
    blob = TextBlob(text)
    print("Noun phrases ",blob.noun_phrases)

    for sentence in blob.sentences:
        print(sentence.words)
        print(sentence.tags)