import pandas as pd

def clean_and_prepare_data(csv_file_path):
    """
    Cleans and prepares the raw TMU ticket sales data.

    Parameters:
    - csv_file_path: str, the path to the CSV file containing the event data.

    Returns:
    - DataFrame with the cleaned and prepared data.
    """

    # load the data
    data = pd.read_csv(csv_file_path)

    # filter rows for the specific event and select columns
    filtered_data = data[data['seller'] == 'Jurassic Quest | Cross Insurance Arena | Portland, ME 807']
    selected_columns = filtered_data[['zipCode', 'buyerEmail']]  # TODO: decide on group by order (currently shows total tickets sold per zip)

    # format zip codes as strings with leading zeros
    selected_columns['zipCode'] = selected_columns['zipCode'].astype(str).str.zfill(5)

    # count the number of tickets per zip code
    ticket_counts = selected_columns.groupby('zipCode').size().reset_index(name='Ticket_Count')

    return ticket_counts

cleaned_data = clean_and_prepare_data('data.csv')
