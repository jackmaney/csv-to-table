When importing CSV files to databases, I sometimes find it tedious to create the table in a database first. This is a very basic app (and a work in progress) that grabs the rows of a CSV file (sampling, if specified), uses the sample to guess at the data types of the columns, and uses these guesses to output a SQL `CREATE TABLE` statement. Think of it as a version of `CREATE TABLE some_table AS SELECT * FROM <some CSV file>`.

For the moment, this is aimed towards PostgreSQL (although that will change) and for now, a very limited number of data types will be supported, namely `text`, `int`, `numeric`, `date`, and `timestamp` (which are the types that I find myself using the most often). 

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
	c numeric,
	d boolean,
	e text
);
```



