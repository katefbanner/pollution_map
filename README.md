# 🌍 Air Pollution Map  

An interactive web application that visualizes **real-time air pollution data** on a map.  
The project uses a **Python (FastAPI) backend** to fetch and serve pollution data from **OpenAQ** and a **React + Leaflet frontend** to display it in an intuitive map interface.  

---

## ✨ Features  
- 🔎 Search pollution data by **city** or **country**  
- 🗺️ Interactive **map with pollution markers**  
- 🎨 **Color-coded indicators** (green = clean air, red = polluted)  
- 📈 View **historical air quality trends**  
- ☁️ **Heatmap layer** for pollutant concentration  

---

## 🛠️ Tech Stack  
**Backend (API)**  
- Python  
- FastAPI  
- Requests (for external API calls)  

**Frontend (Map UI)**  
- React  
- Leaflet.js  
- Fetch API  

**Data Source**  
- [OpenAQ API](https://openaq.org/)  

---

## 🚀 Getting Started  

### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/air-pollution-map.git
cd air-pollution-map
```
### 2. Backend Setup 
```bash
cd backend
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```
### 3. Run the Server
```bash
uvicorn main:app --reload
```

📂 Project Structure
air-pollution-map/
│── backend/             # FastAPI backend
│   ├── main.py          # API entry point
│   ├── requirements.txt # Python dependencies
│   └── venv/            # Virtual environment (ignored by Git)
│
│── frontend/            # React + Leaflet frontend
│   ├── package.json     # JS dependencies
│   └── src/             # React source code
│
└── README.md

