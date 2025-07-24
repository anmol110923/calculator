🎓 मेरा IPU – Educational Platform
A student-centric educational platform crafted to provide easy access to syllabus, notes, PYQs, and practical files for classes 6th to 12th. Designed for clarity, accessibility, and simplicity, it supports learners by offering well-structured study material with interactive features.

🌟 Key Features
📚 Class-wise Study Material
Find notes, PYQs, syllabus, and practical files for each class from 6th to 12th.

🎉 Festival Greeting Pop-Ups
Automatically display personalized greetings during festivals via a dynamic pop-up interface.

🖼️ Image-Based Navigation
Navigate through content with visually intuitive icons and responsive resource cards.

⚡ Easy File Access Structure
Study material is neatly organized in folders and accessed through clickable buttons with HTML redirections.

📱 Fully Responsive Design
Built using mobile-first principles to ensure the platform looks great across devices.

🔗 Demo
Live Website

🛠️ How to Run Locally
Clone the Repository

bash
Copy
Edit
git clone https://github.com/tejazmali/educational-website.git  
cd educational-website  
Run via Live Server
Open index.html with Live Server in VS Code.

⚠️ Note: Clicking on class links may not work via file:// path directly due to browser routing limitations. Always use Live Server.

Directory Structure Tip
Ensure folders like /study material/Notes/notes-9th/ exist and contain an index.html to avoid 404 errors.

Customizing Pop-ups
Edit popup.js in root to set your own festival messages:

javascript
Copy
Edit
const popups = [  
  {  
    name: "Diwali",  
    message: "Happy Diwali! Study with light and joy.",  
    date: "2025-10-29"  
  },  
  {  
    name: "New Year",  
    message: "Happy New Year! New goals, new chapters.",  
    date: "2026-01-01"  
  }  
];  
export default popups;  
📁 Folder Structure Overview
pgsql
Copy
Edit
📂 educational-website  
├── 📂 Images  
├── 📂 study material  
│   ├── 📂 Notes  
│   │   └── 📂 notes-9th (→ should contain index.html)  
├── 📄 index.html  
├── 📄 popup.js  
└── 📄 style.css  
📚 Technologies Used
HTML

CSS

JavaScript

Live Server for local testing

👨‍💻 Contributing
We welcome contributors!

Fork the repository

Make your changes in a new branch

Create a pull request with clear commit messages

📜 License
MIT License – Use freely with attribution.

📬 Contact
Have feedback or want to collaborate?
GitHub: @tejazmali
Website: Portfolio

