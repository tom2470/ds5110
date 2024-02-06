data:
	mkdir -p data
	cd data; curl -LO https://ncaaorg.s3.amazonaws.com/research/academics/2020RES_APR2019PubDataShare.csv;
datahead:
	mkdir -p img
	python -B src/datahead1.py
fig1:
	mkdir -p img
	python -B src/fig11.py
fig2:
	mkdir -p img
	python -B src/fig2.py
fig3:
	mkdir -p img
	python -B src/fig31.py
clean:
	rm -rf data
	rm -rf img
