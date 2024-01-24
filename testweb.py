import streamlit as st
import cv2
from matplotlib import pyplot as plt
import numpy as np

def main():
    st.title("Image Channel Separator")

    # Upload an image through Streamlit
    uploaded_file = st.file_uploader("Choose a color image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the uploaded image
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)

        # Display the original image
        st.image(image, caption="Original Image", use_column_width=True)

        # Split the image into Red, Green, and Blue channels
        red_channel = image[:, :, 2]
        green_channel = image[:, :, 1]
        blue_channel = image[:, :, 0]

        # Display the channels using Matplotlib
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))
        ax1.imshow(red_channel, cmap='Reds')
        ax1.set_title('Red Channel')
        ax2.imshow(green_channel, cmap='Greens')
        ax2.set_title('Green Channel')
        ax3.imshow(blue_channel, cmap='Blues')
        ax3.set_title('Blue Channel')

        st.pyplot(fig)

if __name__ == "__main__":
    main()

