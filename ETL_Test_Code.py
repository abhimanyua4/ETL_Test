import numpy as np
import pandas as pd


def output_dataframe(df_out):
    df_out = df_out.sort_values('Date of Birth')
    df_final_output = df_out[['Quarter_of_joining', 'full_name']].groupby(['Quarter_of_joining']).agg(
        ','.join).reset_index()
    print(df_final_output)
    lst = []
    temp_dict = dict()
    for i in range(len(df_final_output)):
        lst.extend(list(df_final_output['full_name'][i].split(',')))
        temp_dict[df_final_output['Quarter_of_joining'][i]] = lst

    return temp_dict




if __name__ == '__main__':
    df = pd.read_excel('employee__1_data_table.xls')
    df['First Name'] = df['First Name'].astype(str)
    df['Last Name'] = df['Last Name'].astype(str)
    df['Gender'] = df['Gender'].astype(str)
    df['Date of Birth'] = pd.to_datetime(df['Date of Birth'])
    df['Date of Joining'] = pd.to_datetime(df['Date of Joining'])
    df['Quarter of Joining'] = df['Quarter of Joining'].astype(str)
    df['Place Name'] = df['Place Name'].astype(str)
    df['County'] = df['County'].astype(str)
    df['City'] = df['City'].astype(str)
    df['User Name'] = df['User Name'].astype(str)
    df['full_name'] = df['First Name'] + ' ' + df['Last Name']
    df = df.rename(columns={'Quarter of Joining': 'Quarter_of_joining'})
    df_out = df[['Quarter_of_joining', 'full_name', 'Date of Birth']]
    output_dict = output_dataframe(df_out)
    print (output_dict)