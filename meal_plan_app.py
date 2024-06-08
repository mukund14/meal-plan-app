import random
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import requests

# Function to fetch nutrient data (dummy data used here for simplicity)
def get_food_nutrients(food):
    nutrients = {
        "Chicken Breast": {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0, "quantity": "100g", "servings": 1},
        "Quinoa": {"calories": 120, "protein": 4, "fat": 2, "carbs": 21, "quantity": "1 cup", "servings": 1},
        "Chickpeas": {"calories": 180, "protein": 10, "fat": 3, "carbs": 30, "quantity": "1 cup", "servings": 1},
        "Mixed Veggies": {"calories": 50, "protein": 2, "fat": 0.5, "carbs": 10, "quantity": "1 cup", "servings": 1},
        "Mixed Greens": {"calories": 5, "protein": 0.5, "fat": 0.1, "carbs": 1, "quantity": "1 cup", "servings": 1},
        "Cherry Tomatoes": {"calories": 15, "protein": 1, "fat": 0.2, "carbs": 3, "quantity": "10 pieces", "servings": 1},
        "Feta Cheese": {"calories": 100, "protein": 5, "fat": 8, "carbs": 1, "quantity": "1/4 cup", "servings": 1},
        "Overnight Oats": {"calories": 300, "protein": 10, "fat": 8, "carbs": 50, "quantity": "1 cup", "servings": 1},
        "Rice": {"calories": 130, "protein": 2.7, "fat": 0.3, "carbs": 28, "quantity": "1 cup", "servings": 1},
        "Lentils": {"calories": 116, "protein": 9, "fat": 0.4, "carbs": 20, "quantity": "1 cup", "servings": 1},
        "Tofu": {"calories": 70, "protein": 8, "fat": 4, "carbs": 2, "quantity": "100g", "servings": 1},
        "Peanut Butter": {"calories": 190, "protein": 8, "fat": 16, "carbs": 6, "quantity": "2 tbsp", "servings": 1},
        "Bananas": {"calories": 105, "protein": 1.3, "fat": 0.3, "carbs": 27, "quantity": "1 piece", "servings": 1},
        "Oatmeal": {"calories": 150, "protein": 5, "fat": 2.5, "carbs": 27, "quantity": "1 cup", "servings": 1},
        "Eggs": {"calories": 70, "protein": 6, "fat": 5, "carbs": 1, "quantity": "1 piece", "servings": 1},
        "Greek Yogurt": {"calories": 100, "protein": 10, "fat": 0, "carbs": 6, "quantity": "1 cup", "servings": 1},
        "Tacos": {"calories": 200, "protein": 10, "fat": 12, "carbs": 15, "quantity": "2 pieces", "servings": 1},
        "Chicken Curry": {"calories": 250, "protein": 20, "fat": 10, "carbs": 15, "quantity": "1 cup", "servings": 1},
        "Fried Rice": {"calories": 250, "protein": 6, "fat": 10, "carbs": 35, "quantity": "1 cup", "servings": 1},
        "Berries": {"calories": 85, "protein": 1, "fat": 0.5, "carbs": 21, "quantity": "1 cup", "servings": 1},
        "Watermelon": {"calories": 46, "protein": 0.9, "fat": 0.2, "carbs": 12, "quantity": "1 cup", "servings": 1},
        "Oranges": {"calories": 62, "protein": 1.2, "fat": 0.2, "carbs": 15, "quantity": "1 piece", "servings": 1},
        "Apples": {"calories": 95, "protein": 0.5, "fat": 0.3, "carbs": 25, "quantity": "1 piece", "servings": 1},
        "Peaches": {"calories": 59, "protein": 1.4, "fat": 0.4, "carbs": 14, "quantity": "1 piece", "servings": 1},
        "Grapes": {"calories": 62, "protein": 0.6, "fat": 0.3, "carbs": 16, "quantity": "1 cup", "servings": 1},
        "Milk": {"calories": 103, "protein": 8, "fat": 2.4, "carbs": 12, "quantity": "1 cup", "servings": 1},
        "Almond Milk": {"calories": 39, "protein": 1, "fat": 3, "carbs": 2, "quantity": "1 cup", "servings": 1},
        "Cashew Milk": {"calories": 25, "protein": 1, "fat": 2, "carbs": 1, "quantity": "1 cup", "servings": 1},
        "Oat Milk": {"calories": 120, "protein": 3, "fat": 5, "carbs": 16, "quantity": "1 cup", "servings": 1},
    }
    return nutrients.get(food, {"calories": 0, "protein": 0, "fat": 0, "carbs": 0, "quantity": "Unknown", "servings": "Unknown"})

