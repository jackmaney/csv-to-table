#!/usr/bin/env python

import argparse

from typeguesser import TypeGuesser


def main():
    argParser = argparse.ArgumentParser()

    argParser.add_argument(
        "file", type=str, help="The name (and path) of the target CSV file")
    argParser.add_argument(
        "--header", help="Indicate whether or not the file has a header", action="store_true")

    argParser.add_argument(
        "--lowercase_header", help="Indicate whether or not to lowercase inferred " +
                        "column names.", action="store_true")

    argParser.add_argument("--sample", type=float, help="Sampling probability (between 0 and 1). " +
                           "If set, this gives the sampling probability for rows of the given CSV file")
    argParser.add_argument(
        "--quotechar", help="The quote character to use for the CSV file (default '\"')", default="\"")
    argParser.add_argument(
        "--delimiter", help="The delimiter to use for the CSV file (default ',')", default=',')
    argParser.add_argument(
        "--table_name", help="The name of the table desired in the output")
    argParser.add_argument("--columns", type=str,
                           help="A comma-delimited list of column names that you wish to use")

    args = argParser.parse_args()

    columns = None
    if args.columns:
        columns = args.columns.split(",")

    tg = TypeGuesser(
        args.file, header=args.header, sampleProbability=args.sample,
        quotechar=args.quotechar, delimiter=args.delimiter, tableName=args.table_name,
        columns=columns, lowercaseHeader=args.lowercase_header)

    tg.guessTypes()

    print tg.getCreateStatement()

if __name__ == "__main__":
    main()
