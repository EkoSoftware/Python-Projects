# python -m pip install rembg
# python -m pip install pillow
from PIL import Image
from rembg import remove
import sys

if not len(sys.argv) > 2:
    print ("Användning: python tabortbakgrund.py infil.png utfil.png")
    exit(1)
    

input_path = sys.argv[1]
output_path =sys.argv[2]

input_img  = Image.open(input_path)
output_img = remove(input_img)

output_img.save(output_path)
print(f"Fil sparad som {output_path}")
exit(0)