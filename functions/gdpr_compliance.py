import streamlit as st
from streamlit_modal import Modal

def run_compliance_modal():
    # Initialize session state
    if 'compliance_button' not in st.session_state:
        st.session_state.compliance_button = False
    if 'compliance_statut' not in st.session_state:
        st.session_state.compliance_statut = False
    else:
        st.session_state.compliance_statut = st.session_state.compliance_statut
    if 'compliance_message' not in st.session_state:
        st.session_state.compliance_message = False

    modal = Modal(
        "Compliance form",
        key="modal1",
        padding=20,
        max_width=744
    )

    # When one of the consent buttons has been clicked, we display the message
    if not st.session_state.compliance_message and st.session_state.compliance_button:
        st.session_state.compliance_message = True
        with modal.container():
            if st.session_state.compliance_statut:
                st.success("""
                            **Thank you for your consent.**

                            **Your data will only be used for improving your experience with Nutritional AI.**

                            **It is recommended not to divulge any personal information.**
                            """)
            else:
                st.warning("**Your data won't be used for improving Nutritional AI.**")

    if not st.session_state.compliance_button:
        with modal.container():
            st.write("I consent to my conversation being conserved and used to improve the chatbot model")

            consent_button = st.button("**I agree**")
            no_consent_button = st.button("**I do not agree**") 

            if consent_button:
                st.session_state.compliance_button = True
                st.session_state.compliance_statut = True
                st.rerun()

            elif no_consent_button:
                st.session_state.compliance_button = True
                st.rerun()

    # We return the compliance status                
    return st.session_state.compliance_statut