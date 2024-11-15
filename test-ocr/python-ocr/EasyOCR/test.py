import easyocr
reader = easyocr.Reader(['id'])  # 'id' untuk bahasa Indonesia
result = reader.readtext('kk.jpeg')
for (bbox, text, prob) in result:
    print(f"Teks: {text} | Probabilitas: {prob}")