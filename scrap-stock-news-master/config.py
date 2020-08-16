import pandas as pd
import requests
from tqdm import tqdm
from io import StringIO

class APIConnection(object):
    """
    Connection to retrieve data from Stock News Api.

    """
    def __init__(self):
        self.api_token = 'i3lqyzdxynzjast1lazw5fbejsohvuidadkvwfnq'

    def get_news(self, tickers=[], items=0):
        base_link = 'https://stocknewsapi.com/api/v1'

        ## tickers query
        tickers_complement = 'tickers='
        for ticker in tickers:
            tickers_complement += ticker.upper() + ','
        tickers_complement = tickers_complement[:len(tickers_complement)-1]
    
        ## items query
        items_complement = f'items={items}'

        ## token query
        token_complement = f'token={self.api_token}'

        ## data type query
        datatype_complement = 'datatype=csv'

        ## create data range
        n = 500
        date_range = []
        date = '04012019'
        for i in range(n):
            d1 = date

            mm = int(date[0:2])
            dd = int(date[2:4])
            yyyy = int(date[4:8])
            
            next_month = False
            next_year = False

            if dd + 1 > 30: 
                next_month = True
                dd = 1
            else: dd = dd + 1
            if next_month:
                if mm + 1 > 12: 
                    next_year = True
                    mm = 1
                else: mm = mm + 1
            if next_year: yyyy = yyyy + 1
            
            date = '%02d%02d%04d' % (mm, dd, yyyy)
            
            date_range.append(f'{d1}-{date}')

            if (dd >= 11 and mm >= 8 and yyyy >= 2020): break


        df = pd.DataFrame(columns=['date', 'title', 'text', 'sentiment', 'tickers'])

        for date in tqdm(date_range):
            print('Getting news from:', date)
            ## date
            date_complement = f'date={date}'

            ## total
            total_link = f'{base_link}?{tickers_complement}&{items_complement}&{date_complement}&{datatype_complement}&{token_complement}'

            ## request
            response = requests.get(total_link)

            ## data parsing
            keep_col = ['date', 'title', 'text', 'sentiment', 'tickers']
            try:
                df_aux = pd.read_csv(StringIO(response.text), usecols=keep_col, index_col='date')
            except:
                break
            df = pd.concat([df, df_aux])

        df.to_csv('data.csv', sep=';')