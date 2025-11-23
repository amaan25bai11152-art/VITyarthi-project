# VITyarthi-project
College Money Manager v2.0 🎓💸

A smart, statistics-driven Command Line Interface (CLI) application designed to help college students track expenses, analyze spending habits, and stick to a monthly budget.

🚀 Overview

College Money Manager goes beyond simple expense tracking. It utilizes basic statistical methods (Standard Deviation) to analyze your spending volatility and predicts a "Safe Spending Limit" for the next day. It features a persistent login system, visual data representation, and report generation.

✨ Key Features

🔐 User Authentication: Secure registration and login system with password protection and auto-generated Student IDs.
💾 Data Persistence: Automatically saves all user profiles and expense history to a local college_data.json file.
🧠 Smart Backfill: Automatically detects if you haven't logged in for a few days and prompts you to fill in missing expenses sequentially.
📊 Statistical Analysis: Calculates:

Total Expenditure

Daily Average

Standard Deviation (spending consistency)

📈 ASCII Visualizer: Generates a text-based bar graph in the console to visualize spending spikes (1 Star ≈ ₹50).
🔮 Predictive Budgeting: Suggests a "Safe Limit" for tomorrow based on your historical spending variance.
📄 Report Export: Exports a detailed receipt of your expenses to a text file ([Name]_report.txt) for external record-keeping.

🛠️ Built With

Language: Python 3.x

Libraries: json, math, random, os (Standard Library - No external pip installs required!)

📦 Installation & Usage

Clone the Repository

git clone [https://github.com/yourusername/college-money-manager.git](https://github.com/yourusername/college-money-manager.git)
cd college-money-manager


Run the Application

python college_manager.py


(Note: Ensure your script file is named college_manager.py or replace with your filename)

Follow the On-Screen Prompts

Register a new account to get your Student ID.
Login using your ID and Password.
Enter the current Date (e.g., if today is the 15th, enter 15).
The system will guide you through the rest!

📂 Project Structure

├── college_manager.py    # Main application source code
├── college_data.json     # Database (Auto-generated on first run)
├── Alice_report.txt      # Example exported report (Auto-generated)
└── README.md             # Project documentation


📸 Example Output

Spending Graph:

--- SPENDING GRAPH ---
(Each * is approx Rs 50)
Day 1: ** (100)
Day 2: **** (200)
Day 3: * (50)
-------------------------


Prediction:

PREDICTION:
Safe limit for tomorrow: Rs 185


🤝 Contributing

Contributions are welcome! If you have ideas for improvements (like adding GUI or Category tagging), feel free to fork the repository and submit a pull request.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License

This project is open source and available under the MIT License.
