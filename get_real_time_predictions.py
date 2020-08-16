import gradio as gd
from transformers import BertTokenizer
from transformers import TFBertForSequenceClassification
import tensorflow as tf
import numpy as np
import pandas as pd
from os import getcwd
global model


model_path = getcwd() + '/model.h5'
model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels = 3)
model.load_weights(model_path)


global tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case = True)


def get_result_gd(text, model = model, tokenizer = tokenizer):
  inputs = tokenizer(text, return_tensors = 'tf')
  inputs['labels'] = tf.reshape(tf.constant(1), (-1,1))
  outputs = model(inputs)
  loss, logits = outputs[:2]
  logits = np.array(logits)
  labels =  {'Positive' : 2, 'Neutral': 1, 'Negative' : 0}
  logits = [item for sublist in logits for item in sublist]
  probs = {}
  for key, value in labels.items():
        probs[key] = round(logits[value], 2)
  probs = pd.DataFrame.from_records(probs, index = ['Value'])
  return probs

def main():
    inputs = 'text'
    gd.Interface(fn = get_result_gd, inputs = 'text', outputs = gd.outputs.Dataframe()).launch()
    return None
if __name__ == '__main__':
    main()
