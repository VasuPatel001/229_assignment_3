
from matplotlib.image import imread
import matplotlib.pyplot as plt

A = imread("peppers-small.tiff")

plt.imshow(A); plt.savefig('test.png')
