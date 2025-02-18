# ✈️ Travel Agent – AI-Powered Trip Planning Assistant  

**A CrewAI Multi-Agent system that helps travelers organize personalized travel plans by recommending transportation, hotels, clothing, activities, and more.**  

## 📌 Overview  
Travel Agent is an **AI-driven travel planning assistant** built using **CrewAI Multi-Agent System**. It automates trip organization by finding the best **transportation, accommodations, activities, and local attractions** while also providing **clothing recommendations based on the weather** and a **brief history of the destination**. The system generates a **comprehensive travel report** tailored to the user’s preferences.  

## 🔥 Key Features  
✅ **Personalized Transportation Search** – Finds the best **flights, trains, or driving options** based on user input.  
✅ **Smart Hotel Recommendations** – Suggests accommodations based on **price, quality, and user preferences**.  
✅ **Weather-Based Clothing Advice** – Provides **packing recommendations** for the trip.  
✅ **Activity Finder** – Generates personalized itineraries with:  
   - 🎭 Museums & historic sites  
   - 🍽️ Restaurants, bars, and coffee shops  
   - 🌊 Unique activities (surfing, fishing, hiking, etc.)  
✅ **Destination Briefing** – Provides a **short history of the destination**.  
✅ **Comprehensive Travel Report** – Summarizes all findings into an easy-to-read document.  

## 🏗️ Tech Stack  
- **AI Framework:** CrewAI (Multi-Agent System)  
- **Programming Language:** Python  
- **APIs & External Data:** Uses **travel, weather, and accommodation APIs** to retrieve real-time information  
- **Data Processing:** Pandas, NumPy  
- **Report Generation:** Markdown/PDF output for a detailed travel itinerary  

## 🛠️ Installation & Setup  
### **Clone the repository:**  
```sh
git clone https://github.com/MozartofCode/travel-agent.git
cd travel-agent
```

### **Set up a virtual environment (optional but recommended):**  
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

### **Install dependencies:**  
```sh
pip install -r requirements.txt
```

### **Run the Travel Agent System:**  
```sh
python travel_agent.py
```

## 🎯 How It Works  
1️⃣ **User inputs trip details** (destination, dates, budget, preferences).  
2️⃣ The AI system finds **transportation, hotels, and activities** based on the user’s input.  
3️⃣ It **analyzes weather data** and provides **clothing recommendations**.  
4️⃣ It compiles **a travel report**, including a **brief history of the location**.  

## 🚧 Future Enhancements  
🔹 **Real-Time Pricing & Booking Integration** – Connect with APIs to fetch real-time prices and allow direct bookings.  
🔹 **AI Chatbot for Travel Planning** – Add a conversational assistant for interactive trip planning.  
🔹 **Multi-User Support** – Allow multiple travelers to plan a trip together.  
🔹 **Custom Travel Preferences** – Enable users to specify **dietary restrictions, activity levels, and interests**.  
