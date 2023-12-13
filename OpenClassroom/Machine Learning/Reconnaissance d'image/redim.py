from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math

#import des images à modifier
gros = np.array(Image.open("gros.png"))


plt.imshow(gros.reshape(-1,3))
plt.show()

'''def ajuster_image(img_a_ajuster, img_ref):
    coeff = math.floor(len(img_a_ajuster[0]) / len(img_ref[0]))
    colonnes = list(range(0, img_a_ajuster.shape[1]))
    colonnes = colonnes[0::coeff]
    lignes = list(range(0, img_a_ajuster.shape[0]))
    lignes = lignes[0::coeff]

    img_finale = img_a_ajuster[lignes, :, :]
    img_finale = img_finale[:, colonnes, :]

    return img_finale
'''
