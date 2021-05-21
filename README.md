# Mistplay Data Engineer Take Home Challenge

## Solution

Python was chosen for this exercise because it is widely used for data processing and has powerful libraries to achieve this, such as pandas. Pandas was used to create a dataframe out of the data.json file which allowed for effective data manipulation.

Most of the following requirements were achieved using built-in pandas functions, and some helper functions were created to flatten `widget_list` and create a table that gives, for each country in `location,` which `id`s are located in that country. A test file was created to test the functionality of these methods.

The column `email` was anonymized by assigning a number to each unique email in the table and storing the email and its associated unique number in a dictionary. A function was applied to the column `email` to write each email as an anonymous number and create the `email_anon` column. To retrieve the email, the _obtain_original_email_ can be called with a given key and will return the email associated with this key.

## Improvements

The helper functions written often loop through the entire dataframe, which is inefficent, and use more space. There are built-in pandas functions that could be used instead that are more efficient (such as _pandas.DataFrame.explode_) and that should be explored given more time. As well, the function to flatten widget list is not very scalable because it relies on the column names staying the same as the original data.

The solution to anonymize `email` could have used a bidirectional lookup structure as both key and value are unqiue. This would improve the speed of the solution.

More tests could be written to increase the testing coverage.

## How to run

`pip install -r requirements.txt`

`python mistplay_data_processor`

## Task Description

You will be required to produce code to process and transform some sample data.
The sample data is in the file called `data.json`.
There are also some duplicate rows.

The produced code should be able to acheive the following
1. remove duplicates over the columns `id` and `created_at` (considered simultaneously)
2. compute the rank of each user's `user_score` within each age group and output the rank in a new column called `sub_group_rank`
3. process the column `widget_list` by
    1. flattening the list items i.e. each item in the list is put into its own row
    2. extracting the values in the JSON elements into their own columns called `widget_name` and `widget_amount`
4. anonymize the column `email` and output the anonymized version in a new column `email_anon`.
This column `email_anon` should have the following properties.
    1. given an anonymized value the original value can be recovered
5. create a new table that is an inverted index that gives, for each country in `location,` which `id`s are located in that country
6. write the processed tables/data into separate `parquet` file(s).
Exactly how the files/tables are organized is not as important as having all the data present.

Your code will be evaluated for correctness, scalability and maintainability.

## Guidelines

1. You are allowed to use any language and any libraries you wish.
However, you should be able to justify your technical decisions.
Feel free to use any resources available to you.
2. Fork the github repo [ here ](https://github.com/Mistplay/DataEngineerTakeHomeChallenge). Once you've completed the challenge, push all code and other files to Github. Submit the link to your Github repo.
3. The challenge should not require more than a couple of hours to complete.
We don't want you to be spending too much time on it.
This being said, your code should be organized and well-designed within reason.
