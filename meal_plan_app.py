import random
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

# Function to fetch nutrient data (dummy data used here for simplicity)
def get_food_nutrients(food):
    nutrients = {
        "Chicken Breast": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
        "Quinoa": {"calories": 222, "protein": 8, "fat": 3.6, "carbs": 39},
        "Mixed Veggies": {"calories": 50, "protein": 2, "fat": 0.5, "carbs": 10},
        "Mixed Greens": {"calories": 5, "protein": 0.5, "fat": 0.1, "carbs": 1},
        "Chickpeas": {"calories": 180, "protein": 10, "fat": 3, "carbs": 30},
        "Cherry Tomatoes": {"calories": 15, "protein": 1, "fat": 0.2, "carbs": 3},
        "Feta Cheese": {"calories": 100, "protein": 5, "fat": 8, "carbs": 1},
        "Overnight Oats": {"calories": 300, "protein": 10, "fat": 8, "carbs": 50},
        "Rice": {"calories": 130, "protein": 2.7, "fat": 0.3, "carbs": 28},
        "Lentils": {"calories": 116, "protein": 9, "fat": 0.4, "carbs": 20},
        "Frozen Veggies": {"calories": 40, "protein": 2, "fat": 0.2, "carbs": 8},
        "Peanut Butter": {"calories": 190, "protein": 8, "fat": 16, "carbs": 6},
        "Bananas": {"calories": 105, "protein": 1.3, "fat": 0.3, "carbs": 27},
        "Oatmeal": {"calories": 150, "protein": 5, "fat": 2.5, "carbs": 27},
        "Eggs": {"calories": 70, "protein": 6, "fat": 5, "carbs": 1},
        "Greek Salad": {"calories": 150, "protein": 4, "fat": 10, "carbs": 11},
        "Tacos": {"calories": 200, "protein": 10, "fat": 12, "carbs": 15},
        "Chicken Curry": {"calories": 250, "protein": 20, "fat": 10, "carbs": 15},
        "Fried Rice": {"calories": 300, "protein": 7, "fat": 12, "carbs": 40},
        "Pho": {"calories": 350, "protein": 15, "fat": 5, "carbs": 60},
        "Souvlaki": {"calories": 250, "protein": 20, "fat": 15, "carbs": 10},
        "Falafel": {"calories": 180, "protein": 6, "fat": 10, "carbs": 15},
        "Moussaka": {"calories": 400, "protein": 20, "fat": 25, "carbs": 25},
        "Enchiladas": {"calories": 300, "protein": 15, "fat": 20, "carbs": 25},
        "Biryani": {"calories": 400, "protein": 20, "fat": 15, "carbs": 50},
        "Dim Sum": {"calories": 150, "protein": 8, "fat": 5, "carbs": 20},
        "Spring Rolls": {"calories": 200, "protein": 5, "fat": 10, "carbs": 25},
        # Add more foods as needed
    }
    return nutrients.get(food, {"calories": 0, "protein": 0, "fat": 0, "carbs": 0})

