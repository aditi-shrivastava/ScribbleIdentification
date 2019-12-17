from prepare_data import *
from sklearn.model_selection import train_test_split as tts
from keras.models import Sequential,Model
from keras.layers import Input,Dense, Dropout
from keras.utils import np_utils
from nets.MLP import mlp
from nets.conv import conv
from nets.cnn_inception import inception_module
from random import randint

# define some constants
N_OBJECTS= 7
OBJECTS = {0: "Airplane", 1: "Wine Bottle", 2: "Butterfly", 3: "Banana",4:"T Shirt",5:"Umbrella",6:"Grapes"}

# number of samples to take in each class
N = 1000

# some other constants
N_EPOCHS = 20

# data files in the same order as defined in FRUITS
files = ["airplane.npy", "wine_bottle.npy","butterfly.npy","banana.npy","t-shirt.npy","umbrella.npy","grapes.npy"]

# images need to be 28x28 for training with a ConvNet
objects = load("/Users/darklord/Downloads/datasets/", files, reshaped=True)

# images need to be flattened for training with an MLP
# fruits = load("data/", files, reshaped=False)


# limit no of samples in each class to N
objects = set_limit(objects, N)

# normalize the values
objects = list(map(normalize, objects))

# define the labels
labels = make_labels(N_OBJECTS, N)

# prepare the data
(x_train, x_test, y_train, y_test) = tts(objects, labels, test_size=0.05)

# one hot encoding
Y_train = np_utils.to_categorical(y_train, N_OBJECTS)
Y_test = np_utils.to_categorical(y_test, N_OBJECTS)

# use our custom designed ConvNet model
#model = conv(classes=N_OBJECTS, input_shape=(28, 28, 1))
# input_layer = Input(shape=(28, 28, 1))
# x  = inception_module(input_layer,
#                      filters_1x1=64,
#                      filters_3x3_reduce=96,
#                      filters_3x3=128,
#                      filters_5x5_reduce=16,
#                      filters_5x5=32,
#                      filters_pool_proj=32,
#                      name='inception_3a')

model = VGG16(input_shape=(28,28,1), weights=None, include_top=False)
# use our custom designed MLP model
# model = mlp(classes=N_FRUITS)


model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

#raw_input("Type 'train' to start training: ")
print("Training commenced")

model.fit(np.array(x_train), np.array(Y_train), batch_size=32, epochs=N_EPOCHS, verbose=1)

print("Training complete")

print("Evaluating model")
preds = model.predict(np.array(x_test))

score = 0
for i in range(len(preds)):
    if np.argmax(preds[i]) == y_test[i]:
        score += 1

print("Accuracy: ", ((score + 0.0) / len(preds)) * 100)

#name = raw_input(">Enter name to save trained model: ")
model.save('./models/inception_v3.h5')
print("Model saved")


def visualize_and_predict():
    "selects a random test case and shows the object, the prediction and the expected result"
    n = randint(0, len(x_test))
    visualize(denormalize(np.reshape(x_test[n], (28, 28))))
    pred = OBJECTS[np.argmax(model.predict(np.array([x_test[n]])))]
    actual = OBJECTS[y_test[n]]
    print("Actual:", actual)
    print("Predicted:", pred)


print("Testing mode")
visualize_and_predict()