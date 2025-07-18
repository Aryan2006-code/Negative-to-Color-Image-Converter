<h1 align="center">🖼️ Negative to Color Image Converter (Console-based in Python) 🎨</h1>

A lightweight console-based image converter that takes **photo negatives** and converts them into beautiful, realistic color-positive images using **OpenCV**.

Perfect for those scanned old-school photo strips or digital negatives you want to bring back to life.

---

## 🚀 Features

✅ Convert Any Negative – Supports `.jpg`, `.jpeg`, `.png`, etc.  
🧠 Simple Logic – One-line pixel inversion using NumPy  
💾 Auto Save – Saves the converted image in the same folder  
💻 Tech Stack – Built using Python + OpenCV  
🧪 Tested on Windows and Linux

---

## 💻 Tech Stack

| Component     | Tech Used        |
|---------------|------------------|
| Language      | Python 3.8+      |
| Image Lib     | OpenCV (`cv2`)   |
| Interface     | Console (CLI)    |

---

## 🗂️ File Structure

📁 neg_conv
- ├── negative.py # Python script for conversion
- ├── sample_input.jpg # Sample input image (rename your image to this)
- ├── sample_output.jpg # Output image after conversion
- └── README.md # Project documentation


---

## 📌 Sample Usage

### 🎮 Run the Script

--------------------Negative to Color Converter--------------------

Loading image...

✅ Image loaded successfully!

🎨 Converting...

✅ Saved positive image as: positive.jpg


---

## 🔍 Behind the Scenes

The conversion is done using this logic:

''python
positive = 255 - negative

That’s all it takes to invert colors and recreate the original look!

---

## 🚨 Known Issues

🐛 Does not auto-detect grayscale or incorrectly scanned negatives

🖼️ Output may need further color correction (especially old film scans)

---

## 🔮 Future Scope
✨ Add GUI (Tkinter or PyQT version)

📈 Batch conversion of multiple negatives

🌈 Optional color correction (CLAHE, gamma adjustment)

📂 Save to custom folder

---

## 🧑‍💻 Author
Aryan Kumar Prajapati

---


## 🙌 Help Wanted!
If you’re into image processing or OpenCV, feel free to:

⚒️ Suggest optimizations

🐞 Fix bugs or edge cases

🚀 Add a GUI mode or batch processing

Pull requests are welcome!

---

## 📜 License
This project is open-source and free to use under the MIT License.

⭐ Found it useful or fun? Give it a star and share it with your friends!
