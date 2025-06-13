# recolor-images

Recolors image pixels except grays using matplotlib colormap with adjustable brightness

![License](https://img.shields.io/badge/License-MIT-green)

# Function: recolor_except_gray

Recolors an image by applying a specified matplotlib colormap only to the colored pixels,
while leaving grayscale pixels (including black, white, and shades of gray) untouched.

---

## Parameters

- **input_path** (`str`):  
  Path to the source image file. The image should be in a format supported by Pillow (e.g., PNG, JPEG).

- **output_path** (`str`):  
  Path where the recolored image will be saved.

- **colormap_name** (`str`, optional, default: `'YlOrBr'`):  
  The name of a matplotlib colormap to apply to the colored pixels.  
  Examples: `'YlOrBr'`, `'plasma'`, `'viridis'`, `'magma'`, `'inferno'`, `'turbo'`.

- **tol** (`int`, optional, default: 16):  
  The tolerance threshold to consider a pixel grayscale.  
  If the difference between R, G, and B channels is less than `tol`, the pixel is considered grayscale and will not be recolored.

- **invert_colors** (`bool`, optional, default: False):  
  If `True`, the colormap will be inverted before applying.

- **brightness** (`float`, optional, default: 1.0):  
  Multiplier for the brightness of recolored pixels. Values greater than 1.0 brighten colors, less than 1.0 darken them.

---

## Behavior

- The function converts the image to RGB and calculates luminance (grayscale intensity).
- It identifies grayscale pixels by comparing the RGB channels using the tolerance.
- Applies the colormap only to non-grayscale pixels.
- Grayscale pixels, including blacks, whites, and grays, remain unchanged.
- The recolored image is saved to the specified output path.

---

## Example Usage

```python
recolor_except_gray(
    input_path='input_image.jpeg',
    output_path='output_recolored.jpeg',
    colormap_name='plasma',
    tol=10,
    invert_colors=False,
    brightness=1.1
)

## 📜 License

CC0

---

## 🤝 Contributing

Pull requests, ideas, and bug reports are welcome 🙌

---

## 👨‍💼 Maintainer

**HL Varona** — [@humberto.varona@gmail.com](mailto:humberto.varona@gmail.com)
