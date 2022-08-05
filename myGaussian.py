from skimage import img_as_float
from matplotlib import pyplot as plt
from skimage import io
from scipy import ndimage as nd

noisy_img = img_as_float(io.imread("MRI_noisy.tif"))

gaussian_img = nd.gaussian_filter(noisy_img, sigma=5)
plt.imshow(gaussian_img, cmap='gray')
plt.show()
# plt.imsave("images/MRI_images/Gaussian_smoothed.tif", gaussian_img, cmap='gray')
