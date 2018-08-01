for filename in ./backup/*.weights
do
	./darknet detector map TunaVita.data TunaVita.cfg "${filename}" >> map.txt
done
