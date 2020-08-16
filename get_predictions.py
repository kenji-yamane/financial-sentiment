import gradio as gd
from transformers import BertTokenizer
from transformers import TFBertForSequenceClassification
import tensorflow as tf
import numpy as np
from os import getcwd
global model

model_path = getcwd() + '/model.h5'
model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels = 3)
model.load_weights(model_path)

global tokenizer 

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case = True)

def get_result(text, model = model, tokenizer = tokenizer):
  inputs = tokenizer(text, return_tensors = 'tf')
  inputs['labels'] = tf.reshape(tf.constant(1), (-1,1))
  outputs = model(inputs)
  loss, logits = outputs[:2]
  sentiment = np.argmax(np.array(logits))
  if sentiment == 2:
    return 'Positive'
  if sentiment == 1:
    return 'Neutral'
  else:
    return 'Negative'

def predict_on_dataset(data, company, predict_on):
    company_data = data[data['tickers'] == company].copy()
    if predict_on == 'text':
        company_data['BERT_sentiment'] = company_data['text'].apply(get_result, args = (model, tokenizer))
    elif predict_on == 'title':
        company_data['BERT_sentiment'] = company_data['title'].apply(get_result, args = (model, tokenizer))
    return company_data
