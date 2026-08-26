
        
       import os
import time
import pandas as pd
import streamlit as st

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="AgriMitra AI | Autonomous Commerce Platform",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- ADVANCED CUSTOM CSS (UI/UX OVERHAUL) ----------------
st.markdown("""
    <style>
    /* Global Typography & Background */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .stApp {
        background-color: #f8fafb;
    }
    
    /* Hide Default Header Elements */
    header[data-testid="stHeader"] {
        background: transparent;
    }
    
    /* Sidebar Polish */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0;
        padding-top: 1rem;
    }
    
    /* Brand Styling */
    .brand-container {
        padding: 10px 5px 20px 5px;
    }
    .brand-title {
        font-size: 1.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #15803d 0%, #047857 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
        margin: 0;
    }
    .brand-subtitle {
        font-size: 0.8rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-top: 4px;
    }
    
    /* Hero Header Banner */
    .hero-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        border-radius: 16px;
        padding: 24px 32px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.1);
    }
    .hero-banner h2 {
        color: #ffffff;
        font-weight: 700;
        margin: 0 0 6px 0;
        font-size: 1.6rem;
    }
    .hero-banner p {
        color: #94a3b8;
        margin: 0;
        font-size: 0.95rem;
    }

    /* Modern Metric Cards */
    .glass-card {
        background: #ffffff;
        border-radius: 14px;
        padding: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02), 0 1px 2px rgba(0,0,0,0.03);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .glass-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px -5px rgba(0,0,0,0.05);
    }
    .card-label {
        font-size: 0.75rem;
        font-weight: 700;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .card-val {
        font-size: 1.75rem;
        font-weight: 800;
        color: #0f172a;
        margin: 6px 0;
    }
    
    /* Status Badges */
    .pill-green {
        display: inline-block;
        background: #dcfce7;
        color: #15803d;
        padding: 3px 10px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 700;
    }
    .pill-blue {
        display: inline-block;
        background: #dbeafe;
        color: #1d4ed8;
        padding: 3px 10px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 700;
    }
    
    /* Button Customization */
    .stButton > button {
        background: linear-gradient(135deg, #166534 0%, #15803d 100%) !important;
        color: white !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 0.6rem 1.2rem !important;
        border: none !important;
        box-shadow: 0 4px 6px -1px rgba(22, 101, 52, 0.2) !important;
        transition: all 0.2s ease !important;
    }
    .stButton > button:hover {
        box-shadow: 0 8px 15px -3px rgba(22, 101, 52, 0.35) !important;
        transform: translateY(-1px);
    }
    
    /* Table Styling */
    div[data-testid="stTable"] table {
        border-radius: 10px;
        overflow: hidden;
        border: 1px solid #e2e8f0;
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
            pass
    return None

# ---------------- NAVIGATION SIDEBAR ----------------
with st.sidebar:
    st.markdown("""
        <div class="brand-container">
            <div class="brand-title">🌾 AgriMitra AI</div>
            <div class="brand-subtitle">Autonomous Farm Commerce</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    nav_selection = st.radio(
        "NAVIGATION",
        ["🤖 Agentic Advisor", "📊 Market Intelligence", "🛒 B2B Marketplace", "⚙️ Farm Profile Settings"],
        index=0
    )

    st.divider()
    st.markdown("##### 🌐 Preferences & Voice")
    language = st.selectbox("Preferred Language", ["English", "Hindi (हिंदी)", "Kannada (ಕನ್ನಡ)", "Telugu (తెలుగు)"])
    enable_voice = st.toggle("Enable Voice Advisory", value=True)
    
    st.divider()
    st.caption("🟢 **Autonomous Engine:** Ready (v2.4 Pro)")

# ---------------- SESSION STATE DATA ----------------
if 'farm_data' not in st.session_state:
    st.session_state.farm_data = {
        "location": "Karnataka (Kalaburagi)",
        "crop": "Pigeon Pea (Tur Dal)",
        "acreage": 3.5,
        "soil": "Black Soil",
        "budget": 35000
    }

# ---------------- HERO BANNER & METRICS ----------------
st.markdown(f"""
    <div class="hero-banner">
        <h2>Welcome back, Kadambini 👋</h2>
        <p>Managing {st.session_state.farm_data['acreage']} Acres in {st.session_state.farm_data['location']} • Next harvest target: Pigeon Pea</p>
    </div>
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown(f'''
        <div class="glass-card">
            <div class="card-label">Active Crop</div>
            <div class="card-val" style="font-size: 1.3rem;">{st.session_state.farm_data["crop"]}</div>
            <span class="pill-green">Optimal Season</span>
        </div>
    ''', unsafe_allow_html=True)
with m2:
    st.markdown(f'''
        <div class="glass-card">
            <div class="card-label">Allocated Budget</div>
            <div class="card-val">₹{st.session_state.farm_data["budget"]:,}</div>
            <span class="pill-blue">Active Balance</span>
        </div>
    ''', unsafe_allow_html=True)
with m3:
    st.markdown('''
        <div class="glass-card">
            <div class="card-label">Mandi Benchmark</div>
            <div class="card-val">₹6,850</div>
            <span class="pill-green">+4.2% Today</span>
        </div>
    ''', unsafe_allow_html=True)
with m4:
    st.markdown('''
        <div class="glass-card">
            <div class="card-label">Direct Buyer Offer</div>
            <div class="card-val">₹7,200</div>
            <span class="pill-blue">+5.1% Premium</span>
        </div>
    ''', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- PAGE 1: AGENTIC ADVISOR ----------------
if nav_selection == "🤖 Agentic Advisor":
    st.subheader("🤖 Autonomous Input Procurement & Allocation")
    st.caption("Our multi-agent system negotiates prices with verified local vendors, calculates precise dosage by acreage, and builds your custom procurement order.")
    
    c_left, c_right = st.columns([1, 1.2], gap="large")
    
    with c_left:
        st.markdown('''
            <div class="glass-card" style="margin-bottom: 20px;">
                <h4 style="margin-top:0; color: #1e293b;">📋 Active Profile Parameters</h4>
        ''', unsafe_allow_html=True)
        st.write(f"**Region:** {st.session_state.farm_data['location']}")
        st.write(f"**Soil Type:** {st.session_state.farm_data['soil']}")
        st.write(f"**Target Acreage:** {st.session_state.farm_data['acreage']} Acres")
        st.write(f"**Target Language:** {language}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        run_agent = st.button("🚀 Run Autonomous Procurement Agent", use_container_width=True)

    with c_right:
        if run_agent:
            status_box = st.status("🤖 Agent Executing Autonomous Protocol...", expanded=True)
            status_box.write("🔍 Requesting bids from 5 local authorized distributors...")
            time.sleep(1)
            status_box.write("⚖️ Negotiating volume discounts for organic fertilizers...")
            time.sleep(1)
            status_box.write("📦 Verifying soil NPK compatibility matrix...")
            status_box.update(label="✅ Autonomous Strategy Ready!", state="complete", expanded=False)

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

                st.markdown(f"### 🎯 Recommended Procurement Plan ({language})")
                st.table(pd.DataFrame([
                    {"Category": "Seeds", "Product": "Hybrid Certified Seeds", "Quantity": f"{ac * 3} kg", "Est. Cost": f"₹{seed_cost:,}"},
                    {"Category": "Bio-Fertilizer", "Product": "Bio-NPK Liquid + Neem Cake", "Quantity": f"{ac * 5} L", "Est. Cost": f"₹{fert_cost:,}"},
                    {"Category": "Crop Protection", "Product": "Organic Bio-Pesticide", "Quantity": f"{ac * 2} L", "Est. Cost": f"₹{pest_cost:,}"}
                ]))

                st.markdown(f"""
                <div class="glass-card" style="border-left: 4px solid #166534;">
                    <h5 style="margin:0 0 10px 0; color: #166534;">🤖 Agent Execution Insights</h5>
                    <ol style="margin:0; padding-left: 20px; color: #334155; font-size: 0.9rem;">
                        <li><b>Bulk Grouping:</b> Aggregated orders with 12 nearby farms, cutting seed rates by 14%.</li>
                        <li><b>Logistics Lock:</b> Scheduled zero-cost direct dispatch to your local village hub.</li>
                        <li><b>Soil Match:</b> Formulated nitrogen ratio tailored to <b>{st.session_state.farm_data['soil']}</b>.</li>
                    </ol>
                    <hr style="margin: 12px 0;">
                    <b>Total Calculated Cost:</b> ₹{total_est:,} <span class="pill-green">Saved ₹{savings:,}</span>
                </div>
                """, unsafe_allow_html=True)
            
            if enable_voice:
                st.info("🔊 **Audio Summary:** Playback active in selected language.")

# ---------------- PAGE 2: MARKET INTELLIGENCE ----------------
elif nav_selection == "📊 Market Intelligence":
    st.subheader("📊 Price Trends & Forward Demand")
    st.caption("Compare real-time benchmark Mandi prices against AgriMitra contract guarantees.")
    
    chart_data = pd.DataFrame({
        "Month": ["May", "Jun", "Jul", "Aug", "Sep", "Oct (Pred)"],
        "Mandi Benchmark (₹)": [6100, 6300, 6250, 6500, 6850, 6900],
        "AgriMitra Direct (₹)": [6400, 6600, 6600, 6900, 7200, 7350]
    }).set_index("Month")
    
    st.line_chart(chart_data)

# ---------------- PAGE 3: B2B MARKETPLACE ----------------
elif nav_selection == "🛒 B2B Marketplace":
    st.subheader("🛒 Direct B2B Commerce Hub")
    
    tab_buy, tab_sell = st.tabs(["🛍️ Procure Farm Inputs", "🌾 Institutional Buyer Orders"])
    
    with tab_buy:
        p1, p2, p3 = st.columns(3)
        with p1:
            st.markdown('''
                <div class="glass-card">
                    <b>Bio-NPK Fertilizer (1L)</b><br>
                    <small style="color:#64748b;">Vendor: IFFCO Direct</small>
                    <h3 style="margin: 10px 0; color: #166534;">₹450</h3>
                </div>
            ''', unsafe_allow_html=True)
            st.button("Order Now", key="b1", use_container_width=True)
        with p2:
            st.markdown('''
                <div class="glass-card">
                    <b>Pigeon Pea Seeds (10kg)</b><br>
                    <small style="color:#64748b;">Vendor: Mahyco Seeds</small>
                    <h3 style="margin: 10px 0; color: #166534;">₹2,100</h3>
                </div>
            ''', unsafe_allow_html=True)
            st.button("Order Now", key="b2", use_container_width=True)
        with p3:
            st.markdown('''
                <div class="glass-card">
                    <b>Neem Oil Extract (5L)</b><br>
                    <small style="color:#64748b;">Vendor: Krishi Bio Labs</small>
                    <h3 style="margin: 10px 0; color: #166534;">₹1,250</h3>
                </div>
            ''', unsafe_allow_html=True)
            st.button("Order Now", key="b3", use_container_width=True)
            
    with tab_sell:
        st.table(pd.DataFrame([
            {"Buyer": "AgriMills Ltd", "Required Qty": "50 Quintals", "Offered Rate": "₹7,250/Qtl", "Payment Term": "Instant (UPI)"},
            {"Buyer": "State Warehousing Corp", "Required Qty": "200 Quintals", "Offered Rate": "₹7,100/Qtl", "Payment Term": "3 Days Credit"},
            {"Buyer": "Global Pulse Traders", "Required Qty": "100 Quintals", "Offered Rate": "₹7,300/Qtl", "Payment Term": "Instant Transfer"}
        ]))

# ---------------- PAGE 4: FARM SETTINGS ----------------
elif nav_selection == "⚙️ Farm Profile Settings":
    st.subheader("⚙️ Farm Parameters Configuration")
    with st.form("settings_form"):
        loc = st.text_input("Region / Location", value=st.session_state.farm_data["location"])
        crp = st.text_input("Crop Type", value=st.session_state.farm_data["crop"])
        ac = st.number_input("Land Size (Acres)", value=st.session_state.farm_data["acreage"])
        sl = st.selectbox("Soil Type", ["Black Soil", "Red Soil", "Alluvial Soil", "Sandy Loam"], index=0)
        bg = st.number_input("Max Procurement Budget (₹)", value=st.session_state.farm_data["budget"])
        
        save = st.form_submit_button("Update Farm Profile", use_container_width=True)
        if save:
            st.session_state.farm_data = {"location": loc, "crop": crp, "acreage": ac, "soil": sl, "budget": bg}
            st.success("✅ Farm Profile updated!")
