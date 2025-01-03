from transformers import RobertaTokenizer, RobertaForSequenceClassification, RobertaConfig

config = RobertaConfig.from_pretrained("./sentiment_model", num_labels=3)
tokenizer = RobertaTokenizer.from_pretrained("./sentiment_model")
model = RobertaForSequenceClassification.from_pretrained("./sentiment_model", config=config)

news_file = "article.txt"  
with open(news_file, "r", encoding="utf-8") as file:
    text = file.read()

preset = tokenizer(text,return_tensors="pt", padding=True, truncation=True, max_length=512)

outputs = model(**preset)
logits = outputs.logits

sentiment = logits.argmax(dim=-1).item()

if sentiment == 0:
    print("Negative sentiment")
elif sentiment == 1:
    print("Neutral sentiment")
elif sentiment == 2:
    print("Positive sentiment")
else:
    print("Not sure")

