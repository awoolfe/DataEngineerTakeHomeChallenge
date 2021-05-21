'''Take home data challenge
Created by Alessia Woolfe
05/19/2021
'''

import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa


# function to flatten widget list and create name and amount column
def explode_widgets(dataframe):
    data = []
    for index, row in dataframe.iterrows():
        # if widget list is empty, append line with empty widget name and amount
        if len(row["widget_list"]) == 0:
            data.append(
                [row['id'], row['email_anon'], row['age_group'], row['user_score'], row['sub_group_rank'], row['revenue'], None,
                 None, row['location'], row['created_at']])
        else:
            # flatten list, append new line containing the same data as original line, add new columns
            for x in row["widget_list"]:
                wid_name = x['name']
                wid_amount = x['amount']
                data.append([row['id'], row['email_anon'], row['age_group'], row['user_score'], row['sub_group_rank'], row['revenue'],
                             wid_name, wid_amount, row['location'], row['created_at']])
    # create new dataframe from list data
    newdf = pd.DataFrame(data, columns=['id', 'email_anon', 'age_group', 'user_score', 'sub_group_rank', 'revenue', 'widget_name',
                                        'widget_amount', 'location', 'created_at'])
    return newdf


# function to create new table with inverted index
def create_inverted_table(dataframe, columnkey, columnval):
    new_table = {}
    for index, row in dataframe.iterrows():
        # append id to existing key
        if row[columnkey] in new_table:
            new_table[row[columnkey]].append(row[columnval])
        # create new key with id value
        else:
            new_table[row[columnkey]] = [row[columnval]]
    # create new table inverted index
    new_table = pd.DataFrame.from_dict(new_table, orient='index').transpose()
    return new_table

def obtain_original_email(email_dict, email_key):
    email_dict = dict((reversed(x) for x in email_dict.items()))
    return email_dict[email_key]

# create dataframe from json file
df = pd.read_json("data.json", lines="True")

# remove duplicated id and created_at
# duplicated = df[df.duplicated(['id', 'created_at'])]
# print(duplicated)
df = df.drop_duplicates(subset=['id', 'created_at'])

# group by age group, rank user score in new column sub_group_rank
df["sub_group_rank"] = df.groupby("age_group")["user_score"].rank(method='dense')

# create anonymized email list by assigning each unique email to a number
email_dictionary = {emails: i for i, emails in enumerate(df["email"].unique())}
#print(email_dictionary)
df["email_anon"] = df["email"].apply(lambda x: email_dictionary[x])
# original email can be retrieved through the dictionary email_dictionary with obtain_original_email
#print(obtain_original_email(email_dictionary, 2))

# flatten widget list and create new columns name and amount
df = explode_widgets(df)

# create inverted table for which ids exist in each location
country = create_inverted_table(df, 'location', 'id')

#test csv
#country.to_csv('output.csv')
#df.to_csv('ce.csv')

#write cleaned data to parquet file
processed_table = pa.Table.from_pandas(df)
pq.write_table(processed_table, 'processed_data.parquet')

#write inverted index to parquet file
country_table = pa.Table.from_pandas(country)
pq.write_table(country_table, 'inverted_country_index.parquet')
