from PIL import Image
import skimage
import numpy as np


def img_preprocessing(img):
  x_t = Image.fromarray(img)
  area = (0, 20, 160 , 196)
  x_t = np.asarray(x_t.crop(area)) # crop image
  x_t = skimage.color.rgb2gray(x_t) # srayscale
  x_t = skimage.transform.resize(x_t,(80,80)) # scale
  x_t = skimage.exposure.rescale_intensity(x_t, out_range=(0, 255))
  x_t = x_t/255.

  return x_t


def frames_preprocessing(frames):
  """
  * Preprocessing a stack of frames
  * Stacking them into tensor
  * Return tensor
  """
  frames_preproc = [img_preprocessing(frame) for frame in frames]

  s_t = np.stack(frames_preproc, axis=2)
  s_t = s_t.reshape(1, s_t.shape[0], s_t.shape[1], s_t.shape[2])

  return s_t