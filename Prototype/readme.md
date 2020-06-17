# How to execute:
Just download this directory and run using the following command in terminal:

python3 main.py

# Dependencies:
pip install opencv-python

pip install posix_ipc


# Example (5 Blocks):
The current example has a color filter and edge detector which read from the same wire on which the camera writes. Then both the color filter and the edge detector write to wires that are read and displayed by the screen block.
