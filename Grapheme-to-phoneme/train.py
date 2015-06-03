from pybrain.structure import RecurrentNetwork
from pybrain.structure import LinearLayer, LSTMLayer, SoftmaxLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.utilities import percentError
import data_parsing
from scipy import array,where

training_data = []
ds = SupervisedDataSet(28,39)
training_data = data_parsing.conversion_to_one_hot_representation()
ds = data_parsing.conversion_to_pybrain_dataset_format(training_data)
test, train = ds.splitWithProportion( 0.25 )


n = RecurrentNetwork()

input1 = LinearLayer(28)
hidden1 = LSTMLayer(512)
hidden2 = LSTMLayer(512)
hidden3 = LSTMLayer(128)
output1 = SigmoidLayer(39)
output2 = LinearLayer(39)

n.addInputModule(input1)
n.addModule(hidden1)
n.addModule(hidden2)
n.addModule(hidden3)
n.addModule(output1)
n.addOutputModule(output2)

conn1 = FullConnection(input1, hidden1)
conn2 = FullConnection(input1, hidden2)
conn3 = FullConnection(hidden1, hidden3)
conn4 = FullConnection(hidden2, hidden3)
conn5 = FullConnection(hidden3, output1)
conn6 = FullConnection(output1,output2)

n.addConnection(conn1)
n.addConnection(conn2)
n.addConnection(conn3)
n.addConnection(conn4)
n.addConnection(conn5)
n.addConnection(conn6)

n.sortModules()

trainer = BackpropTrainer( n, dataset=train, momentum=0.1, learningrate=0.02 , verbose=True) 

#trainer.trainUntilConvergence()
#NetworkWriter.writeToFile(n, 'g2p_10.xml')
trainer.trainEpochs(500)
print 'Percent Error on Test dataset: ' , percentError( trainer.testOnClassData (dataset=test ), test['target'] )













'''
x = test['input'][0]
y = n.activate(x)

print "output " ,
print y

print "expected  ",
print test['target'][0]
'''


