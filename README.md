# CSV_to_SQLite
Converts a CSV file into a SQLite database table.

Use the `create_new_database()` function to create a new SQLite database file based on the following parameters:
- csv_filepath: Path to CSV file (String)
- sqlite_dbname: Name of the new sqlite database to be created. (ex. "transactions.db")
- sqlite_tablename: Name of the new sqlite table to be created. (String)
- sqlite_columns: An array of tuples containing the column names of the CSV file and their SQLite data types. Both tuples are Strings.

Use the constants in the `constants.py` file to specify the above parameters, or use the function directly by importing it.

To run:
```python3 csv_to_sqlite.py```

For `sqlite_columns`, common SQLite data types covering most types of data are:
- INTEGER
- REAL
- TEXT

A folder `CSV_Files` is provided to store CSV files to process.

**By default, it is set up to REPLACE the database file specified in `sqlite_dbname`.**
