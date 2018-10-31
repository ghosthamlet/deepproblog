import torchvision
import random

trainset = torchvision.datasets.MNIST(root='../../../data/MNIST', train=True, download=True)
testset = torchvision.datasets.MNIST(root='../../../data/MNIST', train=False, download=True)


def next_number(i,dataset,nr_digits):
    n = 0
    nr = list()
    for _ in range(nr_digits):
        x = next(i)
        _,c = dataset[x]
        n =  n*10 + c
        nr.append(str(x))
    return nr,n

def next_example(i,dataset,op,length):
    nr1,n1 = next_number(i,dataset,length)
    nr2,n2 = next_number(i,dataset,length)
    return nr1,nr2,op(n1,n2)

def generate_examples(dataset,op,length,out):
    indices = list(range(len(dataset)))
    random.shuffle(indices)
    i = iter(indices)

    examples = list()
    while(True):
        try:
            examples.append(next_example(i,dataset,op,length))
        except StopIteration:
            break 

    with open(out,'w') as f:
        for example in examples:

            f.write('addition([{}], [{}], {}).\n'.format(','.join(example[0]),','.join(example[1]),example[2]))

generate_examples(trainset,lambda x,y:x+y,1,'train.txt')
generate_examples(trainset,lambda x,y:x+y,3,'test.txt')