# AI Running Coach 🏃‍♂️💨

A Python command-line tool that fetches real-time weather data for any city and uses Google's Gemini AI to analyze if the conditions are optimal for running based on temperature, humidity, and wind.

## Prerequisites
* Python 3 installed
* A free [Google Gemini API Key](https://aistudio.google.com/)
* A free [OpenWeather API Key](https://openweathermap.org/api)

## Setup Instructions

**1. Clone the repository**
```bash
git clone [https://github.com/Astra7-3/ai-running-coach.git](https://github.com/Astra7-3/ai-running-coach.git)
cd ai-running-coach
```
2. Install required libraries

```Bash
pip install google-genai requests rich
```
3. Configure API Keys
Open run_mumbai.py in a text editor. Locate the API key variables near the top of the file and replace the placeholder text with your actual keys:
```Python
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_KEY_HERE")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "YOUR_WEATHER_KEY_HERE")
```
**Usage
Run the script from your terminal:

```Bash
python run_mumbai.py

