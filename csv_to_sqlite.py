import pandas as pd
import sqlite3
from constants import *


def csv_to_sqlite(csv_filepath, sqlite_dbname, sqlite_tablename, sqlite_columns):
    '''
    csv_to_sqlite

    csv_filepath = Path to CSV file.
    sqlite_dbname = Name of the new sqlite database to be created. (ex. "transactions.db")
    sqlite_tablename = Name of the new sqlite table to be created.
    sqlite_columns = An array of tuples containing the column names of the CSV file and their SQLite data types. Both are represented as strings.
    '''

    try:
        df = pd.read_csv(csv_filepath)
    except FileNotFoundError as e:
        print("CSV file was not found. Specify one using the CSV_FILEPATH constant in constants.py. Double check pathing.")
        return None

    def create_col_names(sqlite_column_array):
        use_columns = []

        columns = ' ('
        col_num = 0
        for col in sqlite_column_array:
            if col_num != 0:
                use_columns.append(col[0])

            if col_num != len(sqlite_column_array)-1:
                columns += (col[0] + ' ' + col[1] + ',')
            else:
                columns += (col[0] + ' ' + col[1] + ')')
            col_num += 1

        return columns, use_columns
    
    columns, use_columns = create_col_names(sqlite_columns)
    keyname = sqlite_columns[0][0]

    conn = sqlite3.connect(sqlite_dbname)
    c = conn.cursor()

    c.execute(
        '''CREATE TABLE IF NOT EXISTS ''' + sqlite_tablename + ''' ''' + columns
    )

    df = pd.read_csv(csv_filepath)
    df.columns = use_columns

    df.to_sql(sqlite_tablename, conn, if_exists='replace', index_label=keyname)


if __name__ == '__main__':
    # Creates a new sqlite database file
    csv_to_sqlite(
        csv_filepath=CSV_FILEPATH,
        sqlite_dbname=SQLITE_DBNAME,
        sqlite_tablename=SQLITE_TABLENAME,
        sqlite_columns=SQLITE_COLNAMES
        )
