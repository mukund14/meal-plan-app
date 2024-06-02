import random
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

# Define high-protein recipes
recipes = {
    "Breakfast": [
        {"name": "Greek Yogurt Parfait", "protein": 25},
        {"name": "Scrambled Tofu", "protein": 20},
        {"name": "Protein Smoothie", "protein": 24},
        {"name": "Oatmeal with Protein Powder", "protein": 20},
        {"name": "Chia Seed Pudding", "protein": 15}
    ],
    "Lunch": [
        {"name": "Quinoa and Black Bean Salad", "protein": 16},
        {"name": "Lentil Soup", "protein": 18},
        {"name": "Chickpea Salad", "protein": 15},
        {"name": "Tofu Stir-Fry", "protein": 22},
        {"name": "Veggie Burger", "protein": 20}
    ],
    "Dinner": [
        {"name": "Lentil and Vegetable Stir-Fry", "protein": 22},
        {"name": "Vegetarian Chili", "protein": 20},
        {"name": "Stuffed Bell Peppers with Quinoa and Beans", "protein": 18},
        {"name": "Vegetable Curry with Tofu", "protein": 20},
        {"name": "Spaghetti with Lentil Bolognese", "protein": 22}
    ],
    "Snacks": [
        {"name": "Hummus with Veggies", "protein": 10},
        {"name": "Cottage Cheese with Pineapple", "protein": 25},
        {"name": "Protein Bars", "protein": 20},
        {"name": "Roasted Chickpeas", "protein": 15},
        {"name": "Edamame", "protein": 17}
    ]
}

# Generate the monthly meal plan
def generate_monthly_meal_plan():
    today = datetime.today()
    days = [(today + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(30)]
    meal_plan = {day: {"Breakfast": None, "Lunch": None, "Dinner": None, "Snack 1": None, "Snack 2": None} for day in days}
    
    for day in days:
        meal_plan[day]["Breakfast"] = random.choice(recipes["Breakfast"])
        meal_plan[day]["Lunch"] = random.choice(recipes["Lunch"])
        meal_plan[day]["Dinner"] = random.choice(recipes["Dinner"])
        meal_plan[day]["Snack 1"] = random.choice(recipes["Snacks"])
        meal_plan[day]["Snack 2"] = random.choice(recipes["Snacks"])
    
    return meal_plan

# Create the meal plan
monthly_meal_plan = generate_monthly_meal_plan()

# Convert the meal plan to a DataFrame for better visualization
meal_plan_df = pd.DataFrame(monthly_meal_plan).transpose()

# Streamlit app
st.set_page_config(page_title="Monthly High-Protein Vegetarian Meal Plan", layout="wide")

st.title("Monthly High-Protein Vegetarian Meal Plan")
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .stDownloadButton>button {
        background-color: #4CAF50;
        color: white;
    }
    h1 {
        color: #4CAF50;
    }
    .highlight {
        background-color: #ffeb3b;
        padding: 5px;
    }
</style>
""", unsafe_allow_html=True)

st.write("Here is your high-protein vegetarian meal plan for the month:")

today_str = datetime.today().strftime('%Y-%m-%d')

# Display the meal plan with expandable sections for each day
for day in meal_plan_df.index:
    highlight = "highlight" if day == today_str else ""
    with st.expander(f"{day} {'(Today)' if day == today_str else ''}"):
        st.markdown(f"<div class='{highlight}'><strong>Breakfast:</strong> {meal_plan_df.loc[day, 'Breakfast']['name']} ({meal_plan_df.loc[day, 'Breakfast']['protein']}g protein)</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='{highlight}'><strong>Lunch:</strong> {meal_plan_df.loc[day, 'Lunch']['name']} ({meal_plan_df.loc[day, 'Lunch']['protein']}g protein)</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='{highlight}'><strong>Dinner:</strong> {meal_plan_df.loc[day, 'Dinner']['name']} ({meal_plan_df.loc[day, 'Dinner']['protein']}g protein)</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='{highlight}'><strong>Snack 1:</strong> {meal_plan_df.loc[day, 'Snack 1']['name']} ({meal_plan_df.loc[day, 'Snack 1']['protein']}g protein)</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='{highlight}'><strong>Snack 2:</strong> {meal_plan_df.loc[day, 'Snack 2']['name']} ({meal_plan_df.loc[day, 'Snack 2']['protein']}g protein)</div>", unsafe_allow_html=True)

# Download meal plan as CSV
csv = meal_plan_df.to_csv(index=True).encode('utf-8')
st.download_button(
    label="Download Meal Plan as CSV",
    data=csv,
    file_name='monthly_meal_plan.csv',
    mime='text/csv',
)
