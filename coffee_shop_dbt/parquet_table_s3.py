#!/usr/bin/env python3
import duckdb
import sys

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

    if __name__ == '__main__':
        duckdb.sql(f"""INSTALL httpfs;""")
        duckdb.sql(f"""LOAD httpfs;""")
        print(duckdb.sql(f"""select * from '{sys.argv[1]}' limit 10"""))

if __name__ == '__main__':
    main()
