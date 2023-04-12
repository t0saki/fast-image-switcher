import os
from PIL import Image, ImageTk
from tkinter import Tk, Label

# Create a window
root = Tk()

# Get a list of image files in the folder "images"
exts = ["jpg", "png", "tif", "tiff", "gif"]
images=[]
folders="images"
for file in os.listdir(folders):
    if file.split(".")[-1].lower() in exts:
        images.append(Image.open(os.path.join(folders, file)))

# Convert the images to Tkinter PhotoImages
tkimages = [ImageTk.PhotoImage(image) for image in images]

# Create labels to display the images
img_labels = [Label(root, image=tkimage) for tkimage in tkimages]

# Pack the labels (but don't show them yet)
for label in img_labels:
    label.pack_forget()

counter = 1
root.title("Image Switcher - " + str(counter))
index = 0

# Create a function to switch between the images
def switch_image():
    global img_labels, counter
    
    # Hide the current image
    current_label = img_labels[counter-1]
    current_label.pack_forget()
    
    # Show the next image
    next_label = img_labels[counter]
    next_label.pack()
    
    # Increment the counter and wrap around if necessary
    counter = (counter + 1) % len(img_labels)
    
    # Change the window title
    root.title("Image Switcher - " + str(counter))


# Show the first image
img_labels[0].pack()

# Bind the key and mouse events to the switch_image function
root.bind("<Key>", lambda event: switch_image())
root.bind("<Button>", lambda event: switch_image())

# Start the main event loop
root.mainloop()
