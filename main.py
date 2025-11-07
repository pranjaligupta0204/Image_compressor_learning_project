from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Select image
file_path = askopenfilename(title="Select an image")
img = Image.open(file_path)

# Resize
width, height = img.size
new_width = int(width * 0.5)
new_height = int(height * 0.5)
img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

# Save 
save_path = asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
img.save(save_path, "JPEG", optimize=True, quality=60)

print("Image compressed and saved successfully!")
