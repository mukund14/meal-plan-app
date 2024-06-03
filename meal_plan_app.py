import random
import streamlit as st

# Function to fetch nutrient data (dummy data used here for simplicity)
def get_food_nutrients(food):
    nutrients = {
        "Chicken Breast": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
        "Quinoa Salad": {"calories": 222, "protein": 8, "fat": 3.6, "carbs": 39},
        "Mixed Veggies": {"calories": 50, "protein": 2, "fat": 0.5, "carbs": 10},
        "Mixed Greens": {"calories": 5, "protein": 0.5, "fat": 0.1, "carbs": 1},
        "Chickpeas": {"calories": 180, "protein": 10, "fat": 3, "carbs": 30},
        "Cherry Tomatoes": {"calories": 15, "protein": 1, "fat": 0.2, "carbs": 3},
        "Feta Cheese": {"calories": 100, "protein": 5, "fat": 8, "carbs": 1},
        "Overnight Oats": {"calories": 300, "protein": 10, "fat": 8, "carbs": 50},
        "Rice and Beans": {"calories": 250, "protein": 9, "fat": 1, "carbs": 50},
        "Lentil Soup": {"calories": 180, "protein": 12, "fat": 2, "carbs": 30},
        "Frozen Veggies Stir-fry": {"calories": 150, "protein": 4, "fat": 2, "carbs": 25},
        "Peanut Butter Toast": {"calories": 190, "protein": 8, "fat": 16, "carbs": 6},
        "Bananas": {"calories": 105, "protein": 1.3, "fat": 0.3, "carbs": 27},
        "Oatmeal": {"calories": 150, "protein": 5, "fat": 2.5, "carbs": 27},
        "Eggs": {"calories": 70, "protein": 6, "fat": 5, "carbs": 1},
        "Greek Salad": {"calories": 150, "protein": 4, "fat": 10, "carbs": 11},
        "Tacos": {"calories": 200, "protein": 10, "fat": 12, "carbs": 15},
        "Chicken Curry": {"calories": 250, "protein": 20, "fat": 10, "carbs": 15},
        "Fried Rice with Tofu": {"calories": 300, "protein": 10, "fat": 10, "carbs": 40},
        "Berries": {"calories": 85, "protein": 1, "fat": 0.5, "carbs": 21},
        "Watermelon": {"calories": 46, "protein": 0.9, "fat": 0.2, "carbs": 12},
        "Oranges": {"calories": 62, "protein": 1.2, "fat": 0.2, "carbs": 15},
        "Apples": {"calories": 95, "protein": 0.5, "fat": 0.3, "carbs": 25},
        "Peaches": {"calories": 59, "protein": 1.4, "fat": 0.4, "carbs": 14},
        "Grapes": {"calories": 62, "protein": 0.6, "fat": 0.3, "carbs": 16},
        "Milk": {"calories": 103, "protein": 8, "fat": 2.4, "carbs": 12},
        "Almond Milk": {"calories": 39, "protein": 1, "fat": 3, "carbs": 2},
        "Cashew Milk": {"calories": 25, "protein": 1, "fat": 2, "carbs": 1},
        "Oat Milk": {"calories": 120, "protein": 3, "fat": 5, "carbs": 16},
    }
    return nutrients.get(food, {"calories": 0, "protein": 0, "fat": 0, "carbs": 0})