# Combine nutrients of multiple foods
def combine_nutrients(foods):
    combined = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0, "quantity": [], "servings": []}
    for food in foods:
        nutrients = get_food_nutrients(food)
        combined["calories"] += nutrients["calories"]
        combined["protein"] += nutrients["protein"]
        combined["fat"] += nutrients["fat"]
        combined["carbs"] += nutrients["carbs"]
        combined["quantity"].append(nutrients["quantity"])
        combined["servings"].append(nutrients["servings"])
    combined["quantity"] = ", ".join(combined["quantity"])
    combined["servings"] = ", ".join(map(str, combined["servings"]))
    return combined

# Meal plan options
meal_plans = {
    "Weekly Meal Prep for Busy Professionals": {
        "Breakfast": [["Overnight Oats", "Berries"], ["Bananas", "Greek Yogurt"], ["Oatmeal", "Apples"], ["Eggs", "Oranges"]],
        "Lunch": [["Quinoa", "Chickpeas"], ["Chicken Breast", "Mixed Veggies"], ["Greek Salad", "Feta Cheese"], ["Tacos"]],
        "Dinner": [["Chicken Curry", "Rice"], ["Fried Rice", "Tofu"], ["Lentil Soup", "Mixed Greens"]],
        "Snack": [["Chickpeas"], ["Cherry Tomatoes"], ["Peanut Butter", "Bananas"], ["Berries"]]
    },
    "Budget-Friendly Meal Plans": {
        "Breakfast": [["Oatmeal", "Berries"], ["Bananas"], ["Eggs"], ["Overnight Oats", "Apples"], ["Greek Yogurt"]],
        "Lunch": [["Rice", "Lentils"], ["Lentil Soup"], ["Frozen Veggies", "Tofu"], ["Chickpeas", "Mixed Veggies"]],
        "Dinner": [["Rice", "Beans"], ["Lentil Soup"], ["Frozen Veggies Stir-fry", "Tofu"], ["Chickpeas", "Mixed Veggies"]],
        "Snack": [["Peanut Butter", "Bananas"], ["Cherry Tomatoes"], ["Mixed Greens"], ["Berries"]]
    },
    "Seasonal Meal Planning": {
        "Breakfast": [["Overnight Oats", "Berries"], ["Bananas", "Greek Yogurt"], ["Oatmeal", "Apples"], ["Eggs", "Oranges"]],
        "Lunch": [["Quinoa", "Chickpeas"], ["Chicken Breast", "Mixed Veggies"], ["Greek Salad", "Feta Cheese"], ["Falafel"]],
        "Dinner": [["Chicken Curry", "Rice"], ["Fried Rice", "Tofu"], ["Moussaka"], ["Enchiladas"]],
        "Snack": [["Chickpeas"], ["Cherry Tomatoes"], ["Peanut Butter", "Bananas"], ["Berries"]]
    },
    "Family-Friendly Meal Plans": {
        "Breakfast": [["Overnight Oats", "Berries"], ["Bananas", "Greek Yogurt"], ["Oatmeal", "Apples"], ["Eggs", "Oranges"]],
        "Lunch": [["Quinoa", "Chickpeas"], ["Chicken Breast", "Mixed Veggies"], ["Greek Salad", "Feta Cheese"], ["Tacos"]],
        "Dinner": [["Chicken Curry", "Rice"], ["Fried Rice", "Tofu"], ["Lentil Soup", "Mixed Greens"]],
        "Snack": [["Chickpeas"], ["Cherry Tomatoes"], ["Peanut Butter", "Bananas"], ["Berries"]]
    },
    "Plant-Based Meal Plans": {
        "Breakfast": [["Overnight Oats", "Almond Milk"], ["Bananas", "Greek Yogurt"], ["Oatmeal", "Berries"], ["Eggs"]],
        "Lunch": [["Quinoa", "Chickpeas"], ["Mixed Veggies", "Tofu"], ["Greek Salad", "Feta Cheese"], ["Falafel"]],
        "Dinner": [["Lentil Soup", "Mixed Greens"], ["Fried Rice", "Tofu"], ["Moussaka"], ["Enchiladas"]],
        "Snack": [["Chickpeas"], ["Cherry Tomatoes"], ["Peanut Butter", "Bananas"], ["Berries"]]
    },
    "Fitness-Focused Meal Plans": {
        "Breakfast": [["Overnight Oats", "Almond Milk"], ["Bananas", "Greek Yogurt"], ["Oatmeal", "Berries"], ["Eggs"]],
        "Lunch": [["Quinoa", "Chickpeas"], ["Chicken Breast", "Mixed Veggies"], ["Greek Salad", "Feta Cheese"], ["Souvlaki"]],
        "Dinner": [["Chicken Curry", "Rice"], ["Fried Rice", "Tofu"], ["Lentil Soup", "Mixed Greens"]],
        "Snack": [["Chickpeas"], ["Cherry Tomatoes"], ["Peanut Butter", "Bananas"], ["Berries"]]
    },
    "Quick and Easy Dinner Plans": {
        "Breakfast": [["Overnight Oats", "Almond Milk"], ["Bananas", "Greek Yogurt"], ["Oatmeal", "Berries"], ["Eggs"]],
        "Lunch": [["Quinoa", "Chickpeas"], ["Chicken Breast", "Mixed Veggies"], ["Greek Salad", "Feta Cheese"], ["Tacos"]],
        "Dinner": [["Chicken Curry", "Rice"], ["Fried Rice", "Tofu"], ["Lentil Soup", "Mixed Greens"]],
        "Snack": [["Chickpeas"], ["Cherry Tomatoes"], ["Peanut Butter", "Bananas"], ["Berries"]]
    },
    "Healthy Snacks and Small Meals": {
        "Breakfast": [["Overnight Oats", "Almond Milk"], ["Bananas", "Greek Yogurt"], ["Oatmeal", "Berries"], ["Eggs"]],
        "Lunch": [["Quinoa", "Chickpeas"], ["Chicken Breast", "Mixed Veggies"], ["Greek Salad", "Feta Cheese"], ["Tacos"]],
        "Dinner": [["Chicken Curry", "Rice"], ["Fried Rice", "Tofu"], ["Lentil Soup", "Mixed Greens"]],
        "Snack": [["Chickpeas"], ["Cherry Tomatoes"], ["Peanut Butter", "Bananas"], ["Berries"]]
    },
    "Cultural and International Meal Plans": {
        "Breakfast": [["Greek Yogurt", "Berries"], ["Bananas"], ["Oatmeal", "Apples"], ["Eggs"]],
        "Lunch": [["Tacos"], ["Quinoa", "Chickpeas"], ["Mixed Veggies", "Tofu"], ["Biryani"], ["Souvlaki"]],
        "Dinner": [["Chicken Curry", "Rice"], ["Fried Rice", "Tofu"], ["Lentil Soup", "Mixed Greens"], ["Pho"], ["Dim Sum"]],
        "Snack": [["Chickpeas"], ["Spring Rolls"], ["Peanut Butter", "Bananas"], ["Berries"]]
    },
    "Meal Plans for Dietary Restrictions": {
        "Breakfast": [["Overnight Oats", "Almond Milk"], ["Bananas", "Greek Yogurt"], ["Oatmeal", "Berries"], ["Eggs"]],
        "Lunch": [["Quinoa", "Chickpeas"], ["Chicken Breast", "Mixed Veggies"], ["Greek Salad", "Feta Cheese"], ["Tacos"]],
        "Dinner": [["Chicken Curry", "Rice"], ["Fried Rice", "Tofu"], ["Lentil Soup", "Mixed Greens"]],
        "Snack": [["Chickpeas"], ["Cherry Tomatoes"], ["Peanut Butter", "Bananas"], ["Berries"]]
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
                food_combination = random.choice(foods)
                nutrients = combine_nutrients(food_combination)
                weekly_plan[day][meal_time] = {"foods": food_combination, "nutrients": nutrients}
    
    return weekly_plan

# Create Plotly bar chart for meal nutrients
def create_nutrient_chart(meal_info):
    nutrients = meal_info["nutrients"]
    data = {
        "Nutrient": ["Calories", "Protein", "Fat", "Carbs"],
        "Amount": [nutrients["calories"], nutrients["protein"], nutrients["fat"], nutrients["carbs"]]
    }
    fig = px.bar(data, x="Nutrient", y="Amount", title="Meal Nutrient Composition")
    return fig

# Create Plotly pie chart for total daily nutrients
def create_daily_nutrient_chart(total_nutrients):
    labels = ["Protein", "Fat", "Carbs"]
    values = [total_nutrients["protein"], total_nutrients["fat"], total_nutrients["carbs"]]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3)])
    fig.update_layout(title_text="Total Daily Nutrient Intake")
    return fig

