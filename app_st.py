import streamlit as st
import numpy as np
import pickle


pickle_in = open("model_final.pkl","rb")
classifier = pickle.load(pickle_in)

# Function to validate integer input
def is_valid_integer_input(value):
    try:
        int_value = int(value)
        if int_value in (0, 1):
            return True
        else:
            return False
    except ValueError:
        return False

# Sidebar navigation
page = st.sidebar.selectbox("Select Page", ["Home", "Disease Score", "Physician Score", "Procedure Score", "Diagnosis Score", "Predict"])

# Main content
if page == "Home":
    st.title("Welcome to Surya's Claims Prediction Assignment")
    st.write("This is a web application to calculate different scores and make predictions.")
    st.image('Image.jpg', caption='Welcome Abhishek Sir!!')

elif page == "Disease Score":
    st.title("Calculate Disease Score")

    # Input fields
    field_names = ['Alzheimer',
       'Heart failure', 'Kidney Disease',
       'Cancer', 'ObstrPulmonary',
       'Depression', 'Diabetes',
       'Ischemic Heart', 'Osteoporasis',
       'Rheumatoidarthritis', 'Stroke']
    fields = {}
    for field in field_names:
        fields[field] = st.text_input(f"{field} (Yes:1 No:0)")

    for field, value in fields.items():
        if value != '':
            fields[field] = int(value)
        else:
            fields[field] = 0

    if st.button("Calculate Disease Score"):
        score = 0
        count = 10
        for field, value in fields.items():
            if value == 1:
                score += count
            count = count-1
        st.success(f"Your Disease Score is: {score}")


elif page == "Physician Score":
    st.title("Calculate Physician Score")

    # Input fields
    field_names = ['Attending Physician', 'Operating Physician', 'Other Physician']
    fields = {}
    for field in field_names:
        fields[field] = st.text_input(f"{field} (Yes:1 No:0)")

    for field, value in fields.items():
        if value != '':
            fields[field] = int(value)
        else:
            fields[field] = 0

    if st.button("Calculate Physician Score"):
        score = 0
        count = 15
        for field, value in fields.items():
            if value == 1:
                score += count
            count = count-5
        st.success(f"Your Physician Score is: {score}")



elif page == "Procedure Score":
    st.title("Calculate Procedure Score")

    # Input fields
    field_names = ['Procedure Code_1 ', 'Procedure Code_2',
       'Procedure Code_3', 'Procedure Code_4', 'Procedure Code_5',
       'Procedure Code_6']
    fields = {}
    for field in field_names:
        fields[field] = st.text_input(f"{field} (Yes:1 No:0)")

    for field, value in fields.items():
        if value != '':
            fields[field] = int(value)
        else:
            fields[field] = 0

    if st.button("Calculate Procedure Score"):
        score = 0
        count = 6
        for field, value in fields.items():
            if value == 1:
                score += count
            count = count-1
        st.success(f"Your Procedure Score: {score}")

elif page == "Diagnosis Score":
    st.title("Calculate Diagnosis Score")

    # Input fields
    field_names = ['ClmDiagnosisCode_1', 'ClmDiagnosisCode_2', 'ClmDiagnosisCode_3',
       'ClmDiagnosisCode_4', 'ClmDiagnosisCode_5', 'ClmDiagnosisCode_6',
       'ClmDiagnosisCode_7', 'ClmDiagnosisCode_8', 'ClmDiagnosisCode_9',
       'ClmDiagnosisCode_10']
    fields = {}
    for field in field_names:
        fields[field] = st.text_input(f"{field} (0 or 1)")

    for field, value in fields.items():
        if value != '':
            fields[field] = int(value)
        else:
            fields[field] = 0

    if st.button("Calculate Diagnosis Score"):
        score = 0
        count = 10
        for field, value in fields.items():
            if value == 1:
                score += count
            count = count-1
        st.success(f"Your Diagnosis Score: {score}")
    

elif page == "Predict":
    st.title("Predict Insurance Amount")

    # Input fields
    field_names = ['Beneficiary ID', 'Provider ID', 'Claim Amount Reimbursed', 'Claim Admit Diagnosis Code',
       'Diagnosis Group Code', 'Days admitted', 'Diagnosis Score',
       'ProcedureScore', 'Physician Score', 'NaN count','Total Score', 'Gender(Male:1 Female:0)',
       'Renal Disease Indicator (Yes:1 No:0)', 'IP Annual Reimbursement Amount',
       'IP Annual Deductible Amount', 'OP Annual Reimbursement Amount',
       'OP Annual Deductible Amount', 'Disease Score']
    fields = {}
    for field in field_names:
        fields[field] = st.text_input(f"{field}")

    for field, value in fields.items():
        if value != '':
            fields[field] = int(value)
        else:
            fields[field] = 0


    if st.button('Predict'):
        # Prepare input data
        input_data = []
        for field in field_names:
            if fields[field] != '':
                input_data.append(int(fields[field]))
            else:
                input_data.append(0)
        
        # Convert input data to numpy array for prediction
        input_data = [input_data]  # Convert to list of lists
        input_data = np.array(input_data)  # Convert to numpy array

        # Predict claim amount
        predicted_amount = classifier.predict(input_data)
        
        
        # Display the predicted claim amount
        st.write('Predicted Claim Amount:', predicted_amount)


