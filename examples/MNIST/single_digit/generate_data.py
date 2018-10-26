import torchvision
import random

trainset = torchvision.datasets.MNIST(root='../../../data/MNIST', train=True, download=True)
testset = torchvision.datasets.MNIST(root='../../../data/MNIST', train=False, download=True)



def next_example(dataset,i):
    x,y = next(i),next(i)
    (_,c1),(_,c2) = dataset[x],dataset[y]
    return x,y,c1+c2

def gather_examples(dataset,filename):
    examples = list()
    i = list(range(len(dataset)))
    random.shuffle(i)
    i = iter(i)
    while(True):
        try:
            examples.append(next_example(dataset,i))
        except StopIteration:
            break 

    with open(filename,'w') as f:
        for example in examples:
            f.write('addition({},{},{}).\n'.format(example[0],example[1],example[2]))

gather_examples(trainset,'train_data.txt')
gather_examples(testset,'test_data.txt')
