import torchvision

train_set = torchvision.datasets.MNIST(root='./dataset',train=True,download=True)
test_set = torchvision.datasets.MNIST(root='./dataset',train=False,download=True)

