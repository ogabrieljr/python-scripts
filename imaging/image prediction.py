import os

from imageai.Prediction import ImagePrediction

execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsSqueezeNet()
prediction.setModelPath(os.path.join(
    execution_path, "squeezenet_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()

for files in os.listdir("images"):
    print("\n" + files)
    predictions, probabilities = prediction.predictImage(
        os.path.join(execution_path, f"images\{files}"), result_count=5)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(f"{eachPrediction} : {eachProbability}")
