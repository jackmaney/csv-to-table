#!/usr/bin/env python

import argparse
from typeguesser import TypeGuesser


def main():
    argParser = argparse.ArgumentParser()

    argParser.add_argument("file", type=str, help="The name (and path) of the target CSV file")
    argParser.add_argument("--header", help="Indicate whether or not the file has a header", action="store_true")
    argParser.add_argument("--sample", type=float, help="Sampling probability (between 0 and 1). " +
                                            "If set, this gives the sampling probability for rows of the given CSV file")
    argParser.add_argument("--quotechar", help="The quote character to use for the CSV file (default '\"')", default="\"")
    argParser.add_argument("--table_name", help="The name of the table desired in the output")

    args = argParser.parse_args()

    tg = TypeGuesser(args.file, header=args.header, sampleProbability=args.sample,
                     quotechar=args.quotechar, tableName=args.table_name)

    tg.guessTypes()

    print tg.getCreateStatement()

if __name__ == "__main__":
    main()
