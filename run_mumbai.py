import os
import requests
import argparse
from google import genai
from rich.console import Console
from rich.markdown import Markdown

console = Console()

# Keep your existing keys here
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_KEY_HERE")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "YOUR_WEATHER_KEY_HERE")
def get_weather(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "temp_c": data['main']['temp'],
            "humidity": data['main']['humidity'],
            "wind_kph": round(data['wind']['speed'] * 3.6, 1),
            "feelslike_c": data['main']['feels_like'],
            "condition": data['weather'][0]['description']
        }
    return None

def main():
    parser = argparse.ArgumentParser(description="AI running climate analyzer.")
    parser.parse_args()

    # Pause the terminal to ask the user for a city
    user_city = input("Enter a city to analyze for running (e.g., Tokyo, London, Delhi): ")

    console.print(f"\n[bold cyan]Fetching real-time weather data for {user_city}...[/bold cyan]")
    
    data = get_weather(user_city)
    if not data:
        console.print(f"[bold red]Failed to fetch weather data for '{user_city}'. Check the spelling or your API key.[/bold red]")
        return

    weather_report = f"- {user_city}: {data['temp_c']}°C (Feels like {data['feelslike_c']}°C), Humidity: {data['humidity']}%, Wind: {data['wind_kph']} kph, Condition: {data['condition']}\n"

    # The AI prompt now uses your dynamically typed city
    prompt = f"""
    You are an expert running coach. Here is the current weather data for {user_city}:
    {weather_report}
    
    Based on the temperature, humidity, wind, and conditions, is it a good time for a run right now in this location? 
    Explain why, taking into account how high humidity and temperature affect running performance. Keep your answer under 150 words.
    """
console.print("[bold cyan]Analyzing conditions with AI...[/bold cyan]\n")
    
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=prompt
        )
        console.print(Markdown(response.text))
    except Exception as e:
        console.print(f"[bold red]The AI server is currently busy or unavailable. Please try again later.\nDetails: {e}[/bold red]")

if __name__ == "__main__":
    main()