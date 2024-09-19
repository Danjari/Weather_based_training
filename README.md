# Weather_based_training
This Streamlit app provides exercise recommendations based on the current weather. By entering your location, it fetches real-time weather data and suggests either indoor or outdoor workouts using the OpenWeatherMap and ExerciseDB APIs, including GIFs of exercises


## Longer Description
The **Weather-Based Workout Planner** is a Streamlit app that provides personalized exercise recommendations based on the current weather conditions of the user's location. By entering a city name, the app fetches real-time weather data and suggests whether you should do indoor or outdoor exercises, along with a list of recommended workouts. The app also displays GIFs for visual guidance on the exercises. It’s perfect for anyone who wants to stay active while adjusting their workouts according to the weather.

## Features
- Fetches real-time weather data using OpenWeatherMap API.
- Suggests exercises based on current weather conditions (indoor or outdoor).
- Provides GIFs of exercises to guide users in their workouts.
- Simple and intuitive user interface built with Streamlit.

## APIs Used
### 1. **OpenWeatherMap API**
- **Purpose:** To fetch real-time weather data based on the user's location.
- **Why Chosen:** OpenWeatherMap provides a good weather service with detailed real-time data, which is crucial for determining whether the user should exercise indoors or outdoors.( and it was the first one I found )

### 2. **ExerciseDB API**
- **Purpose:** To provide a wide range of exercises, categorized by type (indoor/outdoor) and body parts, along with associated equipment and GIFs for demonstration.
- **Why Chosen:** ExerciseDB offers an extensive database of exercises with clear visuals, allowing users to get personalized workout recommendations. (recommended by Chat GPT)

## How to Use the App
1. **Enter Location:** Type the name of your city (e.g., "London" or "New York") in the text input field.
2. **Get Recommendations:** Click the "Get Workout Recommendations" button.
3. **View Results:** The app will display the current weather in your location and recommend whether to do indoor or outdoor exercises.
4. **Follow Workouts:** You'll see a list of suggested exercises with the following details:
    - **Exercise Name**
    - **Targeted Muscle Group**
    - **Type of Exercise (indoor/outdoor)**
    - **Equipment Required**
    - **GIF for Exercise Demonstration**

## Prerequisites
Before using the app, you'll need to set up the following:

### API Keys
You will need to sign up for API keys from both OpenWeatherMap and ExerciseDB (via RapidAPI).

1. **OpenWeatherMap API Key:**
   - Sign up for a free API key at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).
   
2. **ExerciseDB API Key:**
   - Create a free account on [RapidAPI](https://rapidapi.com) and subscribe to the **ExerciseDB API** to obtain an API key.

### Local Setup Instructions
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/weather-based-workout-planner.git
   cd weather-based-workout-planner
   ```
2. **Install Required Libraries:**
  Make sure you have Python installed. Then install the dependencies using the following command:
  ```bash
  pip install -r requirements.txt
  ```
3. **	Add Your API Keys:**
  Create a file called .env in the project directory and add your API keys:
  ```bash
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
EXERCISEDB_API_KEY=your_exercisedb_api_key
```
4. Run the Streamlit App:
   ```bash
   streamlit run app.py

THIS PROJECT IS FOR A CLASS. HAD FUN DOING IT THOUGH. 
