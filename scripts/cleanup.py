from os import path, rename

image_string = "img_"

with open('index.md') as f:
    lines = f.read().splitlines()

new = []
img_counter = 1

for line in lines:
    # Ignore line if images are present
    if not '![' in line:
        new.append(line)
        continue

    images = line.split('![')
    for image in images:
        # Ignore section if no brackets are present
        if not ("(" in image and ")" in image):
            continue
        
        start = image.index( "(" ) + 1
        end = image.index( ")", start )
        image_name = image[start:end]

        # Check if the file exists
        if not (path.exists(image_name) and path.exists('fullsize/'+image_name)):
            continue

        # Generate the extension:
        ext = image_name.split(".")[-1]
        
        # Create the new name
        image_new_name = f"{image_string}{img_counter:03}.{ext}"
        img_counter = img_counter + 1

        # Fix the line
        line = line.replace(image_name, image_new_name)

        # Rename the files
        rename(image_name, image_new_name)
        rename("fullsize/"+image_name, "fullsize/"+image_new_name)

    # Add the modified line to the new list
    new.append(line)

for i in new:
    print (i)

with open('index.md', 'w') as f:
    for line in new:
        f.write(f"{line}\n")