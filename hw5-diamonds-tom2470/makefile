data:
	mkdir -p data
	cd data; curl -LO https://github.com/tidyverse/ggplot2/blob/main/data-raw/diamonds.csv?raw=true
q1:
	mkdir -p figs
	python -B src/q1.py
q2:
	mkdir -p figs
	python -B src/q2.py
q3:
	mkdir -p figs
	python -B src/q3.py
q4:
	mkdir -p figs
	python -B src/q4.py
q5:
	mkdir -p figs
	python -B src/q5.py
clean:
	rm -rf data
	rm -rf figs
env:
	conda env create -f environment.yml
	conda activate myenv               
