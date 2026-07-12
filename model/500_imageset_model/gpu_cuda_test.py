"""
Purpose:
Used to test CUDA availabilty/integration with PyTorch for local machine
"""

import torch

print(f"Is CUDA available?: {torch.cuda.is_available()}")
print(f"PyTorch CUDA version: {torch.version.cuda}")
print(f"Device Name: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}")