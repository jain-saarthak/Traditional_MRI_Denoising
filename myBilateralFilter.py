from skimage import img_as_float
from matplotlib import pyplot as plt
from skimage import io
from skimage.restoration import denoise_bilateral

noisy_img = img_as_float(io.imread("MRI_noisy.tif"))

denoise_bilateral = denoise_bilateral(noisy_img, sigma_spatial=10,
                                      multichannel=False)

plt.imshow(denoise_bilateral, cmap='gray')
plt.show()
