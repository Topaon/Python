from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn import neighbors
import numpy as np
import matplotlib.pyplot as plt

#import du dataset
mnist = fetch_openml('mnist_784', version = 1, parser = 'auto')

#échantillonnage
sample = np.random.randint(70000, size = 5000)
data = mnist.data.iloc[sample]
target = mnist.target.iloc[sample]

xtrain, xtest, ytrain, ytest = train_test_split(data, target, train_size = 0.8)
print(type(xtrain))

#recherche du K optimal (en l'occurence on gardera 4)
errors = []

for k in range(2,15):
    knn = neighbors.KNeighborsClassifier(k)
    errors.append(100*(knn.fit(xtrain, ytrain).score(xtest, ytest)))

#affichage de quelques réponses
knn = neighbors.KNeighborsClassifier(4)
knn.fit(xtrain, ytrain)

# On récupère les prédictions sur les données test
predicted = knn.predict(xtest)

# On redimensionne les données sous forme d'images
images = xtest.values.reshape((-1, 28, 28))

# On selectionne un echantillon de 12 images au hasard
select = np.random.randint(images.shape[0], size = 12)

# On affiche les images avec la prédiction associée
fig,ax = plt.subplots(3,4)

for index, value in enumerate(select):
    plt.subplot(3,4,index+1)
    plt.axis('off')
    plt.imshow(images[value],cmap=plt.cm.gray_r,interpolation="nearest")
    plt.title('Predicted: {}'.format( predicted[value]) )

plt.show()
