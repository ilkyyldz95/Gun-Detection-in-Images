from keras.models import load_model
from scipy.ndimage import imread
from os import listdir
import numpy as np
from scipy.misc import imresize


image_dir = 'small_test/'
num_images = len(listdir(image_dir))
test_images = np.zeros((num_images, 335, 472, 3))
dim_average = [335, 472]

i = 0
for image_name in listdir(image_dir):
    # read image
    img = imread(image_dir + image_name, mode='RGB')

    resized_image = imresize(img, dim_average, interp='bilinear', mode=None)

    test_images[i] = resized_image
    i += 1

for fold in range(5):

    print 'Loading 1st half model from directory:', '1st_half_fold_index_' + str(fold) + '.h5'
    model = load_model('1st_half_fold_index_' + str(fold) + '.h5')

    predictions = model.predict(test_images)
    for index in range(num_images):
        print "image name:", listdir(image_dir)[index]
        print "score:", predictions[index]

    accuracy_metric = model.evaluate(test_images, np.ones(num_images))[1]
    print "accuracy of fold ", fold, accuracy_metric

for fold in range(5):

    print 'Loading 2nd half model from directory:', '2nd_half_fold_index_' + str(fold) + '.h5'
    model = load_model('2nd_half_fold_index_' + str(fold) + '.h5')

    predictions = model.predict(test_images)
    for index in range(num_images):
        print "image name:", listdir(image_dir)[index]
        print "score:", predictions[index]

    accuracy_metric = model.evaluate(test_images, np.ones(num_images))[1]
    print "accuracy of fold ", fold, accuracy_metric


# %50 nin altindaki prediction sayisini ve o imagelarin ismini yazdir.