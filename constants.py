CSV_FILEPATH = "CSV Files/Transactions.csv"
SQLITE_DBNAME = 'transactions.db'
SQLITE_TABLENAME = 'Transactions'
SQLITE_KEYNAME = 'transaction_id'
SQLITE_COLNAMES = [
    (SQLITE_KEYNAME, 'int'),
    ('transaction_date', 'date'),
    ('posted_date', 'date'),
    ('card_number_ending', 'int'),
    ('description', 'text'),
    ('category', 'text'),
    ('debit', 'real'),
    ('credit', 'real')
]