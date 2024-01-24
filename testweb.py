import streamlit as st

def main():
    st.title("Streamlit Web Application")

    # Add a text box for user input
    user_input = st.text_input("Enter text:")

    # Add a button to trigger an action
    if st.button("Submit"):
        st.success(f"You entered: {user_input}")

if __name__ == "__main__":
    main()
