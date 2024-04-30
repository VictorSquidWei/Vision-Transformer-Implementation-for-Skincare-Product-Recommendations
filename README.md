# Vision-Transformer-Implementation-for-Skincare-Product-Recommendations


This repository contains the source code for a skin condition analysis application, built using PyTorch and Tkinter. The application provides a user-friendly GUI where users can upload images of skin conditions, and the model predicts whether the condition is related to bags, redness, or acne. Based on the prediction, the application recommends specific skincare products tailored to treat the identified condition, leveraging a trained Vision Transformer model for accurate predictions.

## Repository Contents
- `Glowbot(1).ipynb`: Jupyter notebook detailing the process of training, validating, and testing the model on skin condition images.
- `glowbot.py`: Python script for the GUI application that uses the trained model to perform predictions and display skincare product recommendations.
- `vision_transformer_architecture.png`: Visual representation of the model architecture

## How to Run the Application

First step is always to run the `glowbot(1).ipynb` file and export the model, the file name will be - `full_model.pth`

### Running the Python Script Directly

To run the application directly from the Python script, follow these steps:

1. Ensure Python 3.8 or higher is installed on your system.
2. Install required dependencies:
   ```bash
   pip install torch torchvision pillow tkinter
3. Place the full_model.pth file in the same directory as the glowbot.py script.
4. Run the script:
     ```bash
   python glowbot.py

This will open the GUI where you can upload an image and receive predictions and recommendations.

### Building and Running the Executable

To build an executable from the Python script using PyInstaller, follow these steps:

1. Install PyInstaller if not already installed:
    ```bash
    pip install pyinstaller
2. Navigate to the directory containing glowbot.py.
3. Run PyInstaller to create the executable:
    ```bash
    pyinstaller --onefile --windowed glowbot.py
4. Once the build process is complete, find the executable in the dist directory.
5. Run the executable directly by double-clicking on it in the dist directory. Ensure full_model.pth is in the same directory as the executable for it to function correctly.

## Notes
- The application has been tested on Windows 10 and macOS, but should be compatible with any operating system that supports Python and the required libraries.
- Make sure the image uploaded is in JPEG or PNG format for best results.
