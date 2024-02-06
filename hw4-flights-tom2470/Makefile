URL=https://github.com/ds5110/rdata/blob/main/data/mydb.sqlite?raw=true

# most popular tracks
q1:data/mydb.sqlite
	python -B src/q1.py

# most expensive invoice
q2:data/mydb.sqlite
	python -B src/q2.py

# table info
q3:data/mydb.sqlite
	python -B src/q3.py

q4:data/mydb.sqlite
	python -B src/q4.py

# Get the SQL (and a copy of the database)
data/mydb.sqlite:
	mkdir -p data
	cd data; curl -LO $(URL)

clean:
	rm data/mydb.sqlite
