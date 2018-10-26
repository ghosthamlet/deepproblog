#MNIST examples#

#### MNIST1 ####
This is the MNIST addition example. The training examples are two mnist images, and it's label is the sum of the values of those two images.

#### MNIST2 ####
This is similar to the previous example, except that the operation itself is not known. There are parameters included in the program that should learn which operation is used. There are three datasets included, one for each operation used (*plus*, *minus* and *times*)

#### MNIST3 ####
This is similar to the second problem, but the numbers are of arbitrary length.

### MNIST 4 ####
This is similar to the first problem, but instead of a number that is the sum of the first two digits, there is a third MNIST image that is the sum of the first two.

### MNIST 5 ###
This problem consists of sorted lists of MNIST digits. Each subsequent digit is strictly bigger than the previous one.

#### MNIST baseline ####
This is the same network as is trained in the other experiments. However, this is in a normal, fully-supervised setting. This serves as a baseline to compare to the performance of the other experiments.

### Autoencoder ###
This performs unsupervised pre-training of the convolutional layer by using an auto-encoder. This is done replacing the fully-connected layers with transposed convolutional layers.