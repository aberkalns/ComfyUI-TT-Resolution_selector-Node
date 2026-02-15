# ComfyUI TT Resolution Selector Plugin

A simple and practical ComfyUI plugin that provides a dropdown selection function for commonly used resolutions.

## Features

- 🎯 Offers 20+ commonly used resolution presets with annotations for landscape/portrait/square orientation
- 📐 Includes multiple aspect ratios: 1:1, 2:3, 3:2, 4:7, 7:4, 16:9, 9:16, etc.
- �️ Supports custom resolution input
- �🔄 Returns standard integer values ​​for width and height
- 🎨 Suitable for image generation, processing, and other scenarios

## Supported Resolutions

### Square (1:1)
- 512x512 (1:1) (Square)
- 768x768 (1:1) (Square)
- 1024x1024 (1:1) (Square)

### Portrait Aspect Ratio
- 512x768 (2:3) (Portrait)
- 512x896 (4:7) (Portrait)
- 640x960 (2:3) (Portrait)
- 832x1216 (13:19) (Portrait)
- 1024x1536 (2:3) (Portrait)
- 720x1280 (9:16) (Portrait)
- 1080x1920 (9:16) (Portrait)
- 768x1344 (4:7) (Portrait)
- 896x1152 (7:9) (Portrait)
- 2048x3072 (Portrait)
- 480x832 (3:5.2) (Portrait)
- 480x854 (9:16) (Portrait)

### Landscape Aspect Ratio
- 768x512 (3:2) (Landscape)
- 896x512 (7:4) (Landscape)
- 960x640 (3:2) (Landscape)
- 1216x832 (19:13) (Landscape)
- 1536x1024 (3:2) (Landscape)
- 1280x720 (16:9) (Landscape)
- 1920x1080 (16:9) (Landscape)
- 1344x768 (7:4) (Landscape)
- 1152x896 (9:7) (Landscape)
- 3072x2048 (Landscape)
- 832x480 (5.2:3) (Landscape)
- 854x480 (16:9) (Landscape)

## Installation Methods

### Method 1: Direct Download
1. Download all files for this plugin.
2. Copy the entire folder to... In the `ComfyUI/custom_nodes/` directory
3. Restart ComfyUI

### Method 2: Git Cloning
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/yourusername/comfyui-resolution-selector.git
```

## Usage

1. Right-click to add a node in ComfyUI
2. Select `utils` -> `TT Resolution Selector`
3. **Preset Mode**: Directly select the desired resolution from the dropdown menu
4. **Custom Mode**:
   - Turn on the `use_custom_resolution` switch
   - Enter custom values ​​in `custom_width` and `custom_height`
   - The resolution selected from the dropdown will be ignored.
5. The node will output the corresponding width and height values.
6. Connect the output to other nodes that require resolution parameters.

## Output Explanation

- **width**: Image width (integer)
- **height**: Image Height (Integer)

## Update Log

### This fork
- English translation by Google

### v1.1.0
- ✨ Added custom resolution function
- 📝 Optimized resolution list, added landscape/portrait/square annotations
- 🔧 Added custom switch control

### v1.0.0
- Initial version release
- Supports 20+ common resolutions
- Basic dropdown selection function

## Author
- AI Code Hero Potato
