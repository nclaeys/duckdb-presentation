# How to load data in Duckdb using duckdb binary

create table raw_csv_items as select * from read_csv('../data/raw/raw_items.csv',header=True);

select * from raw_csv_items;

copy (select * from raw_csv_items) to '../data/raw/raw_items.parquet' (FORMAT 'parquet');

select * from read_parquet('../data/raw/raw_items.parquet');

# creating simple script that shows parquet data (alternative to datafusion setup)

./show_parquet_table.py ../data/raw/raw_items.parquet
