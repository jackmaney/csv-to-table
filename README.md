When importing CSV files to databases, I sometimes find it tedious to create the table in a database first. This is a very basic app (and a work in progress) that grabs the rows of a CSV file (sampling, if specified), uses the sample to guess at the data types of the columns, and uses these guesses to output a SQL `CREATE TABLE` statement. Think of it as a version of `CREATE TABLE some_table AS SELECT * FROM <some CSV file>`.

For the moment, this is aimed towards PostgreSQL (although that will change) and for now, a very limited number of data types will be supported, namely `text`, `boolean`, `smallint`, `int`, `bigint`, `numeric`, `date`, and `timestamp` (which are the types that I find myself using the most often).

To install, you can use pip:

```
sudo pip install csv-to-table
```

or you can grab the code (via either a `git clone` or just downloading a zip file of the repository) and then doing a

```
python setup.py install
```

Here's the flowchart of the type guessing (it's also available in the `images` folder of this repo):

![flowchart](https://github.com/jackmaney/csv-to-table/blob/master/images/type_guessing_flowchart.png?raw=true)

Here's a quick example:

Input:

```
$cat test.csv
a,b,c,d,e
32,"2013-12-28 22:16:57",0,"True","Here's some text, and some more"
"17.1","2012-06-29 05:11:00", -3,"False","Yep, more text"
```

Code:

```
from typeguesser import TypeGuesser

tg = TypeGuesser("test.csv", header=True)

tg.guessTypes()

print tg.getCreateStatement()
```

Output:

```
$ python test.py
CREATE TABLE test (
    a numeric,
    b timestamp,
    c smallint,
    d boolean,
    e text
);
```

Or, equivalently, you can use the included script `csv-to-table.py`:

```
$ ./csv-to-table.py -h
usage: csv_to_table.py [-h] [--header] [--lowercase_header] [--sample SAMPLE]
[--quotechar QUOTECHAR] [--delimiter DELIMITER]
[--table_name TABLE_NAME] [--columns COLUMNS]
file

positional arguments:
file                  The name (and path) of the target CSV file

optional arguments:
-h, --help            show this help message and exit
--header              Indicate whether or not the file has a header
--lowercase_header    Indicate whether or not to lowercase inferred column
names.
--sample SAMPLE       Sampling probability (between 0 and 1). If set, this
gives the sampling probability for rows of the given
CSV file
--quotechar QUOTECHAR
The quote character to use for the CSV file (default
  '"')
  --delimiter DELIMITER
  The delimiter to use for the CSV file (default ',')
  --table_name TABLE_NAME
  The name of the table desired in the output
  --columns COLUMNS     A comma-delimited list of column names that you wish
  to use

```

So, in particular:

```
$ ./csv-to-table.py --header test.csv
CREATE TABLE test (
	a numeric,
	b timestamp,
	c smallint,
	d boolean,
	e text
);
```
