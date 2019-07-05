Resorte.png : graf.py
	python graf.py > Resorte.png
graf.py : Resorte.txt
	g++ JuradoDavidS5C3.cpp > a.out
	./a.out > Resorte.txt
