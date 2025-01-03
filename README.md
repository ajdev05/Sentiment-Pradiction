# Sentiment Analysis

This project uses a fine-tuned DistilRoBERTa model to analyze the sentiment of financial news articles. The model classifies text into three sentiment categories: Negative, Neutral, and Positive.

## Model Information

The model is a fine-tuned version of DistilRoBERTa, specifically trained on financial news data. It's hosted on Hugging Face:
- Model: [mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis](https://huggingface.co/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/ajdev05/Sentiment-Pradiction.git
cd Sentiment-Pradiction
```

2. Install dependencies:
```bash
pip install -r r.txt
```

3. Download the model files:
   - Visit the [model page on Hugging Face](https://huggingface.co/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis)
   - Download all files and place them in a directory named `sentiment_model` in your project root

## Usage

1. Place your financial news article in a file named `article.txt` in the project directory.

2. Run the sentiment analysis script:
```python main.py
```

## Labels

The model uses the following sentiment labels:
- 0: Negative
- 1: Neutral
- 2: Positive

This project uses a model that's available on Hugging Face. Please refer to the [model page](https://huggingface.co/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis) for licensing information.


