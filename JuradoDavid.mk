all : Canal.png TransformadaFitrada.png
	python JuradoDavid_canal_ionico.py > Canal.png
	python JuradoDavid_Fourier.py > TransformadaFiltranda.png