# streamlit version of the app 
#%%writefile app.py
# app.py

import streamlit as st
import requests
st.set_page_config(page_title="Weather-Based Workout Planner", page_icon="💪", layout="centered")

# OpenWeatherMap API configuration
WEATHER_API_KEY = st.secrets["WEATHER_API_KEY"]  #find a way to hide? DONE
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'


# ExerciseDB API configuration
EXERCISE_URL = 'https://exercisedb.p.rapidapi.com/exercises'
EXERCISE_HEADERS = {
    'x-rapidapi-host': 'exercisedb.p.rapidapi.com',
    'x-rapidapi-key': st.secrets["RAPID_API_KEY"]  # hide DONE
}



def get_weather(location):
    """
    Fetches current weather data for a given location (city name).

    Parameters:
        location (str): The city name, optionally with country code (e.g., 'London,UK').

    Returns:
        dict or None: Weather data if successful, else None.
    """
    params = {
        'q': location,
        'appid': WEATHER_API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    try:
        response = requests.get(WEATHER_URL, params=params)
        response.raise_for_status()  # Raises error for bad status
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching weather data: {e}")
        return None

def determine_workout_type(weather_data):
    """
    Determines whether to suggest indoor or outdoor workouts based on weather data.

    Parameters:
        weather_data (dict): The weather data fetched from OpenWeatherMap.

    Returns:
        str: 'indoor' or 'outdoor'
    """
    if not weather_data:
        return 'indoor'  # Default to indoor if no data

    temp = weather_data['main']['temp']
    weather_conditions = weather_data['weather'][0]['main'].lower()

    # Define your criteria for outdoor workouts
    if 15 <= temp <= 25 and weather_conditions not in ['rain', 'snow', 'storm', 'drizzle']:
        return 'outdoor'
    else:
        return 'indoor'

def get_exercises(workout_type):
    """
    Fetches exercises based on the workout type.

    Parameters:
        workout_type (str): 'indoor' or 'outdoor'

    Returns:
        list: List of exercise dictionaries.
    """
    try:
        response = requests.get(EXERCISE_URL, headers=EXERCISE_HEADERS)
        response.raise_for_status()
        exercises = response.json()

        # Filter exercises based on workout type
        if workout_type == 'outdoor':
            # Example: Choose exercises that don't require equipment
            filtered = [ex for ex in exercises if ex['equipment'].lower() in ['body weight', 'none']]
        else:
            # Example: Choose exercises that might require equipment
            filtered = [ex for ex in exercises if ex['equipment'].lower() not in ['body weight', 'none']]

        return filtered[:10]  # Return top 10 exercises
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching exercises: {e}")
        return []

def main():
   
    
    st.title("💪 Weather-Based Workout Planner")
    st.write("Plan your workouts based on the current weather conditions!")

    # Sidebar
    st.sidebar.header("About")
    st.sidebar.info(
        """
        **Weather-Based Workout Planner** suggests workout routines tailored to the current weather of your location.
        - **Indoor Workouts**: Yoga, Strength Training
        - **Outdoor Workouts**: Running, Cycling,Body Training
        """
    )

    # User Input
    location = st.text_input("Enter your location (city name, e.g., 'London' or 'New York,US'):")

    if st.button("Get Workout Recommendations"):
        if location:
            with st.spinner('Fetching weather data...'):
                weather_data = get_weather(location)

            if weather_data:
                description = weather_data['weather'][0]['description'].title()
                temp = weather_data['main']['temp']
                st.success(f"**Current weather in {location}:** {description}, {temp}°C")
            else:
                st.warning("Unable to fetch weather data. Defaulting to indoor workouts.")

            workout_type = determine_workout_type(weather_data)
            st.info(f"**Recommended workout type:** {workout_type.title()}")

            with st.spinner('Fetching exercises...'):
                exercises = get_exercises(workout_type)

            if exercises:
                st.subheader("Here are some exercises for you:")
                for idx, ex in enumerate(exercises, 1):
                    with st.expander(f"Exercise {idx}: {ex['name'].title()}"):
                        st.markdown(f"**Target Muscle Group:** {ex['target'].title()}")
                        st.markdown(f"**Equipment Needed:** {ex['equipment'].title()}")
                        st.image(ex['gifUrl'], caption=f"Exercise{idx}: {ex['name'].title()}", use_column_width=True)
                        st.markdown("**Instructions:**")
                        for instruction in ex['instructions']:
                            st.markdown(f"- {instruction}")
            else:
                st.warning("No exercises found.")
        else:
            st.error("Please enter a valid city name.")

if __name__ == "__main__":
    main()
