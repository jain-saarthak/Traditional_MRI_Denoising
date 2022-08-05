import h5py
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, img_as_float
from scipy import ndimage as nd
from skimage.restoration import denoise_nl_means, estimate_sigma

# import matplotlib.image as image

f = h5py.File('1meas_MID00014_FID153636_AX_T1.h5', 'r')
# print(list(f.keys()))
dataset = f['reconstruction']
# print(dataset.dtype)    ---------> Why is the dtype float32?
# ans = np.empty([dataset.shape[0], dataset.shape[1], dataset.shape[2]])



# Original
for i in range(dataset.shape[0]):
    kSpaceImage = dataset[i, :, :]
    plt.imshow(kSpaceImage, cmap='gray')
    # plt.imshow(kSpaceImage)
    plt.show()



# Gaussian
# for i in range(dataset.shape[0]):
#     kSpaceImage = np.asmatrix(dataset[i, :, :])
#     kSpaceImage = dataset[i, :, :]
#     # name = 'test' + str(i) + '.tif'
#     # Image.fromarray(kSpaceImage).save(name)
#     # reloaded = np.array(Image.open(name))
#     gaussian_img = nd.gaussian_filter(kSpaceImage, sigma=1)
#     plt.imshow(gaussian_img, cmap='gray')
#     # ans[i] = gaussian_img
#     # plt.imshow(kSpaceImage)
#     plt.show()
#     # print(kSpaceImage.dtype) Correct shape and values seem correct, dtype is float32


# NLM
# for i in range(dataset.shape[0]):
#     kSpaceImage = dataset[i, :, :]
#     sigma_est = np.mean(estimate_sigma(kSpaceImage, multichannel=False))
#     NLM_skimg_denoise_img = denoise_nl_means(kSpaceImage, h=1.15 * sigma_est, fast_mode=True,
#                                              patch_size=9, patch_distance=5, multichannel=False)
#     plt.imshow(NLM_skimg_denoise_img, cmap='gray')
#     plt.show()




# ans_np = np.array(ans)
# print(ans.shape)
# plt.imshow(ans[:,:,:])
# plt.show()
# print(ans_np)


