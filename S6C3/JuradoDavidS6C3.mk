init.png : graf.py
	python graf.py > init.png
graf.py : init.txt
	g++ JuradoDavidS6C2.cpp > a.out
	./a.out > init.txt
