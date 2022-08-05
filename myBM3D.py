import os
from skimage import img_as_float
from matplotlib import pyplot as plt
from skimage import io
import bm3d

Input_Folder = './JPG_IMAGES/'
Output_Folder = './BM3D_IMAGES/'

Input_Image_List = os.listdir(Input_Folder)

if os.path.isdir(Output_Folder) is False:
    os.mkdir(Output_Folder)

for i in range(0, len(Input_Image_List)):
    noisy_img = img_as_float(io.imread(Input_Folder + Input_Image_List[i]))
    BM3D_denoised_image = bm3d.bm3d(noisy_img, sigma_psd=0.2, stage_arg=bm3d.BM3DStages.ALL_STAGES)
    plt.imsave(Output_Folder + str(i+1) + '.png', BM3D_denoised_image, cmap='gray')


# plt.imshow(BM3D_denoised_image, cmap='gray')
# plt.show()
