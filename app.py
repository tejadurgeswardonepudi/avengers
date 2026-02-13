import streamlit as st
from groq_helper import get_ai_response
from prompts import marketing_prompt, sales_pitch_prompt, lead_scoring_prompt

st.set_page_config(page_title="MarketAI Suite", layout="wide")

st.title("📊 MarketAI Suite – AI Sales & Marketing Platform")

st.write("Use AI to generate marketing campaigns, sales pitches, and score leads.")

menu = st.sidebar.radio(
    "Select Feature",
    ["Marketing Campaign", "Sales Pitch", "Lead Scoring"]
)

if menu == "Marketing Campaign":
    st.header("📣 Marketing Campaign Generator")

    product = st.text_input("Product Name", "SaaS CRM")
    audience = st.text_input("Target Audience", "Small Business Owners")
    platform = st.selectbox("Platform", ["LinkedIn", "Instagram", "Email"])

    if st.button("Generate Campaign"):
        with st.spinner("Generating campaign..."):
            prompt = marketing_prompt(product, audience, platform)
            result = get_ai_response(prompt)

        st.success("Campaign Generated Successfully")
        st.text_area("Campaign Output", result, height=350)

elif menu == "Sales Pitch":
    st.header("💼 Sales Pitch Generator")

    product = st.text_input("Product / Service", "Enterprise CRM")
    customer = st.text_input("Target Customer", "Fortune 500 IT Director")

    if st.button("Generate Pitch"):
        with st.spinner("Generating sales pitch..."):
            prompt = sales_pitch_prompt(product, customer)
            result = get_ai_response(prompt)

        st.success("Sales Pitch Ready")
        st.text_area("Pitch Output", result, height=300)

else:
    st.header("📈 Lead Scoring System")

    budget = st.text_input("Budget", "$50,000")
    urgency = st.selectbox("Urgency Level", ["Low", "Medium", "High"])
    requirement = st.text_area(
        "Customer Requirement",
        "Immediate implementation required for enterprise rollout"
    )

    if st.button("Score Lead"):
        with st.spinner("Analyzing lead..."):
            prompt = lead_scoring_prompt(budget, urgency, requirement)
            result = get_ai_response(prompt)

        st.success("Lead Analysis Completed")
        st.text_area("Lead Scoring Result", result, height=300)