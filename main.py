from PIL import Image

image_path_list = ['enter.png']

image_list = [Image.open(file) for file in image_path_list]

image_list[0].save(
    'test.gif',
    save_all=True,
    append_images=image_list[1:],
    duration=500,
    loop=0
)