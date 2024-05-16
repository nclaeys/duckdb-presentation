# How to process local data using Duckdb

```
create table raw_csv_items as select * from read_csv('../data/raw/raw_items.csv',header=True);
```

```
select * from raw_csv_items;
```

```
copy (select * from raw_csv_items) to '../data/raw/raw_items.parquet' (FORMAT 'parquet');
```

```
select * from read_parquet('../data/raw/raw_items.parquet');
```

# creating simple script that shows parquet/csv data (alternative to datafusion setup)

```
./show_parquet_table.py ../data/raw/raw_items.parquet
```



# loading external data

## Parquet
```
./show_parquet_table.py https://github.com/nclaeys/duckdb-presentation/raw/master/data/raw/raw_items_sample.parquet
```

### analyzing parquet metadata

```
./show_parquet_metadata.py https://github.com/nclaeys/duckdb-presentation/raw/master/data/raw/raw_items_sample.parquet
```

## CSV
```
./show_csv_table.py https://github.com/nclaeys/duckdb-presentation/raw/master/data/raw/raw_items.csv
```

## reading google sheet data
```
select * from read_csv_auto('https://docs.google.com/spreadsheets/d/1HpFaXByq9BUGJghYEEJIclbAYvGOKqHEJzazPEZocAo/export?usp=sharing&format=csv', normalize_names=True);
```

## S3 data

```
eval $(aws configure export-credentials --format env) 
./duckdb_s3.py
```
