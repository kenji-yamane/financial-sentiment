import pandas as pd

def process_data(data, historic):
    data['date'] = data['date'].astype(str)
    historic['Date'] = pd.to_datetime(historic['Date']).astype(str)
    columns = ['Volume', 'Open', 'High', 'Low']

    # turn $234.03 into 234.03
    historic[historic.columns[1:]] = historic[historic.columns[1:]].replace('[\$,]', '', regex=True).astype(float)

    # combine data and historic
    data = pd.merge(data.copy(), historic, left_on = 'date', right_on=  'Date', how = 'left')
    data = data.rename(columns = {'sentiment' : 'stocknews_sentiment'})

    # quantify the sentiment
    categorical_to_numerical = {'Negative' : 0, 'Neutral' : 0.5, 'Positive' : 1}
    data = data.replace(categorical_to_numerical)

    # get the sentiment mean for each day
    data = data[['stocknews_sentiment', 'BERT_sentiment', ' Close/Last', ' Volume',' Open', ' High', ' Low', 'Date']].groupby(by = 'Date').mean()

    # scale the sentiment to the same order of the values, for better comparison
    data['price_stocknews_sentiment'] = data['stocknews_sentiment'] * (data[' Open'].values.mean())
    data['price_BERT_sentiment'] = data['BERT_sentiment'] * (data[' Open'].values.mean())

    # scale the sentiment to the same order of the values, for better comparison
    data['volume_stocknews_sentiment'] = data['stocknews_sentiment'] * (data[' Volume'].values.mean())
    data['volume_BERT_sentiment'] = data['BERT_sentiment'] * (data[' Volume'].values.mean())
    # drop duplicated_columns
    data = data.loc[:,~data.columns.duplicated()]

    # get index
    data['date'] = data.index

    # moving averages
    data['price_sma_stocknews_sentiment'] = data['price_stocknews_sentiment'].rolling(7).mean()
    data['price_sma_BERT_sentiment'] = data['price_BERT_sentiment'].rolling(7).mean()
    data['volume_sma_stocknews_sentiment'] = data['volume_stocknews_sentiment'].rolling(2).mean()
    data['volume_sma_BERT_sentiment'] = data['volume_BERT_sentiment'].rolling(2).mean()
    data['sma_volume'] = data[' Volume'].rolling(2).mean()
    data['sma_close_price'] = data[' Close/Last'].rolling(7).mean()
    data['sma_open_price'] = data[' Open'].rolling(7).mean()
    data['sma_high_price'] = data[' High'].rolling(7).mean()
    data['sma_low_price'] = data[' Low'].rolling(7).mean()
    return data