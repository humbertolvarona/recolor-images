# recolor-images

Recolors image pixels except grays using matplotlib colormap with adjustable brightness

![License](https://img.shields.io/badge/License-Creative_Commons_Zero_v1.0_Universal-green)

# Function: recolor_except_gray

Recolors an image by applying a specified matplotlib colormap only to the colored pixels,
while leaving grayscale pixels (including black, white, and shades of gray) untouched.

---

## Requirements

- Python 3.x
- Pillow (`pip install pillow`)
- NumPy (`pip install numpy`)
- Matplotlib (`pip install matplotlib`)

---

## Parameters

- **input_path** (`str`):  
  Path to the source image file. The image should be in a format supported by Pillow (e.g., PNG, JPEG).

- **output_path** (`str`):  
  Path where the recolored image will be saved.

- **colormap_name** (`str`, optional, default: `'YlOrBr'`):  
  The name of a matplotlib colormap to apply to the colored pixels.  
  Examples: `'YlOrBr'`, `'plasma'`, `'viridis'`, `'magma'`, `'turbo'`, `'cividis'`, `'twilight'`, `'nipy_spectral'`, `'cubehelix'`, `'gist_earth'`, `'ocean'`, `'terrain'`.

- **tol** (`int`, optional, default: 16):  
  Tolerance threshold to determine if a pixel is grayscale.  
  Pixels whose RGB channel values differ from each other by less than `tol` are considered grayscale (including blacks, whites, and grays).  
  - Lower `tol` means stricter detection (fewer pixels considered gray).  
  - Higher `tol` means more pixels classified as gray (including some lightly colored ones).  
  Typical range: 5 to 30.

- **invert_colors** (`bool`, optional, default: False):  
  If `True`, the colormap is inverted before application.

- **brightness** (`float`, optional, default: 1.0):  
  Multiplier for brightness of recolored pixels.  
  Values > 1.0 brighten the colors, values < 1.0 darken them.

- **contrast** (`float`, optional, default: 1.0):  
  Adjusts the contrast of the recolored pixels before brightness is applied.  
  Values > 1.0 increase contrast, values < 1.0 decrease contrast.  
  Typical range: 0.5 to 2.0.

- **reinforce_blacks** (`bool`, optional, default: True):  
  If `True`, pixels darker than `black_threshold` are reinforced to pure black.

- **black_threshold** (`int`, optional, default: 40):  
  Luminance threshold below which pixels are considered black/dark enough to reinforce.  
  - Lower values (e.g., 10) reinforce only the very darkest pixels.  
  - Higher values (e.g., 60) reinforce a broader range of dark pixels, making more areas black.  
  Range: 0 to ~80.

- **reinforce_whites** (`bool`, optional, default: False):  
  If `True`, pixels brighter than or equal to `white_threshold` are reinforced to pure white.

- **white_threshold** (`int`, optional, default: 215):  
  Luminance threshold above which pixels are considered white/bright enough to reinforce.  
  - Lower values (e.g., 200) cause more light pixels to be forced to white.  
  - Higher values (e.g., 230) limit reinforcement to only the brightest pixels.  
  Range: ~200 to 255.

---

## Behavior and Effects

- **Grayscale detection (`tol`)**:  
  Controls which pixels remain untouched because they are considered grayscale.  
  A lower `tol` means stricter grayscale detection, preserving fewer pixels as grayscale.  
  A higher `tol` preserves more pixels as grayscale, preventing recoloring of slightly colored pixels near gray.

- **Contrast (`contrast`)**:  
  Modifies the difference between light and dark areas in the recolored pixels before brightness is applied.  
  Increasing contrast (>1.0) makes colors more vivid by making darks darker and lights lighter.  
  Decreasing contrast (<1.0) softens the color differences.

- **Black reinforcement (`black_threshold`)**:  
  Pixels with luminance below this value are set to pure black `[0,0,0]` if `reinforce_blacks` is enabled.  
  Increasing this value makes more pixels appear fully black, which can increase contrast but may lose shadow details.  
  Decreasing it restricts reinforcement to only the deepest blacks.

- **White reinforcement (`white_threshold`)**:  
  Pixels with luminance equal or above this value are set to pure white `[255,255,255]` if `reinforce_whites` is enabled.  
  Lowering this threshold results in a broader range of light pixels becoming white, which can increase highlights but reduce subtlety.  
  Raising it limits the effect to only very bright whites.

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
```

## 📜 License

Creative Commons Zero v1.0 Universal

---

## 🤝 Contributing

Pull requests, ideas, and bug reports are welcome 🙌

---

## 👨‍💼 Maintainer

**HL Varona** — [humberto.varona@gmail.com](mailto:humberto.varona@gmail.com)
