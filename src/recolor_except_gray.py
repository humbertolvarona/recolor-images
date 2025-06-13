from PIL import Image
import numpy as np
import matplotlib.cm as cm

def is_gray(pixel, tol=16):
    return abs(int(pixel[0]) - int(pixel[1])) < tol and \
           abs(int(pixel[1]) - int(pixel[2])) < tol and \
           abs(int(pixel[0]) - int(pixel[2])) < tol

def recolor_except_gray(input_path, output_path, colormap_name='YlOrBr',
                        tol=16, invert_colors=False, brightness=1.0):
    img = Image.open(input_path).convert('RGB')
    arr = np.array(img)
    height, width, _ = arr.shape

    luminance = np.dot(arr[..., :3], [0.299, 0.587, 0.114])
    luminance_norm = (luminance - luminance.min()) / (np.ptp(luminance) + 1e-8)

    if invert_colors:
        luminance_norm = 1.0 - luminance_norm

    gray_mask = np.zeros((height, width), dtype=bool)
    for i in range(height):
        for j in range(width):
            if is_gray(arr[i, j], tol=tol):
                gray_mask[i, j] = True

    cmap = cm.get_cmap(colormap_name)
    recolored = cmap(luminance_norm)[..., :3] * 255 * brightness
    recolored = np.clip(recolored, 0, 255).astype(np.uint8)

    output_arr = arr.copy()
    output_arr[~gray_mask] = recolored[~gray_mask]

    output_img = Image.fromarray(output_arr)
    output_img.save(output_path)
