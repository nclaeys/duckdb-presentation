#!/usr/bin/env python3
import os

import duckdb
import sys


if __name__ == '__main__':
  duckdb.sql(f"""INSTALL httpfs;""")
  duckdb.sql(f"""LOAD httpfs;""")
  print(duckdb.sql(f"""select * from read_csv_auto('{sys.argv[1]}',header=True) limit 10"""))
