# 📧 Mail Merge Automation Project 🚀  

**Automate personalized letters effortlessly!** This project reads a list of names, customizes a template letter for each person, and saves the ready-to-send letters in a designated folder. 📝✨  

## 🎯 Features  
✅ **Reads Names** from a file 📝  
✅ **Uses a Template Letter** 📝  
✅ **Personalizes Each Letter** with the recipient’s name 👤  
✅ **Saves Ready-to-Send Letters** 📂  

---

## 🛠 How It Works  
1⃣ **Reads names** from `invited_names.txt`  
2⃣ **Opens the template letter** from `starting_letter.txt`  
3⃣ **Replaces** `[name]` in the template with actual names  
4⃣ **Generates a unique letter** for each person 📩  
5⃣ **Saves** the personalized letters in `Output/ReadyToSend/`  

---

## 📂 Project Structure  
```
📁 Mail Merge Project Start  
 ├── 📂 Input  
 │   ├── 📝 invited_names.txt  (List of names)  
 │   └── 📝 starting_letter.txt (Template letter)  
 │  
 ├── 📂 Output  
 │   ├── 📂 ReadyToSend  
 │       ├── 📝 letter_for_JohnDoe.txt  
 │       └── 📝 letter_for_JaneDoe.txt  
 │  
 └── 📝 main.py  (The automation script)  
```

---

## 🏃‍♂️ How to Run  
1⃣ **Ensure all input files exist** (names & template letter) 💑  
2⃣ Run the script:  
```sh
python main.py
```
3⃣ Check the **`Output/ReadyToSend/`** folder for your personalized letters! 📬  

---

## 🎉 Example Output  
📝 **Template Letter (starting_letter.txt)**  
```
Dear [name],  

We are pleased to invite you to our special event! 🎉  

Best regards,  
The Event Team
```

📝 **Generated Letter (letter_for_John.txt)**  
```
Dear John,  

We are pleased to invite you to our special event! 🎉  

Best regards,  
The Event Team
```

---

## 🤖 Technologies Used  
- 🐍 **Python**  
- 📂 **File Handling** (`open()`, `read()`, `write()`)  
- 🔄 **String Replacement** (`replace()`)  

---

## 🚀 Future Enhancements  
✨ Add **email sending functionality** 📧  
✨ Customize letters with **dynamic fields** 📝  
✨ Add **error handling** for missing files ⚠️  

---

🎯 **Enjoy Automating!** 🎯  

💙 Made with Python & Love 🐍📩  

