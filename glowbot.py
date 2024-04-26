import tkinter as tk
from tkinter import Tk, Canvas, filedialog, messagebox
from tkinter.ttk import Button, Label
from tkinter import font as tkFont
import torch
import torchvision.transforms as transforms
from PIL import Image
import os

class SkinApp:
    def __init__(self, master):
        self.master = master
        if master is not None:
            master.title("Skin Condition Analysis")
            master.geometry('800x600')

            self.customFont = tkFont.Font(family="Helvetica", size=16, weight="bold")

            self.canvas = Canvas(master)
            self.canvas.pack(fill='both', expand=True)
            self.canvas.bind("<Configure>", self.set_gradient_background)

            self.label = Label(master, text="Upload an image to analyze skin condition.", font=self.customFont, background='light blue')
            label_window = self.canvas.create_window(400, 150, window=self.label) 

            self.upload_button = Button(master, text="Upload Image", command=self.upload_image, style='TButton')
            upload_button_window = self.canvas.create_window(400, 500, window=self.upload_button)

            self.close_button = Button(master, text="Close", command=master.quit, style='TButton')
            close_button_window = self.canvas.create_window(400, 550, window=self.close_button)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = torch.load('full_model.pth', map_location=self.device)
        self.model.eval()

    def set_gradient_background(self, event=None):
        self.canvas.delete("gradient")
        width = event.width
        height = event.height
        for i in range(height):
            color = "#%02x%02x%02x" % (int(135 - i / height * 135), 
                                       int(206 - i / height * 206),  
                                       int(250 - i / height * 50))   
            self.canvas.create_line(0, i, width, i, fill=color, tags="gradient")
    
    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                prediction = self.predict(file_path)
                product = self.recommend_product(prediction)
                self.label.config(text=f"Prediction: {prediction}\nRecommended products:\n{product})")
            except Exception as e:
                messagebox.showerror("Prediction Error", str(e))

    def predict(self, image_path):
        image = Image.open(image_path).convert('RGB')
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        image = transform(image).unsqueeze(0)
        image = image.to(self.device)

        with torch.no_grad():
            output = self.model(image)
            _, predicted = torch.max(output.data, 1)
            class_names = ['bags', 'redness', 'acne']
            return class_names[predicted.item()]

    def recommend_product(self, condition):
        recommendations = {
            'bags': [
                "The Ordinary: Caffeine Solution 5% + EGCG",
                "SK-II: SKINPOWER Eye Cream",
                "Brickell: RESTORING EYE CREAM FOR MEN",
                "Paula’s Choice: C5 Super Boost Eye Cream",
                "Origins: GINZING™ Vitamin C & Niacinamide Eye Cream To Brighten And Depuff"
            ],
            'redness': [
                "Clinique: Redness Solutions Daily Relief Cream",
                "Paula’s Choice: Regular Strength Anti-Redness Exfoliating Solution With 2% Salicylic Acid",
                "The Ordinary: Soothing & Barrier Support Serum",
                "Musely: The Red Rescue",
                "Neostrata: Redness Neutralizing Serum"
            ],
            'acne': [
                "CeraVe: Renewing SA Cleanser",
                "Paula’s Choice: Extra Strength Kit",
                "Pauls’s Choice: Advanced Illuminate + Smooth Kit",
                "The Ordinary: The balance Set",
                "Exposed Skincare: Basic Kit"
            ]
        }
        return '\n'.join(recommendations.get(condition, ["No recommendations available"]))


if __name__ == '__main__':
    root = Tk()
    app = SkinApp(root)
    root.mainloop()

# def test_predict(app, image_path):
    
#     try:
#         prediction = app.predict(image_path)
#         print(f"Predicted class: {prediction}")
#         print(f"Recommended product: {app.recommend_product(prediction)}")
#     except Exception as e:
#         print(f"Error during prediction: {str(e)}")

# if __name__ == '__main__':
    
#     app = SkinApp(None)

   
#     test_image_path = 'test1.png'

    
    # test_predict(app, test_image_path)
    
    