# Meal plan options
meal_plans = {
    "Weekly Meal Prep for Busy Professionals": {
        "Breakfast": ["Overnight Oats", "Bananas", "Greek Yogurt", "Oatmeal", "Eggs"],
        "Lunch": ["Quinoa Salad with Chickpeas", "Chicken Breast with Mixed Veggies", "Greek Salad with Feta", "Tacos"],
        "Dinner": ["Chicken Curry with Rice", "Fried Rice with Tofu", "Lentil Soup with Mixed Greens"],
        "Snack": ["Chickpeas", "Cherry Tomatoes", "Peanut Butter Toast", "Berries"]
    },
    "Budget-Friendly Meal Plans": {
        "Breakfast": ["Oatmeal with Berries", "Bananas", "Eggs", "Overnight Oats", "Greek Yogurt"],
        "Lunch": ["Rice and Beans", "Lentil Soup", "Frozen Veggies Stir-fry with Tofu", "Chickpeas and Mixed Veggies"],
        "Dinner": ["Rice and Beans", "Lentil Soup", "Frozen Veggies Stir-fry with Tofu", "Chickpeas and Mixed Veggies"],
        "Snack": ["Peanut Butter Toast", "Bananas", "Cherry Tomatoes", "Mixed Greens"]
    },
    "Seasonal Meal Planning": {
        "Breakfast": ["Overnight Oats", "Bananas", "Greek Yogurt", "Oatmeal with Berries", "Eggs"],
        "Lunch": ["Quinoa Salad with Chickpeas", "Chicken Breast with Mixed Veggies", "Greek Salad with Feta", "Falafel"],
        "Dinner": ["Chicken Curry with Rice", "Fried Rice with Tofu", "Moussaka", "Enchiladas"],
        "Snack": ["Chickpeas", "Cherry Tomatoes", "Peanut Butter Toast", "Berries"]
    },
    "Family-Friendly Meal Plans": {
        "Breakfast": ["Overnight Oats", "Bananas", "Greek Yogurt", "Oatmeal with Berries", "Eggs"],
        "Lunch": ["Quinoa Salad with Chickpeas", "Chicken Breast with Mixed Veggies", "Greek Salad with Feta", "Tacos"],
        "Dinner": ["Chicken Curry with Rice", "Fried Rice with Tofu", "Lentil Soup with Mixed Greens"],
        "Snack": ["Chickpeas", "Cherry Tomatoes", "Peanut Butter Toast", "Berries"]
    },
    "Plant-Based Meal Plans": {
        "Breakfast": ["Overnight Oats with Almond Milk", "Bananas", "Greek Yogurt", "Oatmeal with Berries", "Eggs"],
        "Lunch": ["Quinoa Salad with Chickpeas", "Mixed Veggies with Tofu", "Greek Salad with Feta", "Falafel"],
        "Dinner": ["Lentil Soup with Mixed Greens", "Fried Rice with Tofu", "Moussaka", "Enchiladas"],
        "Snack": ["Chickpeas", "Cherry Tomatoes", "Peanut Butter Toast", "Berries"]
    },
    "Fitness-Focused Meal Plans": {
        "Breakfast": ["Overnight Oats with Almond Milk", "Bananas", "Greek Yogurt", "Oatmeal with Berries", "Eggs"],
        "Lunch": ["Quinoa Salad with Chickpeas", "Chicken Breast with Mixed Veggies", "Greek Salad with Feta", "Souvlaki"],
        "Dinner": ["Chicken Curry with Rice", "Fried Rice with Tofu", "Lentil Soup with Mixed Greens"],
        "Snack": ["Chickpeas", "Cherry Tomatoes", "Peanut Butter Toast", "Berries"]
    },
    "Quick and Easy Dinner Plans": {
        "Breakfast": ["Overnight Oats with Almond Milk", "Bananas", "Greek Yogurt", "Oatmeal with Berries", "Eggs"],
        "Lunch": ["Quinoa Salad with Chickpeas", "Chicken Breast with Mixed Veggies", "Greek Salad with Feta", "Tacos"],
        "Dinner": ["Chicken Curry with Rice", "Fried Rice with Tofu", "Lentil Soup with Mixed Greens"],
        "Snack": ["Chickpeas", "Cherry Tomatoes", "Peanut Butter Toast", "Berries"]
    },
    "Healthy Snacks and Small Meals": {
        "Breakfast": ["Overnight Oats with Almond Milk", "Bananas", "Greek Yogurt", "Oatmeal with Berries", "Eggs"],
        "Lunch": ["Quinoa Salad with Chickpeas", "Chicken Breast with Mixed Veggies", "Greek Salad with Feta", "Tacos"],
        "Dinner": ["Chicken Curry with Rice", "Fried Rice with Tofu", "Lentil Soup with Mixed Greens"],
        "Snack": ["Chickpeas", "Cherry Tomatoes", "Peanut Butter Toast", "Berries"]
    },
    "Cultural and International Meal Plans": {
        "Breakfast": ["Greek Yogurt", "Bananas", "Oatmeal with Berries", "Eggs", "Overnight Oats"],
        "Lunch": ["Tacos", "Quinoa Salad with Chickpeas", "Mixed Veggies with Tofu", "Biryani", "Souvlaki"],
        "Dinner": ["Chicken Curry with Rice", "Fried Rice with Tofu", "Lentil Soup with Mixed Greens", "Pho", "Dim Sum"],
        "Snack": ["Chickpeas", "Spring Rolls", "Peanut Butter Toast", "Bananas", "Falafel"]
    },
    "Meal Plans for Dietary Restrictions": {
        "Breakfast": ["Overnight Oats with Almond Milk", "Bananas", "Greek Yogurt", "Oatmeal with Berries", "Eggs"],
        "Lunch": ["Quinoa Salad with Chickpeas", "Chicken Breast with Mixed Veggies", "Greek Salad with Feta", "Tacos"],
        "Dinner": ["Chicken Curry with Rice", "Fried Rice with Tofu", "Lentil Soup with Mixed Greens"],
        "Snack": ["Chickpeas", "Cherry Tomatoes", "Peanut Butter Toast", "Berries"]
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

st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
    }
    h1 {
        color: #4CAF50;
    }
    .stSelectbox {
        border: 2px solid #4CAF50;
        border-radius: 5px;
        padding: 5px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .stDownloadButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .highlight {
        background-color: #ffeb3b;
        padding: 5px;
    }
    .meal-time {
        font-weight: bold;
        color: #4CAF50;
    }
    .meal-food {
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

st.title("Customizable Weekly Meal Plan Generator")
st.write("Select your meal plan criteria and generate a customized weekly meal plan with breakfast, lunch, dinner, and snacks.")

# User selection
selection = st.selectbox("Choose your meal plan criteria:", list(meal_plans.keys()), key="meal_plan_selectbox")

# Generate and display meal plan
if st.button("Generate Weekly Meal Plan"):
    weekly_meal_plan = generate_weekly_meal_plan(selection)
    st.write(f"Meal Plan: {selection}")
    
    days = list(weekly_meal_plan.keys())
    cols = st.columns(len(days))

    for col, day in zip(cols, days):
        col.header(day)
        for meal_time, foods in weekly_meal_plan[day].items():
            col.markdown(f"<div class='meal-time'>{meal_time}</div>", unsafe_allow_html=True)
            for food, nutrients in foods.items():
                col.markdown(f"<div class='meal-food'><strong>{food}</strong></div>", unsafe_allow_html=True)
                col.write(f"Calories: {nutrients['calories']} kcal")
                col.write(f"Protein: {nutrients['protein']} g")
                col.write(f"Fat: {nutrients['fat']} g")
                col.write(f"Carbs: {nutrients['carbs']} g")
                col.write("---")
