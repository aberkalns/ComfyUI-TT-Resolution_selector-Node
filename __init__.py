"""
ComfyUI TT Resolution Selector Plugin
TT Common Resolution Selection Plugin
"""

from .nodes.resolution_selector import TTResolutionSelector

# Node mapping
NODE_CLASS_MAPPINGS = {
    "TTResolutionSelector": TTResolutionSelector,
}

# Node display name mapping
NODE_DISPLAY_NAME_MAPPINGS = {
    "TTResolutionSelector": "TT resolution selector",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
