"""
TT Resolution Selector Node Provides a dropdown selection of 
commonly used resolutions, returning width and height
"""

class TTResolutionSelector:
    """
    TT Resolution Selector Node
    """
    
    # Common Resolution Presets (Name: (Width, Height))
    RESOLUTIONS = {
        "3072x2048 (Landscape)": (3072, 2048),
        "2048x3072 (Portrait)": (2048, 3072),
        "640x960 (2:3) (Portrait)": (640, 960),
        "960x640 (3:2) (Landscape)": (960, 640),
        "832x1216 (13:19) (Portrait)": (832, 1216),
        "1216x832 (19:13) (Landscape)": (1216, 832),
        "1024x1536 (2:3) (Portrait)": (1024, 1536),
        "1536x1024 (3:2) (Landscape)": (1536, 1024),
        "1280x720 (16:9) (Landscape)": (1280, 720),
        "1920x1080 (16:9) (Landscape)": (1920, 1080),
        "720x1280 (9:16) (Portrait)": (720, 1280),
        "1080x1920 (9:16) (Portrait)": (1080, 1920),
        "1344x768 (7:4) (Landscape)": (1344, 768),
        "768x1344 (4:7) (Portrait)": (768, 1344),
        "1152x896 (9:7) (Landscape)": (1152, 896),
        "896x1152 (7:9) (Portrait)": (896, 1152),
        "480x832 (3:5.2) (Portrait)": (480, 832),
        "832x480 (5.2:3) (Landscape)": (832, 480),
        "480x854 (9:16) (Portrait)": (480, 854),
        "854x480 (16:9) (Landscape)": (854, 480),
        "512x512 (1:1) (Square)": (512, 512),
        "768x768 (1:1) (Square)": (768, 768),
        "1024x1024 (1:1) (Square)": (1024, 1024),
        "512x768 (2:3) (Portrait)": (512, 768),
        "768x512 (3:2) (Landscape)": (768, 512),
        "512x896 (4:7) (Portrait)": (512, 896),
        "896x512 (7:4) (Landscape)": (896, 512),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        """
        Define input type
        """
        return {
            "required": {
                "use_custom_resolution": ("BOOLEAN", {"default": False, "label_on": "Turn on customization", "label_off": "Turn off customization"}),
                "resolution": (list(cls.RESOLUTIONS.keys()), {
                    "default": "1024x1024 (1:1) (quare))"
                }),
                "custom_width": ("INT", {"default": 1024, "min": 64, "max": 8192, "step": 1}),
                "custom_height": ("INT", {"default": 1024, "min": 64, "max": 8192, "step": 1}),
            }
        }
    
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "get_resolution"
    CATEGORY = "utils"
    
    def get_resolution(self, use_custom_resolution, resolution, custom_width, custom_height):
        """
        Returns the width and height based on the selected resolution
        
        Args:
            use_custom_resolution (bool): Whether to use a custom resolution
            resolution (str): The selected resolution string
            custom_width (int): The custom width
            custom_height (int): The custom height
            
        Returns:
            tuple: (width, height)
        """
        if use_custom_resolution:
            return (custom_width, custom_height)
            
        width, height = self.RESOLUTIONS.get(resolution, (1024, 1024))
        return (width, height)
