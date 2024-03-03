import streamlit as st
import image_insertion_lib as glib

st.set_page_config(layout="wide", page_title="Friend Gen")

st.title("Friend Gen")

col1, col2, col3 = st.columns(3)

placement_options_dict = { # Configure mask areas for image insertion
    "1": (78, 60, 359, 115),  #x, y, width, height
    "1": (108, 237, 295, 239),
    "2": (0, 0, 200, 100),
    "3": (0, 0, 0, 0),
    "4": (0, 0, 0, 0), 
    "5": (0, 0, 0, 0), 
    "6": (0, 0, 0, 0), 
    "7": (0, 0, 0, 0), 
    "8": (0, 0, 0, 0), 
    "9": (0, 0, 0, 0), 
}

placement_options = list(placement_options_dict)


with col1:
    st.subheader("Friendless image")
    
    uploaded_file = st.file_uploader("Select an image (must be 512x512)", type=['png', 'jpg'])
    
    if uploaded_file:
        uploaded_image_preview = glib.get_bytesio_from_bytes(uploaded_file.getvalue())
        st.image(uploaded_file)
    else:
        st.image("img/input/pug.jpeg")
    

with col2:
    st.subheader("Insertion parameters")
    
    placement_area = st.multiselect("Placement area:", 
        placement_options,
    )
    
    with st.expander("Custom:", expanded=False):
        
        mask_dimensions = placement_options_dict[placement_area]
    
        mask_x = st.number_input("Mask x position", value=mask_dimensions[0])
        mask_y = st.number_input("Mask y position", value=mask_dimensions[1])
        mask_width = st.number_input("Mask width", value=mask_dimensions[2])
        mask_height = st.number_input("Mask height", value=mask_dimensions[3])
    
    # prompt_text = st.text_area("Object to add:", height=100, help="The prompt text")
    
    generate_button = st.button("Generate")
    

with col3:
    st.subheader("Friends generated here.")

    if generate_button:
        with st.spinner("Drawing friends..."):
            if uploaded_file:
                image_bytes = uploaded_file.getvalue()
            else:
                image_bytes = None
            
            generated_image = glib.get_image_from_model(
                prompt_content=prompt_text, 
                image_bytes=image_bytes, 
                insertion_position=(mask_x, mask_y),
                insertion_dimensions=(mask_width, mask_height),
            )
        
        st.image(generated_image)


# Load CSS
with open('styles.css') as f:
        css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
# End load CSS