import numpy as np
from PIL import Image

# Load the result image
result_image = Image.open("image.png")
result_np = np.array(result_image)

# Ensure the values in the result image are within the valid range [0, 255]
result_np = np.clip(result_np, 0, 255).astype(np.uint8)

# Get the shape of the result image
height, width, channels = result_np.shape

# Generate the first share randomly
share1_np = np.random.randint(0, 256, (height, width, channels), dtype=np.uint8)

# Calculate the second share such that their sum equals the result image
# Use modulo 256 to handle overflow and stay within the range [0, 255]
share2_np = result_np - share1_np

# Convert the arrays back to images
share1_image = Image.fromarray(share1_np)
share2_image = Image.fromarray(share2_np)

# Save the generated shares
share1_image.save('image_file.png')
share2_image.save('hidden_image.png')

# To verify, combine the shares again and save the result
combined_np = share1_np + share2_np
combined_image = Image.fromarray(combined_np)
combined_image.save('verified_result.png')
