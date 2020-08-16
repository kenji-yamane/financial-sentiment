import pandas as pd
import gradio as gd
import tensorflow as tf
from get_predictions import predict_on_dataset
from process_data_after_predictions import process_data
from plot_data import plot_results
import sys
from os import getcwd

def main():
    companys = ['NFLX'] # choose FB or AMZN
    get_predictions_data = sys.argv[0]

    data = pd.read_csv('stock_news_data.csv', sep = ';')
    # get predictions
    if (get_predictions_data == True):
        for company in companys:
            company = company.lower()
            company_path_title = getcwd() + '/data_after_predictions/' + (company) + '_data_title.csv' 
            company_path_text = getcwd() + '/data_after_predictions/' + (company) + '_data_text.csv' 


            company_data_title = get_predictions(data, company = company, predict_on = 'title')
            company_data_title.csv(company_path_title)

            company_data_text = get_predictions(data, company = company, predict_on = 'text')
            company_data_text.csv(company_path_text)
    else:
        # process predictions and plot results
        for company in companys:
            company_lower = company.lower()
            company_path_title = getcwd() + '/data_after_predictions/' + (company_lower) + '_data_title.csv' 
            company_path_text = getcwd() + '/data_after_predictions/' + (company_lower) + '_data_text.csv' 
            historic_path = getcwd() + '/historic_data_nasdaq/' + (company_lower) + '_historic.csv' 
            historical_data = pd.read_csv(historic_path)
            company_text = pd.read_csv(company_path_text)
            company_title = pd.read_csv(company_path_title)


            plottable_data_title = process_data(company_title, historical_data)
            plottable_data_text = process_data(company_text, historical_data)
            text_company = company + '_TEXT'
            title_company = company + '_TITLE'
            plot_results(plottable_data_title, title_company)
            plot_results(plottable_data_text, text_company)
            

if __name__ == '__main__':
    main()
