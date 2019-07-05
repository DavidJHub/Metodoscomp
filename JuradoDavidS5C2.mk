EULER.pdf : graficas.py
	python graficas.py > EULER.pdf
EULER.txt : JuradoDavidS5C2EULER.cpp
	g++ JuradoDavidS5C2EULER.cpp > a.out
	./a.out
RK.pdf : graficas.py
	python graficas.py > RK.pdf
RK.txt : JuradoDavidS5C2RK.cpp
	g++ JuradoDavidS5C2RK.cpp > a.out
	./a.out