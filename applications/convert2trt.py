from tensorflow.python.compiler.tensorrt import trt_convert as trt
model_dir = '/home/conex/OpenPose/trained_models/test_modelxxxx' # test model dir
save_dir = './model' # dir to save the converted model
converter = trt.TrtGraphConverterV2(input_saved_model_dir=model_dir)
converter.convert()
converter.save(save_dir)