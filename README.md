This darknet is based on AlexeyAB's darknet

Check this link : https://github.com/AlexeyAB/darknet

Added Function
1. train_detector_v2
	Added "-save_interval" option. It means interval of saving .weight file.
	e.g.) ./darknet detector train data_file.data cfg_file.cfg weigh_file.weights -save_interval 1000
	this save weight file like ~~~_1000.weight, ~~~_2000.weight, ~~~_3000.weight, so on.

2. validate_detector_map_v2
	It is same as "validate_detector_map".
	But SAVE processed images(like test result) image in "results_map" named as "predict_$filename.jpg"
	In output image, Red box is ground-truth, green box is TP, blue box is FP.
	
	Added options: "excel_format", "no_img"
	1. "excel_format" : 
		Convert map results to excel format and append to "map_excel.txt" file
		This is useful when you use .sh or .cmd file.
		e.g.) ~~.sh
			for filename in ./backup/*.weights
			do
				./darknet detector map_v2 data_file.data cfg_file.cfg "${filename}" -excel_format
			done
			
	2. "no_img" : 
		Do not save images.

3. validate_detector_map_v3
	it is modifying. Don't Use.
	
	
Modified Function
1. test_detector
	image is saved in "results" directory & its name is "predect_$filename.jpg"
	Prediction value is printed next to class name in images


by the way, as you know, actually _v2 functions is debugging fuctions to add new options in original fucntions.
so _v2 functions will be merged with orginal functions. but because of lack of time,  maintain this shape