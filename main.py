import streamlit as st
from util import *

# Page title of the application
page_title = "RecipeWiz"
page_icon = "✨"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="centered")

# Application Title and description
st.title(f'{page_title}{page_icon}')
st.write('***:blue[From craving to cooking—instantly!]***')
st.write("""
*Select a cuisine, choose your dish, and let RecipeWiz conjure up the perfect recipe! �🍕 Whether it's spicy Mexican 
or creamy Italian, dinner inspiration is just a click away.*
""")
# Display footer in the sidebar
display_footer()

cuisine_dish_dict = {'Italian': ['Seafood Pasta', 'Sicilian Eggplant Rigatoni', 'Tagliatelle Bolognese', 'Trofie Al Pesto', 'Tomato Risotoo', 'Sicilian Cannoli', 'Tiramisu', ],
                     'Mexican': ['Chicken Enchiladas', 'Baja Fish Tacos', 'Chicken Burrito', 'Pulled Pork Quesadillas', 'Almost Pozole', 'Queso Fundido', 'Fully Loaded Nachos', 'Chilli sin Carne', 'Cauliflower Steaks with Romesco'],
                     'Thai': ['Pad Thai Goong Sod', 'Tom Kha Gai', 'Som Tum', 'Yum Woon Sen Neua', 'Gaeng Kiew Wan Goong', 'Massaman Gai'],
                     ' Indian': ['Lamb Vindaloo', 'Beef Koftas', 'Fried Chicken Curry', 'Egg and Potato Curry', 'Vall Dhal', 'Whole Moong, Dry', 'Toovar Dhal', 'Black Chana Dhal', 'Cut Okra Curry', 'Madras Potato and Pea Curry', 'Bombay Potato Curry', 'Fresh Mixed Vegetable Curry', 'Aubergine and Pea Curry', 'Guaer Curry', 'Kadu and Tomato Curry'],}

# st.write(cuisine_dish_dict.keys())
# st.write(cuisine_dish_dict['Thai'])

st.subheader('Select Cuisine & Dish', divider='gray')
cuisine = st.selectbox('Select the Cuisine', cuisine_dish_dict.keys(),
                         placeholder='Select the Cuisine', help='Select the Cuisine from the list', label_visibility="visible")

dish = st.selectbox('Select the Dish', cuisine_dish_dict[cuisine],
                         placeholder='Select the Dish', help='Select the Dish from the list', label_visibility="visible")

prompt = f"Generate the recipe to make following {cuisine} dish: {dish}"
button = st.button("Generate Recipe", type='primary', disabled=not cuisine, icon=':material/celebration:')

if button:
    with st.spinner('Processing ...', show_time=True):
        st.subheader('Recipe:', divider='gray')
        response = langflow_recipe_generator(prompt)
        st.write(response)







