Resultados_hw2.pdf : Resultados_hw2.tex
	latex Resultados_hw2.tex > Resultados_hw2.pdf
Resultados_hw2.tex : ODEs.cpp ODEplots.py 
	g++ ODEs.cpp > a.out
	./a.out    
	python ODEplots.py