# Function to fetch recipe and image
def get_recipe_and_image(food):
    api_key = 'YOUR_SPOONACULAR_API_KEY'
    url = f"https://api.spoonacular.com/recipes/complexSearch?query={food}&number=1&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["results"]:
        recipe = data["results"][0]
        recipe_title = recipe["title"]
        image_url = recipe["image"]
        recipe_url = f"https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-').lower()}-{recipe['id']}"
        return recipe_title, image_url, recipe_url
    else:
        return None, None, None

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
        daily_total_nutrients = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0}
        for meal_time, meal_info in weekly_meal_plan[day].items():
            col.markdown(f"<div class='meal-time'>{meal_time}</div>", unsafe_allow_html=True)
            foods = meal_info["foods"]
            nutrients = meal_info["nutrients"]
            daily_total_nutrients["calories"] += nutrients["calories"]
            daily_total_nutrients["protein"] += nutrients["protein"]
            daily_total_nutrients["fat"] += nutrients["fat"]
            daily_total_nutrients["carbs"] += nutrients["carbs"]
            col.markdown(f"<div class='meal-food'><strong>{', '.join(foods)}</strong></div>", unsafe_allow_html=True)
            col.write(f"Quantity: {nutrients['quantity']}")
            col.write(f"Servings: {nutrients['servings']}")
            col.plotly_chart(create_nutrient_chart(meal_info))

            for food in foods:
                recipe_title, image_url, recipe_url = get_recipe_and_image(food)
                if recipe_title:
                    col.image(image_url, caption=recipe_title, use_column_width=True)
                    col.write(f"[View Recipe]({recipe_url})")

        col.plotly_chart(create_daily_nutrient_chart(daily_total_nutrients))
        col.write(f"Total Calories: {daily_total_nutrients['calories']} kcal")
        col.write(f"Total Protein: {daily_total_nutrients['protein']} g")
        col.write(f"Total Fat: {daily_total_nutrients['fat']} g")
        col.write(f"Total Carbs: {daily_total_nutrients['carbs']} g")
        col.write("---")
