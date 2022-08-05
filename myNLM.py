import os
from skimage import img_as_float, img_as_ubyte
from skimage.restoration import denoise_nl_means, estimate_sigma
from matplotlib import pyplot as plt
from skimage import io
import numpy as np
from skimage.metrics import peak_signal_noise_ratio

def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)

Input_Folder = './JPG_IMAGES/'
Output_Folder = './NLM_IMAGES/'
# reference_ge_image = img_as_float(io.imread('./RECONSTRUCED_JPG_IMAGES/0108.jpg', as_gray=True))
Input_Image_List = os.listdir(Input_Folder)

if os.path.isdir(Output_Folder) is False:
    os.mkdir(Output_Folder)

for i in range(0, len(Input_Image_List)):
    noisy_img = img_as_float(io.imread(Input_Folder + Input_Image_List[i], as_gray=True))

    sigma_est = np.mean(estimate_sigma(noisy_img, multichannel=False))

    NLM_skimg_denoise_img = denoise_nl_means(noisy_img, h=1.15 * sigma_est, fast_mode=True,
                                         patch_size=9, patch_distance=5, multichannel=False)
    # denoise_img_as_8byte = img_as_ubyte(NLM_skimg_denoise_img)
    plt.imsave(Output_Folder + str(i + 1) + '.png', NLM_skimg_denoise_img, cmap='gray')
    print(signaltonoise(noisy_img, axis=None))
    print(signaltonoise(NLM_skimg_denoise_img, axis=None))
    # print(signaltonoise(reference_ge_image, axis=None))
    # plt.imshow(NLM_skimg_denoise_img, cmap='gray')
    # plt.show()