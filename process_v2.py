import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Directory where the data will reside, relative to 'darknet.exe'
train_data = 'data/TunaVita/obj/'
test_data = 'data/TunaVita/sc1/'

# Percentage of images to be used for the test set
percentage = 100; 

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1   
index_test = round(100 / percentage)  
for pathAndFilename in glob.iglob(os.path.join(train_data, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1 
        file_train.write(train_data + title + '.jpg' + "\n")
    else:
        file_train.write(train_data + title + '.jpg' + "\n")
        counter = counter + 1
		
for pathAndFilename in glob.iglob(os.path.join(test_data, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1 
        file_test.write(test_data + title + '.jpg' + "\n")
    else:
        file_test.write(test_data + title + '.jpg' + "\n")
        counter = counter + 1
