#!/usr/bin/env python3
import os

import duckdb
import sys


if __name__ == '__main__':
  duckdb.sql(f"""INSTALL httpfs;""")
  duckdb.sql(f"""LOAD httpfs;""")
  print(duckdb.sql(f"""select * from parquet_metadata('{sys.argv[1]}')"""))

  print(duckdb.sql(f"""select * from parquet_schema('{sys.argv[1]}')"""))
