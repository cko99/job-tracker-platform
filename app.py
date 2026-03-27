import streamlit as st
from utils.export import create_tracker

st.set_page_config(page_title="Job Tracker", page_icon="💼", layout="wide")

st.markdown(
    """
    <style>
    .stApp { background: radial-gradient(circle at top left, #1a1f35 0%, #0f1324 45%, #090b16 100%); color: #ecf0ff; }
    .block-container { padding-top: 1.2rem; padding-bottom: 2rem; max-width: 1300px; }
    .header {
        display: flex; justify-content: space-between; align-items: center;
        background: rgba(18, 22, 39, 0.85); border: 1px solid rgba(106, 129, 209, 0.2);
        border-radius: 18px; padding: 1rem 1.2rem; margin-bottom: 1rem; backdrop-filter: blur(6px);
    }
    .metric-card {
        border-radius: 16px; padding: 1rem 1.1rem; color: #f6f8ff;
        border: 1px solid rgba(255, 255, 255, 0.07); box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35);
        min-height: 118px;
    }
    .metric-card h2 { margin: 0; font-size: 2rem; }
    .metric-card p { margin: 0.35rem 0 0; font-size: 1rem; opacity: 0.9; }
    .c1 { background: linear-gradient(140deg, #203056, #1e4f8d); }
    .c2 { background: linear-gradient(140deg, #4a3320, #7e5a24); }
    .c3 { background: linear-gradient(140deg, #173d39, #2a6a56); }
    .c4 { background: linear-gradient(140deg, #2f2856, #503f8a); }
    .panel {
        background: rgba(16, 20, 37, 0.85); border: 1px solid rgba(98, 117, 191, 0.2);
        border-radius: 16px; padding: 1rem; margin-top: 1rem;
    }
    .insight {
        background: rgba(42, 49, 77, 0.5); border-radius: 12px; padding: 0.8rem;
        margin-bottom: 0.7rem; border: 1px solid rgba(150, 173, 255, 0.16);
    }
    .job-list-item {
        display: flex; justify-content: space-between; align-items: center;
        background: rgba(28, 35, 59, 0.55); border-radius: 12px;
        border: 1px solid rgba(143, 165, 240, 0.16); padding: 0.75rem 0.8rem; margin-bottom: 0.6rem;
    }
    .tag { border-radius: 999px; padding: 0.22rem 0.6rem; font-size: 0.8rem; font-weight: 600; }
    .wishlist { background: rgba(74, 185, 141, 0.28); color: #bff5d6; }
    .interview { background: rgba(239, 195, 83, 0.28); color: #ffeeb8; }
    .applied { background: rgba(108, 177, 239, 0.28); color: #d6eeff; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="header">
      <h1 style="margin:0;">💼 Job Tracker</h1>
      <div style="opacity:0.9;">Dark Analytics Dashboard</div>
    </div>
    """,
    unsafe_allow_html=True,
)

metric_cols = st.columns(4)
for col, klass, value, label in [
    (metric_cols[0], "c1", "135", "Total Applications"),
    (metric_cols[1], "c2", "32.6%", "Response Rate"),
    (metric_cols[2], "c3", "19.3%", "Interview Rate"),
    (metric_cols[3], "c4", "7.4%", "Offer Rate"),
]:
    with col:
        st.markdown(
            f'<div class="metric-card {klass}"><h2>{value}</h2><p>{label}</p></div>',
            unsafe_allow_html=True,
        )

left, right = st.columns([1.4, 1])

with left:
    st.markdown('<div class="panel"><h3 style="margin-top:0;">Weekly Applications</h3></div>', unsafe_allow_html=True)
    st.line_chart(
        {
            "Applied": [15, 38, 42, 67, 49, 58, 84, 82, 99, 105],
            "Interviews": [7, 12, 20, 24, 17, 21, 40, 43, 57, 68],
            "Offers": [1, 4, 6, 8, 7, 7, 11, 14, 19, 24],
        }
    )

    st.markdown(
        """
        <div class="panel">
          <h3 style="margin-top:0;">Job Search Strategy Insights</h3>
          <div class="insight"><strong>Best Performing Role:</strong> Data Analyst</div>
          <div class="insight"><strong>Best Platform:</strong> LinkedIn</div>
          <div class="insight"><strong>Most responses:</strong> Mondays at 9 AM</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown('<div class="panel"><h3 style="margin-top:0;">Application Breakdown</h3></div>', unsafe_allow_html=True)
    st.bar_chart({"Applied": [36], "Interview": [23], "Offer": [37], "Rejected": [2]})

    st.markdown(
        """
        <div class="panel">
          <h3 style="margin-top:0;">Follow Up Now</h3>
          <div class="job-list-item"><div><strong>TechCorp</strong><br/><small>GIS Analyst</small></div><span class="tag wishlist">Wishlist</span></div>
          <div class="job-list-item"><div><strong>Novus Tech</strong><br/><small>Software Engineer</small></div><span class="tag interview">Interview</span></div>
          <div class="job-list-item"><div><strong>CreativeSoft</strong><br/><small>Data Analyst</small></div><span class="tag applied">Applied</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

if st.button("Export Excel"):
    create_tracker()
    st.success("Excel file generated!")
