# financial-sentiment

This repository consists in a sentiment analysis of financial market using pre-trained BERT models

## Setup
  ```
  pip install -r requirements.txt
  ```
### To test the prediction and generate data
  ```
  python main.py True
  ```
### To process and plot data already obtained
  ```
  python main.py False
  ```
The images generated are 24 for each company. Transactioned and action price (2 factors), analyzed our model vs reality, stocknews model vs reality and the two models vs reality (3 factors), smoothed and not smoothed (2 factors), and title and body (2 factors), totalizing 2.3.2.2 = 24
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
