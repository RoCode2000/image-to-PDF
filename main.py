from PIL import Image

image_1 = Image.open(r'/Users/rogerteong/Desktop/Education Transcript/Diploma in CE Year 1.png')
image_2 = Image.open(r'/Users/rogerteong/Desktop/Education Transcript/Diploma in CE Year 2.png')
image_3 = Image.open(r'/Users/rogerteong/Desktop/Education Transcript/Diploma in CE Year 3.png')
image_4 = Image.open(r'/Users/rogerteong/Desktop/Education Transcript/Certificate in Business Transcript.png')

im_1 = image_1.convert('RGB')
im_2 = image_2.convert('RGB')
im_3 = image_3.convert('RGB')
im_4 = image_4.convert('RGB')

image_list = [im_1, im_2, im_3, im_4]

im_1.save(r'/Users/rogerteong/Desktop/Education Transcript/Image to PDF Transcript.pdf', save_all=True, append_images=image_list)