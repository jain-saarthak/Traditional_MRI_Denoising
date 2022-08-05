from skimage import img_as_float
from matplotlib import pyplot as plt
from skimage import io
from medpy.filter.smoothing import anisotropic_diffusion

noisy_img = img_as_float(io.imread("MRI_noisy.tif"))

img_aniso_filtered = anisotropic_diffusion(noisy_img, niter=50, kappa=50, gamma=0.2, option=2)

plt.imshow(img_aniso_filtered, cmap='gray')
plt.show()
