import os

STORAGE = 'local' # do not change

# Change to directory of your dataset
DATASET_PATH = "/home/conex/Yet-Another-Openpose-Implementation/mydata"
IMAGES_PATH = "/home/conex/Yet-Another-Openpose-Implementation/mydata/images"
TRAIN_ANNS = DATASET_PATH + "/annotations/person_keypoints_train2017.json"
VALID_ANNS = DATASET_PATH + "/annotations/person_keypoints_val2017.json"

# will be used as output files
ROOT_TFRECORDS_PATH = "/home/conex/Yet-Another-Openpose-Implementation/mydata"
TRAIN_TFRECORDS = ROOT_TFRECORDS_PATH + "/training"
VALID_TFRECORDS = ROOT_TFRECORDS_PATH + "/validation"

RESULTS_ROOT = "/home/conex/Yet-Another-Openpose-Implementation/trained"
TENSORBOARD_PATH = RESULTS_ROOT + "/tensorboard"
CHECKPOINTS_PATH = RESULTS_ROOT + "/checkpoints"
MODELS_PATH = RESULTS_ROOT + "/models"





