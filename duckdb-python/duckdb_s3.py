#!/usr/bin/env python3
import os
import duckdb

bucket = "conveyor-samples-b9a6edf0"

def main():

    # setup connection to s3 using duckb
    duckdb.sql(f"""
        INSTALL httpfs;
        INSTALL AWS;
        LOAD httpfs;
        LOAD aws;
        """)

    # default loading of credential (still some issues with using sso https://github.com/duckdb/duckdb_aws/issues/14)
    # eval $(aws configure export-credentials --format env)
    duckdb.sql("""CALL load_aws_credentials();""")

    # perform some transformation
    duckdb.sql(f"""
        CREATE VIEW items AS
        WITH 
        raw_items as (SELECT id as item_id, order_id, sku as product_id 
                           FROM read_csv('s3://{bucket}/coffee-data/raw/raw_items.csv', delim=',', header=True, AUTO_DETECT=True)),
        raw_products as (SELECT sku as product_id, name, price, description,
                 case when type = 'food' then 1 else 0 end is_food_item,
                 case when type = 'beverage' then 1 else 0 end is_drink_item
            FROM read_csv('s3://{bucket}/coffee-data/raw/raw_products.csv', delim=',', header=True, AUTO_DETECT=True))
        
        SELECT raw_items.order_id, 
               sum(raw_products.is_food_item) as count_food, 
               sum(raw_products.is_drink_item) as count_drink,
               count(*) as total_count
        FROM raw_products left join raw_items on raw_items.product_id = raw_products.product_id
        group by 1;
        
	""")

    print(duckdb.sql(f"""select * from items order by total_count desc limit 10"""))

    # write the results to an output
    duckdb.sql(f"""
            COPY
                items
            TO
                's3://{bucket}/coffee-data/tmp/duckdb_output.parquet'(FORMAT PARQUET);
    	""")

if __name__ == '__main__':
    main()
