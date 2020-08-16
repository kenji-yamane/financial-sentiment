# Stock News Sentiment Analysis using Transfer Learning from BERT Model
This repository consists in a sentiment analysis of financial market using pre-trained BERT models

## Setup
  ```
  pip install -r requirements.txt
  ```
### If you want to get the prediction, generate data, process it and plot, run:
  ```
  python main.py True
  ```
### If you juts want to process and plot data already obtained, run:
  ```
  python main.py False
  ```
The images generated are 24 for each company. We analyze volume transactioned and stock price (2 factors), analyzed our model vs reality, stocknews model vs reality and the two models vs reality (3 factors), smoothed and not smoothed curves (2 factors), and predicting only on the title and  only on the body/corpus of the news (2 factors), totalizing 2.3.2.2 = 24
### To make predictions in real time:
- Run the following file
    ```
    python get_real_time_predictions.py
    ```
- Access the link that appears. Sentiment with biggest value is the one predicted by the AI

## Collaborators

- Mateus Nobre - https://github.com/mateusnobre
- Kenji Yamane - https://github.com/kenji-yamane
- João Sarmento - https://github.com/joaolrsarmento/
