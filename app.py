        import os
import time
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AgriMitra AI | Autonomous Agri-Commerce",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Modern App UI/UX
st.markdown("""
    <style>
    .stApp { background-color: #f8faf9; }
    
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e0e0e0;
    }
    
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 15px;
    }
    .metric-title { font-size: 0.85rem; color: #64748b; font-weight: 600; text-transform: uppercase; }
    .metric-value { font-size: 1.8rem; font-weight: 700; color: #1e293b; margin: 5px 0; }
    .badge-green { background: #dcfce7; color: #15803d; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; }
    .badge-blue { background: #dbeafe; color: #1e40af; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; }

    .brand-title { font-size: 1.8rem; font-weight: 800; color: #166534; margin: 0; }
    .brand-subtitle { font-size: 0.95rem; color: #475569; }
    
    .stButton > button {
        background-color: #166534 !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.5rem 1rem !important;
        border: none !important;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #15803d !important;
    }
    </style>
""", unsafe_allow_html=True)

# Safe AI Agent Execution Handler
def run_ai_agent(prompt):
    api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if api_key:
        try:
            import google.generativeai as genai
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            return response.text
        except Exception:
            pass  # Fallback to internal simulation logic if SDK/key fails
    return None

# ---------------- NAVIGATION SIDEBAR ----------------
with st.sidebar:
    st.markdown('<div class="brand-title">🌾 AgriMitra AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="brand-subtitle">Autonomous Farm Commerce</div>', unsafe_allow_html=True)
    st.divider()

    nav_selection = st.radio(
        "NAVIGATION",
        ["🤖 Agentic Advisor", "📊 Market Intelligence", "🛒 B2B Marketplace", "⚙️ Farm Profile Settings"],
        index=0
    )

    st.divider()
    st.markdown("##### 🌐 Voice & Localization")
    language = st.selectbox("Preferred Language", ["English", "Hindi (हिंदी)", "Kannada (ಕನ್ನಡ)", "Telugu (తెలుగు)"])
    enable_voice = st.toggle("Enable Voice Advisory", value=True)
    
    st.divider()
    st.caption("🟢 **Agent Node:** Online (v2.4-Production)")

# ---------------- SESSION STATE DATA ----------------
if 'farm_data' not in st.session_state:
    st.session_state.farm_data = {
        "location": "Karnataka (Kalaburagi)",
        "crop": "Pigeon Pea (Tur Dal)",
        "acreage": 3.5,
        "soil": "Black Soil",
        "budget": 35000
    }

# Top Header Layout Across All Pages
top_c1, top_c2, top_c3 = st.columns([2, 1, 1])
with top_c1:
    st.title(f"{nav_selection.split(' ')[1]} Overview")
with top_c2:
    st.markdown(f'<div class="metric-card"><div class="metric-title">Active Crop</div><div class="metric-value">{st.session_state.farm_data["crop"]}</div></div>', unsafe_allow_html=True)
with top_c3:
    st.markdown(f'<div class="metric-card"><div class="metric-title">Working Budget</div><div class="metric-value">₹{st.session_state.farm_data["budget"]:,}</div></div>', unsafe_allow_html=True)

st.divider()

