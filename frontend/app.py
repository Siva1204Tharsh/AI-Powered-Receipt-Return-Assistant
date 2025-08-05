import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="Visual Receipt Scanner", layout="centered")
st.title("🧾 Visual Receipt Scanner for Returns")

uploaded_file = st.file_uploader("Upload your receipt", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Receipt", use_column_width=True)
    
    with st.spinner("Analyzing receipt..."):
        response = requests.post(
            "http://localhost:8000/upload/",
            files={"file": uploaded_file.getvalue()}
        )
    st.write("Raw Response:", response.text)
    result = response.json()
    if result["status"] == "Return Approved":
        st.success(f"✅ Status: {result['status']}")
        st.json(result["match"])
        # return_image = Image.open(result["image"])
        # st.image(return_image, caption="Analyzed Receipt", use_column_width=True)

    else:
        st.error(f"❌ Status: {result['status']}")
        st.json(result)

else:
    st.write("Upload a receipt to analyze it!")
    # st.success(f"✅ Status: {result['status']}")
    # st.json(result)


    # st.image(result["image"], caption="Analyzed Receipt", use_column_width=True)