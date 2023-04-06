import streamlit as st
import pickle

# Load the trained model from the pickle file
with open("ECG.pkl", "rb") as f:
    model = pickle.load(f)

# Create the Streamlit app
st.title('ECG Classification')
st.write('Enter the following features to classify ECG results:')
age = st.sidebar.number_input('Enter your age: ')

sex = st.sidebar.selectbox('Sex', (0, 1))
cp = st.sidebar.selectbox('Chest pain type', (0, 1, 2, 3))
tres = st.sidebar.number_input('Resting blood pressure: ')
res = st.sidebar.number_input('Resting electrocardiographic results: ')
tha = st.sidebar.number_input('Maximum heart rate achieved: ')
exa = st.sidebar.selectbox('Exercise induced angina: ', (0, 1))
old = st.sidebar.number_input('oldpeak ')
slope = st.sidebar.number_input('he slope of the peak exercise ST segmen: ')
ca = st.sidebar.selectbox('number of major vessels', (0, 1, 2, 3))
thal = st.sidebar.selectbox('thal', (0, 1, 2))

# Create a button to make the prediction
if st.button('Predict'):
    # Make the prediction using the input values
    features = [[age,sex, cp, tres,res,tha,exa,old,slope,ca,thal]]
    result = model.predict(features)[0]

    # Display the prediction
    if result == 0:
        st.write('The ECG results indicate Patient Has no heart disease.')
    else:
        st.write('The ECG results indicate  Patient Has heart disease.')
