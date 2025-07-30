import streamlit as st
import pandas as pd
import joblib
import base64  # To encode the background image

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Dino-Identifier 🦖",
    page_icon=" paleontologist_technologist/dino_identifier_app/main/assets/favicon.ico", # You can use an emoji or a URL to an icon
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- BACKGROUND IMAGE FUNCTION ---
# This function sets a background image and adds a semi-transparent overlay
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0,0,20,0.7), rgba(0,0,20,0.7)), url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .st-emotion-cache-16txtl3 {{
        color: #FFFFFF;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# --- IMPORTANT: Create an 'assets' folder in your project's root and add a 'background.png' image to it. ---
# You can download a suitable image from Pexels.com or Unsplash.com (e.g., search for "jungle night" or "fossil").
try:
    set_png_as_page_bg('assets/background.jpg')
except FileNotFoundError:
    st.warning("Background image not found. Please create an 'assets/background.jpg' file.")


# --- MODEL LOADING ---
@st.cache_data
def load_model():
    try:
        model = joblib.load('models/dino_identifier_model.joblib')
        return model
    except FileNotFoundError:
        return None

model = load_model()

if model is None:
    st.error("🚨 Model file not found! Please run the training script first.")
    st.stop()

# --- SIDEBAR ---
with st.sidebar:
    st.image("assets/dino.png", width=150) # A sample logo, you can create your own
    st.header("🔬 Fossil Analysis Panel")
    st.markdown("Enter the known measurements of the dinosaur fossil.")

    length = st.slider("Length (meters)", 0.1, 50.0, 10.0, 0.1, help="Estimated length from head to tail.")
    max_ma = st.slider("Geological Age - Max (Mya)", 60.0, 250.0, 100.0, help="The oldest possible age of the fossil in millions of years ago.")
    min_ma = st.slider("Geological Age - Min (Mya)", 60.0, 250.0, 80.0, help="The youngest possible age of the fossil in millions of years ago.")

    st.markdown("---")
    predict_button = st.button("IDENTIFY DINOSAUR ➜", use_container_width=True)
    st.markdown("---")
    st.info("This app uses a RandomForest model to classify dinosaurs based on physical attributes.")


# --- MAIN PAGE ---
st.title("DINOSAUR IDENTIFICATION SYSTEM")
st.markdown("### A Machine Learning approach to paleontological classification.")
st.write("---")


if predict_button:
    input_data = pd.DataFrame({
        'length_m': [length],
        'max_ma': [max_ma],
        'min_ma': [min_ma]
    })

    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0]

    st.header("ANALYSIS RESULTS", divider='rainbow')

    col1, col2 = st.columns(2)

    with col1:
        if prediction == 1:  # Carnivore
            st.subheader("DIET TYPE: CARNIVORE")
            st.image(
                "https://www.nhm.ac.uk/discover/dino-directory/_next/image?url=https%3A%2F%2Fwww.nhm.ac.uk%2Fresources%2Fnature-online%2Flife%2Fdinosaurs%2Fdinosaur-directory%2Fimages%2Freconstruction%2Fsmall%2Fmegalosaurus.jpg&w=2048&q=75",
                caption="This specimen likely belongs to a predatory species."
            )
            prob = prediction_proba[1]
            diet_type = "Carnivore"
        else:  # Herbivore
            st.subheader("DIET TYPE: HERBIVORE")
            st.image(
                "https://www.nhm.ac.uk/discover/dino-directory/_next/image?url=https%3A%2F%2Fwww.nhm.ac.uk%2Fresources%2Fnature-online%2Flife%2Fdinosaurs%2Fdinosaur-directory%2Fimages%2Freconstruction%2Fsmall%2Fapatosaurus-art.jpg&w=2048&q=75",
                caption="This specimen likely belongs to a plant-eating species."
            )
            prob = prediction_proba[0]
            diet_type = "Herbivore"

    with col2:
        st.metric(label="Predicted Diet", value=diet_type)
        st.metric(label="Confidence Level", value=f"{prob*100:.2f}%")

        st.subheader("Input Measurement Summary")
        st.json({
            "Length": f"{length} meters",
            "Lived Between": f"{max_ma} and {min_ma} Mya"
        })

        st.success("Analysis complete. The model has classified the fossil based on the provided data.")

else:
    st.info("Please enter the fossil measurements in the sidebar and click 'IDENTIFY DINOSAUR' to begin the analysis.")
    st.image(
        "https://www.nhm.ac.uk/discover/dino-directory/_next/image?url=https%3A%2F%2Fwww.nhm.ac.uk%2Fresources%2Fnature-online%2Flife%2Fdinosaurs%2Fdinosaur-directory%2Fimages%2Freconstruction%2Fsmall%2FBactrosaurus.jpg&w=2048&q=75",
        caption="Awaiting data from the analysis panel..."
    )
