# MAIN IDEA
Main idea is to make alg that would sort every row based on the "gravity force" to a certain point
* Distance is measured as normal distance, taking pixel coords
* "Weight" is measured by the color of the pixel

# Build
Built EXE-file is in directory "dist" of the project. Compiled with "PyInstaller".

# How to use
* Add the image you want to edit to the directory with executable you're going to use (start.py or exe)
* Enter a formula to measure "weigth" in weigthmeasure.txt (in the same folder). Use only r, g, b variables and write it in one line
* Start the algorithm (with start.py or exe)
* Select a point that will be the "center" one

Finally, you will get a new image. If it doesn't work, try playing around with formulas: probably, you wrote smth wrong or the file you're looking for cannot be opened
