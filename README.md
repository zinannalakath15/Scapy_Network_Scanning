🛰️ ICMP Network Scanner using Scapy

A simple and lightweight network scanning tool created using Python and the Scapy library.
This script scans a given IP range and identifies active hosts by sending ICMP Echo Requests (Ping).
It also measures RTT (Round Trip Time) to show how fast the devices respond.

🔍 Features

✔ Scan a range of IP addresses
✔ Detect live hosts in a network
✔ Display response time (RTT)
✔ Shows UP/DOWN status of each device
✔ Virtual environment support
✔ Beginner-friendly project for cybersecurity learners

🛠️ Technologies Used

Python 3.x

Scapy Library

Virtual Environment (venv)

📡 How It Works

The user defines an IP prefix (ex: 10.10.20.)

Select a start and end host number (ex: 91 to 111)

The script sends ICMP packets to each IP

Hosts that respond → Marked UP

Hosts with no response → Marked DOWN

📁 Project Structure
├── scan.py        # Main scanner script
├── README.md      # Documentation file
└── env/           # Virtual environment (optional)

🧩 Installation & Usage
1️⃣ Clone this repository
git clone https://github.com/<your-username>/scapy-network-scanner.git
cd scapy-network-scanner

2️⃣ Create & activate virtual environment
python -m venv env
.\env\Scripts\activate  # For Windows
# source env/bin/activate  # For Linux/Mac

3️⃣ Install required library
pip install scapy

4️⃣ Run the scanner
python scan.py

📸 Screenshots

Add your output screenshots here 👇

🔹 Code Execution Screenshot

(Insert image here)

🔹 Live Hosts Detected Screenshot

(Insert image here)

🧠 Applications

LAN device discovery

Network monitoring

Ethical hacking practice

ICMP protocol learning

⚠️ Limitations

ICMP traffic may be blocked in some networks

Requires admin/root permission

Slower for large ranges without threading

🚀 Future Improvements

Multi-threaded scanning for better speed

Logging results to files

Add TCP port scanning support

GUI/Web interface

📝 License

This project is open-source and free to use under the MIT License.

👤 Author

Abdul Bayis
Cybersecurity Learner & Python Enthusiast
