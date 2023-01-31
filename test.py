import wget
import os
import zipfile

response = wget.download("https://public.vinai.io/word2vec_vi_words_300dims.zip", "wordvec/word2vec_vi_words_300dims.zip")
with zipfile.ZipFile("wordvec/word2vec_vi_words_300dims.zip", 'r') as zip_ref:
    zip_ref.extractall("wordvec")

text = "alo"
for w in text:
    print(w)