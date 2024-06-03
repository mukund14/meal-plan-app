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
        "Breakfast": ["Overnight Oats", "Bananas", "Greek Yogurt", "Oatmeal", "Eggs"],
        "Lunch": ["Chicken Breast", "Quinoa", "Mixed Veggies", "Greek Salad", "Tacos"],
        "Dinner": ["Chicken Breast", "Quinoa", "Mixed Veggies", "Chicken Curry", "Fried Rice"],
        "Snack": ["Chickpeas", "Cherry Tomatoes", "Peanut Butter", "Bananas", "Spring Rolls"]
    },
    "Budget-Friendly Meal Plans": {
        "Breakfast": ["Oatmeal", "Bananas", "Eggs", "Overnight Oats", "Greek Yogurt"],
        "Lunch": ["Rice", "Lentils", "Frozen Veggies", "Chickpeas", "Mixed Veggies"],
        "Dinner": ["Rice", "Lentils", "Frozen Veggies", "Chickpeas", "Mixed Veggies"],
        "Snack": ["Peanut Butter", "Bananas", "Cherry Tomatoes", "Eggs", "Mixed Greens"]
    },
    "Seasonal Meal Planning": {
        "Breakfast": ["Overnight Oats", "Bananas", "Greek Yogurt", "Oatmeal", "Eggs"],
        "Lunch": ["Chicken Breast", "Quinoa", "Mixed Veggies", "Greek Salad", "Falafel"],
        "Dinner": ["Chicken Breast", "Quinoa", "Mixed Veggies", "Moussaka", "Enchiladas"],
        "Snack": ["Chickpeas", "Cherry Tomatoes", "Peanut Butter", "Bananas", "Spring Rolls"]
    },
    "Family-Friendly Meal Plans": {
        "Breakfast": ["Overnight Oats", "Bananas", "Greek Yogurt", "Oatmeal", "Eggs"],
        "Lunch": ["Chicken Breast", "Quinoa", "Mixed Veggies", "Greek Salad", "Tacos"],
        "Dinner": ["Chicken Breast", "Quinoa", "Mixed Veggies", "Chicken Curry", "Fried Rice"],
        "Snack": ["Chickpeas", "Cherry Tomatoes", "Peanut Butter", "Bananas", "Spring Rolls"]
    },
    "Plant-Based Meal Plans": {
        "Breakfast": ["Overnight Oats", "Bananas", "Greek Yogurt", "Oatmeal", "Eggs"],
        "Lunch": ["Chickpea Salad", "Quinoa", "Mixed Veggies", "Greek Salad", "Falafel"],
        "Dinner": ["Chickpea Salad", "Quinoa", "Mixed Veggies", "Moussaka", "Enchiladas"],
        "Snack": ["Chickpeas", "Cherry Tomatoes", "Peanut Butter", "Bananas", "Spring Rolls"]
    },
    "Fitness-Focused Meal Plans": {
        "Breakfast": ["Overnight Oats", "Bananas", "Greek Yogurt", "Oatmeal", "Eggs"],
        "Lunch": ["Chicken Breast", "Quinoa", "Mixed Veggies", "Greek Salad", "Souvlaki"],
        "Dinner": ["Chicken Breast", "Quinoa", "Mixed Veggies", "Chicken Curry", "Fried Rice"],
        "Snack": ["Chickpeas", "Cherry Tomatoes", "Peanut Butter", "Bananas", "Spring Rolls"]
    },
    "Quick and Easy Dinner Plans": {
        "Breakfast": ["Overnight Oats", "Bananas", "Greek Yogurt", "Oatmeal", "Eggs"],
        "Lunch": ["Chicken Breast", "Quinoa", "Mixed Veggies", "Greek Salad", "Tacos"],
        "Dinner": ["Chicken Breast", "Quinoa", "Mixed Veggies", "Chicken Curry", "Fried Rice"],
        "Snack": ["Chickpeas", "Cherry Tomatoes", "Peanut Butter", "Bananas", "Spring Rolls"]
    },
    "Healthy Snacks and Small Meals": {
        "Breakfast": ["Overnight Oats", "Bananas", "Greek Yogurt", "Oatmeal", "Eggs"],
        "Lunch": ["Chicken Breast", "Quinoa", "Mixed Veggies", "Greek Salad", "Tacos"],
        "Dinner": ["Chicken Breast", "Quinoa", "Mixed Veggies", "Chicken Curry", "Fried Rice"],
        "Snack": ["Chickpeas", "Cherry Tomatoes", "Peanut Butter", "Bananas", "Spring Rolls"]
    },
    "Cultural and International Meal Plans": {
        "Breakfast": ["Greek Yogurt", "Bananas", "Oatmeal", "Eggs", "Overnight Oats"],
        "Lunch": ["Tacos", "Quinoa", "Mixed Veggies", "Biryani", "Souvlaki"],
        "Dinner": ["Chicken Curry", "Quinoa", "Mixed Veggies", "Pho", "Dim Sum"],
        "Snack": ["Chickpeas", "Spring Rolls", "Peanut Butter", "Bananas", "Falafel"]
    },
    "Meal Plans for Dietary Restrictions": {
        "Breakfast": ["Overnight Oats", "Bananas", "Greek Yogurt", "Oatmeal", "Eggs"],
        "Lunch": ["Chicken Breast", "Quinoa", "Mixed Veggies", "Greek Salad", "Tacos"],
        "Dinner": ["Chicken Breast", "Quinoa", "Mixed Veggies", "Chicken Curry", "Fried Rice"],
        "Snack": ["Chickpeas", "Cherry Tomatoes", "Peanut Butter", "Bananas", "Spring Rolls"]
    }
}

# Generate weekly meal plan based on selected criteria
def generate_weekly_meal_plan(selection):
    selected_plan = meal_plans.get(selection, {})
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekly_plan = {day: {} for day in days}
    
    for day in days:
        for meal_time in ["Breakfast", "Lunch", "Dinner", "Snack"]:
            foods = selected_plan.get(meal_time, [])
            if foods:
                food = random.choice(foods)
                weekly_plan[day][meal_time] = {food: get_food_nutrients(food)}
    
    return weekly_plan

# Streamlit app
st.set_page_config(page_title="Customizable Weekly Meal Plan Generator", layout="wide")

st.title("Customizable Weekly Meal Plan Generator")
st.write("Select your meal plan criteria and generate a customized weekly meal plan with breakfast, lunch, dinner, and snacks.")

# User selection
selection = st.selectbox("Choose your meal plan criteria:", list(meal_plans.keys()))

# Generate and display meal plan
if st.button("Generate Weekly Meal Plan"):
    weekly_meal_plan = generate_weekly_meal_plan(selection)
    st.write(f"Meal Plan: {selection}")
    
    for day, meals in weekly_meal_plan.items():
        st.header(day)
        for meal_time, foods in meals.items():
            st.subheader(meal_time)
            for food, nutrients in foods.items():
                st.markdown(f"**{food}**")
                st.write(f"Calories: {nutrients['calories']} kcal")
                st.write(f"Protein: {nutrients['protein']} g")
                st.write(f"Fat: {nutrients['fat']} g")
                st.write(f"Carbs: {nutrients['carbs']} g")
                st.write("---")

