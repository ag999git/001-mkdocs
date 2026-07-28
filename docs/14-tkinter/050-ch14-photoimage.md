



# Research / Project Question

## Investigating Image Persistence in Tkinter (`PhotoImage` Bug)

When beginners use images in Tkinter, they sometimes observe a strange problem:

> The image either **does not appear** or **disappears suddenly**, even though the code appears correct.

This is one of the most common beginner issues in Tkinter applications.

### Your Task

Research and explain **why images sometimes disappear when using `PhotoImage()` in Tkinter**.

Your answer must include the following sections:

### Part A — Theory (Research Component)

Explain the following concepts:

1.  What is `PhotoImage()` in Tkinter?
2.  Which widgets can display images?
3.  Why does the image sometimes disappear?
4.  What is **garbage collection** in Python?
5.  Why is storing the image in a variable important?
6.  Explain the difference between:

#### Incorrect approach

```python
image=tk.PhotoImage(file="pic.png")
```

#### Correct approach

```python
img = tk.PhotoImage(file="pic.png")
```

7.  Write **three rules/best practices** for displaying images in Tkinter.

----------

### Part B — Script Writing

Write a Tkinter program that:

1.  Creates a GUI window.
2.  Loads an image using `PhotoImage()`.
3.  Displays the image inside a `Label` widget.
4.  Stores the image in a variable so that it remains visible.
5.  Displays a text caption below the image.
6.  Includes meaningful comments using `#`.

Assume that an image file named:

```python
flower.png
```

is present in the same folder as the Python program.

----------

### Part C — Reflection

Answer the following:

> What would happen if the image were not stored in a variable?

Explain briefly.

----------

# Answer (Theory/ Write-up)

## Understanding `PhotoImage()` Persistence in Tkinter

Tkinter allows images to be displayed in GUI applications using the `PhotoImage()` class.

Images can be shown inside widgets such as:

-   `Label`
-   `Button`
-   `Canvas`

Example:
```python
img = tk.PhotoImage(file="flower.png")
```

This loads an image into memory.



## The Common Beginner Problem

Sometimes the image:
- does not appear. or
- appears briefly and disappears even though the code looks correct.

Example of problematic code:

```python

label = tk.Label(root, image=tk.PhotoImage(file="flower.png")) 
```
Why? Because:

```python
Image created→ No variable stores it→ Python removes object from memory→ Image disappears
```

This automatic memory cleanup is called:



## What is Garbage Collection?

Python automatically removes unused objects from memory to save resources. If an object is not referenced by any variable: Python assumes it is no longer needed and deletes it.

This causes problems with `PhotoImage()` if the image object is not stored properly.

## Correct Solution

Always store the image in a variable.

Correct approach:

```python
img = tk.PhotoImage(file="flower.png")
```
Then attach it to a widget. Example:

```python
label = tk.Label(root, image=img)
```

Now Python keeps the image alive because:
```python
variable img still references it
```

## Best Practices

1.  Always store `PhotoImage()` in a variable.
2.  Keep image files in the same folder as the script.
3.  Use meaningful variable names such as: `logo_imgprofile_imgflower_img`

instead of something like: `img_temp1`

----------

# Model Script Solution

```python

import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Tkinter Image Demo")

# Create a frame to hold image + caption
# frame is like a container to group widgets together
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Create tiny image in code (50 × 50)
img = tk.PhotoImage(width=50, height=50)

# Fill image with color
img.put("lightblue", to=(0, 0, 50, 50))

# Display image
# Note: The image object (img) must be kept referenced in the code because Tkinter 
# needs it to display the image. If we create the image inside the Label without 
# keeping a reference, it may not show up.
img_label = tk.Label(frame,
                     image=img)

img_label.pack()

# Caption below image 
# We ensure the caption is created after the image and is packed below it in the frame.
caption = tk.Label(frame,
                   text="Generated Image")

caption.pack(pady=5)  # No padx needed since it's centered in the frame

# Start GUI
root.mainloop()

```


## Expected Output
A window opens displaying:

```
Flower Image

(The actual picture depends on the image file used.)
```

## Reflection Answer

If the image is not stored in a variable:

>Python may remove it from memory

through **garbage collection**, causing the image to disappear or fail to display.

Therefore:

> **Always store `PhotoImage()` in a variable before displaying it in Tkinter.**






















