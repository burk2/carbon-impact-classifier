# app.py

import streamlit as st

# Rule-based carbon impact data
carbon_data = {
    "flying": {"category": "Severe", "co2": 986, "tip": "Offset with trees or fly less often."},
    "plane": {"category": "Severe", "co2": 986, "tip": "Offset with trees or fly less often."},
    "beef": {"category": "High", "co2": 27, "tip": "Try plant-based swaps weekly."},
    "lamb": {"category": "High", "co2": 39, "tip": "Try lentils or beans instead."},
    "pork": {"category": "Moderate", "co2": 12, "tip": "Reduce frequency to cut emissions."},
    "chicken": {"category": "Moderate", "co2": 6.9, "tip": "Better than red meat, but plants are better."},
    "cheese": {"category": "High", "co2": 13.5, "tip": "Use alternatives like nut cheese or less often."},
    "streaming": {"category": "Moderate", "co2": 20, "tip": "Reduce video quality or stream less."},
    "bicycle": {"category": "Low", "co2": 0.01, "tip": "Great choice! Zero emissions."},
    "walking": {"category": "Low", "co2": 0.01, "tip": "Excellent – 100% emission free."},
    "train": {"category": "Moderate", "co2": 41, "tip": "Still better than flying or driving."},
    "bus": {"category": "Moderate", "co2": 68, "tip": "Shared travel cuts per-person emissions."},
    "car": {"category": "High", "co2": 271, "tip": "Carpool or switch to electric if possible."},
    "electric car": {"category": "Moderate", "co2": 73, "tip": "Clean if powered by renewable electricity."},
    "shower": {"category": "Low", "co2": 1.5, "tip": "Keep it short to save water and energy."},
    "laundry": {"category": "Moderate", "co2": 2.3, "tip": "Use cold water and full loads."}
}

st.title("🌍 AI Carbon Impact Classifier")

st.write("Type any daily activity or product to check its carbon impact:")

user_input = st.text_input("Enter activity or product:")

def classify_activity(text):
    text = text.lower()
    for keyword, data in carbon_data.items():
        if keyword in text:
            return data
    return {"category": "Unknown", "co2": None, "tip": "Sorry, no data available for this activity."}

if user_input:
    result = classify_activity(user_input)
    st.markdown(f"### 🧠 Carbon Impact Category: **{result['category']}**")
    if result["co2"] is not None:
        st.markdown(f"**🌡️ Estimated CO₂ emissions:** {result['co2']} kg")
    st.markdown(f"💬 **Sustainability Tip:** {result['tip']}")
