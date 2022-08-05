from skimage import img_as_float
from matplotlib import pyplot as plt
from skimage import io
from skimage.restoration import denoise_wavelet

noisy_img = img_as_float(io.imread("MRI_noisy.tif"))

wavelet_smoothed = denoise_wavelet(noisy_img, multichannel=False,
                                   method='BayesShrink', mode='soft',
                                   rescale_sigma=True)

plt.imshow(wavelet_smoothed, cmap='gray')
plt.show()
