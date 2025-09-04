class SeedSSManager:
    """
    A ComfyUI custom node for saving and restoring random seeds.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 2**31}),
                "label": ("STRING", {"default": "default"}),
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "snapshot"
    CATEGORY = "Utilities/Seed"

    def __init__(self):
        self.snapshots = {}

    def snapshot(self, seed: int, label: str = "default"):
        """Save or restore a seed value."""
        self.snapshots[label] = seed
        print(f"[SeedSSManager] Stored seed {seed} under label '{label}'")
        return (seed,)


# Register the node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "SeedSSManager": SeedSSManager,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SeedSSManager": "Seed SS Manager",
}

# Tell ComfyUI to also load frontend assets from the "web" folder
WEB_DIRECTORY = "web"