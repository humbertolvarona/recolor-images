from PIL import Image
import numpy as np
import matplotlib.cm as cm

def is_gray(pixel, tol=16):
    return abs(int(pixel[0]) - int(pixel[1])) < tol and \
           abs(int(pixel[1]) - int(pixel[2])) < tol and \
           abs(int(pixel[0]) - int(pixel[2])) < tol

def adjust_contrast(arr, contrast=1.0):
    factor = (259 * (contrast + 255)) / (255 * (259 - contrast))
    return np.clip(factor * (arr - 128) + 128, 0, 255)

def recolor_except_gray(input_path, output_path, colormap_name='YlOrBr',
                        tol=16, invert_colors=False, brightness=1.0,
                        contrast=1.0,
                        reinforce_blacks=True, black_threshold=40,
                        reinforce_whites=False, white_threshold=215):
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
    recolored = cmap(luminance_norm)[..., :3] * 255
    recolored = adjust_contrast(recolored, contrast)
    recolored = recolored * brightness
    recolored = np.clip(recolored, 0, 255).astype(np.uint8)

    output_arr = arr.copy()
    output_arr[~gray_mask] = recolored[~gray_mask]

    if reinforce_blacks:
        black_mask = luminance < black_threshold
        output_arr[black_mask] = [0, 0, 0]

    if reinforce_whites:
        white_mask = luminance >= white_threshold
        output_arr[white_mask] = [255, 255, 255]

    output_img = Image.fromarray(output_arr)
    output_img.save(output_path)
                            
