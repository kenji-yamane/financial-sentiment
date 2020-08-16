import pandas as pd
import matplotlib.pyplot as plt
from os import getcwd
def plot_results(data, company):
    # plot volume suavized
    fig_1 = data.plot(x = 'date', y = ['sma_volume', 'volume_sma_BERT_sentiment'], figsize = (50, 10), fontsize = 30 , title = (company + 'Volume vs Nosso Modelo(BERT) | Suavizado'))
    fig_1_path = getcwd() + '/' + company + '_Volume vs Nosso Modelo(BERT) | Suavizado'
    plt.savefig(fig_1_path, dpi = 300)
    plt.close()

    fig_2 = data.plot(x = 'date', y = ['sma_volume', 'volume_sma_stocknews_sentiment'], figsize = (50, 10), fontsize = 30, title = (company + 'Volume vs Stock News API | Suavizado' ))
    fig_2_path = getcwd() + '/' + company + '_Volume vs Stock News API | Suavizado'
    plt.savefig(fig_2_path, dpi = 300)
    plt.close()
    
    
    fig_3 = data.plot(x = 'date', y = ['sma_volume', 'volume_sma_stocknews_sentiment', 'volume_sma_BERT_sentiment'], figsize = (50, 10), fontsize = 30 , title = (company + 'Volume vs Nosso Modelo(BERT) vs Stock News API | Suavizado'))  
    fig_3_path = getcwd() + '/' + company + '_Volume vs Nosso Modelo(BERT) vs Stock News API | Suavizado'
    plt.savefig(fig_3_path, dpi = 300)
    plt.close()
    
    # sma = simple moving average
    # plot prices suavized
    fig_4 = data.plot(x = 'date', y = ['sma_open_price', 'sma_close_price', 'sma_high_price', 'sma_low_price', 'price_sma_BERT_sentiment'], figsize = (50, 10), fontsize = 30 , title = (company + 'Preço vs Nosso Modelo(BERT) | Suavizado'))
    fig_4_path = getcwd() + '/' + company + 'Preço vs Nosso Modelo(BERT) | Suavizado'
    plt.savefig(fig_4_path, dpi = 300)
    plt.close()
    
    fig_5 = data.plot(x = 'date', y = ['sma_open_price', 'sma_close_price', 'sma_high_price', 'sma_low_price', 'price_sma_stocknews_sentiment'], figsize = (50, 10), fontsize = 30 , title = (company + 'Preço vs Stock News API | Suavizado'))
    fig_5_path = getcwd() + '/' + company + 'Preço vs Stock News API | Suavizado'
    plt.savefig(fig_5_path, dpi = 300)
    plt.close()
    
    fig_6 = data.plot(x = 'date', y = ['sma_open_price', 'sma_close_price', 'sma_high_price', 'sma_low_price', 'price_sma_stocknews_sentiment', 'price_sma_BERT_sentiment'], figsize = (50, 10), fontsize = 30 , title = (company + 'PReço vs Nosso Modelo(BERT) vs Stock News API | Suavizado'))
    fig_6_path = getcwd() + '/' + company + 'Preço vs Nosso Modelo(BERT) vs Stock News API | Suavizado'
    plt.savefig(fig_6_path, dpi = 300)
    plt.close()
    
    # plot volume
    fig_7 = data.plot(x = 'date', y = [' Volume', 'volume_BERT_sentiment'], figsize = (50, 10), fontsize = 30 , title = (company + 'Volume vs Nosso Modelo(BERT)'))
    fig_7_path = getcwd() + '/' + company + '_Volume vs Nosso Modelo(BERT)'
    plt.savefig(fig_7_path, dpi = 300)
    plt.close()
    
    fig_8 = data.plot(x = 'date', y = [' Volume', 'volume_stocknews_sentiment'], figsize = (50, 10), fontsize = 30, title = (company + 'Volume vs Stock News API' ))
    fig_8_path = getcwd() + '/' + company + '_Volume vs Stock News API'
    plt.savefig(fig_8_path, dpi = 300)
    plt.close()
    
    fig_9 = data.plot(x = 'date', y = [' Volume', 'volume_stocknews_sentiment', 'volume_BERT_sentiment'], figsize = (50, 10), fontsize = 30 , title = (company + 'Volume vs Nosso Modelo(BERT) vs Stock News API')) 
    fig_9_path = getcwd() + '/' + company + '_Volume vs Nosso Modelo(BERT) vs Stock News API'
    plt.savefig(fig_9_path, dpi = 300)
    plt.close()
    
    # plot prices
    fig_10 = data.plot(x = 'date', y = [' Open', ' Close/Last', ' High', ' Low', 'price_BERT_sentiment'], figsize = (50, 10), fontsize = 30 , title = (company + 'Preço vs Nosso Modelo(BERT)'))
    fig_10_path = getcwd() + '/' + company + '_Preço vs Nosso Modelo(BERT) '
    plt.savefig(fig_10_path, dpi = 300)
    plt.close()
    
    fig_11 = data.plot(x = 'date', y = [' Open', ' Close/Last', ' High', ' Low', 'price_stocknews_sentiment'], figsize = (50, 10), fontsize = 30 , title = (company + 'Preço vs Stock News API'))
    fig_11_path = getcwd() + '/' + company + '_Preço vs Stock News API'
    plt.savefig(fig_11_path, dpi = 300)
    plt.close()
    
    fig_12 = data.plot(x = 'date', y = [' Open', ' Close/Last', ' High', ' Low', 'price_stocknews_sentiment', 'price_BERT_sentiment'], figsize = (50, 10), fontsize = 30 , title = (company + 'Preço vs Nosso Modelo(BERT) vs Stock News API'))
    fig_12_path = getcwd() + '/' + company + '_Preço vs Nosso Modelo(BERT) vs Stock News API'
    plt.savefig(fig_12_path, dpi = 300)
    plt.close()
    
    return None


