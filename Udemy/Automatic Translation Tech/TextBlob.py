from textblob import TextBlob

original_text = 'Easy way to translate a text in Python'
blob = TextBlob(original_text)
translated_blob = blob.translate(to='ar')

print(f"Original text: {original_text}")
print(f"Translated text: {translated_blob}")