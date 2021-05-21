import pandas as pd
import TakeHomeChallengeSolutions
import pyarrow.parquet as pq
import pyarrow as pa

test_df = pd.read_json("test_data.json", lines=True)

def test_explode_widget(dataframe):
    assert dataframe.shape[0] == 3
    assert dataframe.shape[1] == 9
    dataframe=TakeHomeChallengeSolutions.explode_widgets(dataframe)
    assert dataframe.shape[0] == 4
    assert dataframe.shape[1] == 10
    print("Explode widget success!")

def test_create_inverted_table(dataframe):
    assert dataframe.shape[0] == 3
    assert dataframe.shape[1] == 9
    dataframe=TakeHomeChallengeSolutions.create_inverted_table(dataframe,'location','id')
    assert dataframe['Indonesia'].count() == 2
    assert dataframe['Greece'].count() == 2
    print('Inverted table success!')


test_explode_widget(test_df)
test_create_inverted_table(test_df)