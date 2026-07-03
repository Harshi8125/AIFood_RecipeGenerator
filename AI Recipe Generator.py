import streamlit as st
import ollama

st.set_page_config(page_title="AI Recipe Generator", page_icon="🍽️")

st.title("🍽️ AI Recipe Generator & Meal Planner")
st.write("Generate delicious recipes using AI!")

ingredients = st.text_area(
    "🥕 Ingredients (Separate with commas)"
)

cuisine = st.selectbox(
    "🍛 Select Cuisine",
    ["Indian", "Chinese", "Italian", "Mexican", "American"]
)

budget = st.number_input(
    "💰 Budget (₹)",
    min_value=100,
    value=500,
    step=100
)

time = st.number_input(
    "⏰ Cooking Time (Minutes)",
    min_value=10,
    value=30,
    step=5
)

diet = st.selectbox(
    "🥗 Diet Preference",
    ["Vegetarian", "Non-Vegetarian", "Vegan"]
)

if st.button("🍳 Generate Recipe"):

    prompt = f"""
    Generate a recipe using these details.

    Ingredients: {ingredients}

    Cuisine: {cuisine}

    Budget: ₹{budget}

    Cooking Time: {time} minutes

    Diet Preference: {diet}

    Give the answer in this format:

    Recipe Name

    Ingredients Required

    Step-by-Step Cooking Instructions

    Cooking Time

    Estimated Cost

    Calories

    Tips
    """

    with st.spinner("Generating recipe... 🍳"):

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

    st.subheader("🍽️ Generated Recipe")

    st.write(response["message"]["content"])