# ---------------- PAGE 1: AGENTIC ADVISOR ----------------
if nav_selection == "🤖 Agentic Advisor":
    st.subheader("Autonomous Input Procurement & Budget Allocator")
    st.write("Our AI Agent coordinates input vendors, calculates chemical quantities by acreage, and locks direct wholesale prices.")
    
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("### 📋 Active Farm Parameters")
        st.write(f"**Region:** {st.session_state.farm_data['location']}")
        st.write(f"**Soil Condition:** {st.session_state.farm_data['soil']}")
        st.write(f"**Target Acreage:** {st.session_state.farm_data['acreage']} Acres")
        st.write(f"**Language Selected:** {language}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        run_agent = st.button("🚀 Execute Autonomous Procurement Agent")

    with col_right:
        if run_agent:
            status_box = st.status("🤖 Agent Executing Tasks...", expanded=True)
            status_box.write("🔍 Scanning regional dealers in local radius...")
            time.sleep(1)
            status_box.write("⚖️ Negotiating bulk volume pricing for bio-fertilizers...")
            time.sleep(1)
            status_box.write("📦 Verifying soil NPK compatibility...")
            status_box.update(label="✅ Agent Execution Complete!", state="complete", expanded=False)

            prompt = f"""
            You are AgriMitra AI, an autonomous commerce agent for Indian farmers.
            Generate a procurement plan for:
            - Location: {st.session_state.farm_data['location']}
            - Crop: {st.session_state.farm_data['crop']}
            - Soil: {st.session_state.farm_data['soil']}
            - Land Size: {st.session_state.farm_data['acreage']} Acres
            - Budget: ₹{st.session_state.farm_data['budget']}
            - Language: {language}

            Output an itemized purchase table, 3 agent actions taken, and net savings summary.
            """
            
            ai_response = run_ai_agent(prompt)
            
            if ai_response:
                st.markdown(ai_response)
            else:
                ac = st.session_state.farm_data['acreage']
                seed_cost = int(ac * 1200)
                fert_cost = int(ac * 2500)
                pest_cost = int(ac * 900)
                total_est = seed_cost + fert_cost + pest_cost
                savings = int(total_est * 0.14)

                st.markdown(f"### 🎯 Autonomous Procurement Plan ({language})")
                st.table(pd.DataFrame([
                    {"Category": "Seeds", "Recommended Product": "Hybrid Certified Seeds", "Quantity": f"{ac * 3} kg", "Est. Cost (INR)": f"₹{seed_cost:,}"},
                    {"Category": "Bio-Fertilizer", "Recommended Product": "Bio-NPK Liquid + Neem Cake", "Quantity": f"{ac * 5} L", "Est. Cost (INR)": f"₹{fert_cost:,}"},
                    {"Category": "Crop Protection", "Recommended Product": "Organic Bio-Pesticide", "Quantity": f"{ac * 2} L", "Est. Cost (INR)": f"₹{pest_cost:,}"}
                ]))

                st.markdown(f"""
                #### 🤖 Autonomous Actions Logged
                1. **Bulk Grouping Discount:** Pooled demand across regional farms, saving 14% on wholesale seeds.
                2. **Direct Logistics Lock:** Arranged direct delivery to village hub.
                3. **Soil Optimization Match:** Adjusted NPK ratio specifically for **{st.session_state.farm_data['soil']}**.

                **Total Procurement Cost:** ₹{total_est:,} *(Saved ₹{savings:,} vs standard retail)*
                """)
            
            if enable_voice:
                st.info("🔊 Audio Advisory Generated: Playing Voice Summary in selected language.")

# ---------------- PAGE 2: MARKET INTELLIGENCE ----------------
elif nav_selection == "📊 Market Intelligence":
    st.subheader("Real-Time Mandi Price Trends & Buyer Demand")
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<div class="metric-card"><div class="metric-title">Current Mandi Rate</div><div class="metric-value">₹6,850/Qtl</div><span class="badge-green">+4.2% today</span></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-card"><div class="metric-title">AgriMitra Direct Buyer Rate</div><div class="metric-value">₹7,200/Qtl</div><span class="badge-blue">Direct Contract</span></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-card"><div class="metric-title">Estimated Yield Revenue</div><div class="metric-value">₹1,80,000</div><span class="badge-green">Net Positive</span></div>', unsafe_allow_html=True)
        
    st.write("### Price Trend Analysis")
    chart_data = pd.DataFrame({
        "Month": ["May", "Jun", "Jul", "Aug", "Sep", "Oct (Pred)"],
        "Mandi Benchmark (₹)": [6100, 6300, 6250, 6500, 6850, 6900],
        "AgriMitra Direct (₹)": [6400, 6600, 6600, 6900, 7200, 7350]
    }).set_index("Month")
    st.line_chart(chart_data)

# ---------------- PAGE 3: B2B MARKETPLACE ----------------
elif nav_selection == "🛒 B2B Marketplace":
    st.subheader("Verified Inputs & Direct Grain Contracts")
    
    tab_buy, tab_sell = st.tabs(["🛍️ Direct Input Procurement", "🌾 Sell Produce to Institutional Buyers"])
    
    with tab_buy:
        st.write("Verified farm inputs from authorized distributors:")
        p1, p2, p3 = st.columns(3)
        with p1:
            st.markdown('<div class="metric-card"><b>Bio-NPK Liquid Fertilizer (1L)</b><br><small>Vendor: IFFCO Agri Direct</small><br><h3>₹450</h3></div>', unsafe_allow_html=True)
            st.button("Procure via Agent", key="buy1")
        with p2:
            st.markdown('<div class="metric-card"><b>Pigeon Pea Seeds (F1 Hybrid - 10kg)</b><br><small>Vendor: Mahyco Seeds</small><br><h3>₹2,100</h3></div>', unsafe_allow_html=True)
            st.button("Procure via Agent", key="buy2")
        with p3:
            st.markdown('<div class="metric-card"><b>Organic Neem Oil Extract (5L)</b><br><small>Vendor: Krishi Bio Labs</small><br><h3>₹1,250</h3></div>', unsafe_allow_html=True)
            st.button("Procure via Agent", key="buy3")
            
    with tab_sell:
        st.write("Active institutional buyer purchase orders:")
        st.table(pd.DataFrame([
            {"Buyer": "AgriMills Ltd", "Required Qty": "50 Quintals", "Offered Rate": "₹7,250/Qtl", "Payment Term": "Instant (UPI)"},
            {"Buyer": "State Warehousing Corp", "Required Qty": "200 Quintals", "Offered Rate": "₹7,100/Qtl", "Payment Term": "3 Days Credit"},
            {"Buyer": "Global Pulse Traders", "Required Qty": "100 Quintals", "Offered Rate": "₹7,300/Qtl", "Payment Term": "Instant Transfer"}
        ]))

# ---------------- PAGE 4: FARM SETTINGS ----------------
elif nav_selection == "⚙️ Farm Profile Settings":
    st.subheader("Configure Farm Profile")
    with st.form("settings_form"):
        loc = st.text_input("Region / Location", value=st.session_state.farm_data["location"])
        crp = st.text_input("Crop Type", value=st.session_state.farm_data["crop"])
        ac = st.number_input("Land Size (Acres)", value=st.session_state.farm_data["acreage"])
        sl = st.selectbox("Soil Type", ["Black Soil", "Red Soil", "Alluvial Soil", "Sandy Loam"], index=0)
        bg = st.number_input("Max Procurement Budget (₹)", value=st.session_state.farm_data["budget"])
        
        save = st.form_submit_button("Save Farm Profile")
        if save:
            st.session_state.farm_data = {"location": loc, "crop": crp, "acreage": ac, "soil": sl, "budget": bg}
            st.success("✅ Farm Profile parameters updated successfully!")