# Meal plan options
meal_plans = {
    "Weekly Meal Prep for Busy Professionals": {
        "Breakfast": ["Overnight Oats", "Bananas"],
        "Lunch": ["Chicken Breast", "Quinoa", "Mixed Veggies"],
        "Dinner": ["Chicken Breast", "Quinoa", "Mixed Veggies"],
        "Snack": ["Chickpeas", "Cherry Tomatoes"]
    },
    "Budget-Friendly Meal Plans": {
        "Breakfast": ["Oatmeal", "Bananas"],
        "Lunch": ["Rice", "Lentils", "Frozen Veggies"],
        "Dinner": ["Rice", "Lentils", "Frozen Veggies"],
        "Snack": ["Peanut Butter", "Bananas"]
    },
    "Seasonal Meal Planning": {
        "Breakfast": ["Overnight Oats", "Bananas"],
        "Lunch": ["Greek Salad", "Quinoa"],
        "Dinner": ["Chicken Breast", "Quinoa", "Mixed Veggies"],
        "Snack": ["Chickpeas", "Cherry Tomatoes"]
    },
    "Family-Friendly Meal Plans": {
        "Breakfast": ["Overnight Oats", "Bananas"],
        "Lunch": ["Chicken Breast", "Quinoa", "Mixed Veggies"],
        "Dinner": ["Chicken Breast", "Quinoa", "Mixed Veggies"],
        "Snack": ["Chickpeas", "Cherry Tomatoes"]
    },
    "Plant-Based Meal Plans": {
        "Breakfast": ["Overnight Oats", "Bananas"],
        "Lunch": ["Chickpea Salad", "Quinoa", "Mixed Veggies"],
        "Dinner": ["Chickpea Salad", "Quinoa", "Mixed Veggies"],
        "Snack": ["Chickpeas", "Cherry Tomatoes"]
    },
    "Fitness-Focused Meal Plans": {
        "Breakfast": ["Overnight Oats", "Bananas"],
        "Lunch": ["Chicken Breast", "Quinoa", "Mixed Veggies"],
        "Dinner": ["Chicken Breast", "Quinoa", "Mixed Veggies"],
        "Snack": ["Chickpeas", "Cherry Tomatoes"]
    },
    "Quick and Easy Dinner Plans": {
        "Breakfast": ["Overnight Oats", "Bananas"],
        "Lunch": ["Chicken Breast", "Quinoa", "Mixed Veggies"],
        "Dinner": ["Chicken Breast", "Quinoa", "Mixed Veggies"],
        "Snack": ["Chickpeas", "Cherry Tomatoes"]
    },
    "Healthy Snacks and Small Meals": {
        "Breakfast": ["Overnight Oats", "Bananas"],
        "Lunch": ["Chicken Breast", "Quinoa", "Mixed Veggies"],
        "Dinner": ["Chicken Breast", "Quinoa", "Mixed Veggies"],
        "Snack": ["Chickpeas", "Cherry Tomatoes"]
    },
    "Cultural and International Meal Plans": {
        "Breakfast": ["Greek Yogurt", "Bananas"],
        "Lunch": ["Tacos", "Quinoa", "Mixed Veggies"],
        "Dinner": ["Chicken Curry", "Quinoa", "Mixed Veggies"],
        "Snack": ["Chickpeas", "Spring Rolls"]
    },
    "Meal Plans for Dietary Restrictions": {
        "Breakfast": ["Overnight Oats", "Bananas"],
        "Lunch": ["Chicken Breast", "Quinoa", "Mixed Veggies"],
        "Dinner": ["Chicken Breast", "Quinoa", "Mixed Veggies"],
        "Snack": ["Chickpeas", "Cherry Tomatoes"]
    }
}

# Generate meal plan based on selected criteria
def generate_meal_plan(selection):
    selected_plan = meal_plans.get(selection, {})
    meal_plan = {
        "Breakfast": {food: get_food_nutrients(food) for food in selected_plan.get("Breakfast", [])},
        "Lunch": {food: get_food_nutrients(food) for food in selected_plan.get("Lunch", [])},
        "Dinner": {food: get_food_nutrients(food) for food in selected_plan.get("Dinner", [])},
        "Snack": {food: get_food_nutrients(food) for food in selected_plan.get("Snack", [])}
    }
    return meal_plan

# Streamlit app
st.set_page_config(page_title="Customizable Meal Plan Generator", layout="wide")

st.title("Customizable Meal Plan Generator")
st.write("Select your meal plan criteria and generate a customized meal plan with breakfast, lunch, dinner, and snacks.")

# User selection
selection = st.selectbox("Choose your meal plan criteria:", list(meal_plans.keys()))

# Generate and display meal plan
if st.button("Generate Meal Plan"):
    meal_plan = generate_meal_plan(selection)
    st.write(f"Meal Plan: {selection}")
    
    for meal_time, foods in meal_plan.items():
        st.subheader(meal_time)
        for food, nutrients in foods.items():
            st.markdown(f"**{food}**")
            st.write(f"Calories: {nutrients['calories']} kcal")
            st.write(f"Protein: {nutrients['protein']} g")
            st.write(f"Fat: {nutrients['fat']} g")
            st.write(f"Carbs: {nutrients['carbs']} g")
            st.write("---")

