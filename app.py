import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(
    page_title="ZAPPYBOO | AI Study Planner",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Theme ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {
        --bg: #0b1020;
        --panel: #121a2d;
        --panel-soft: #172139;
        --border: rgba(155, 174, 220, .16);
        --muted: #9aa9c7;
        --text: #f4f7ff;
        --purple: #9b8cff;
        --blue: #6cbcff;
        --mint: #65e6c4;
    }

    .stApp {
        background:
            radial-gradient(ellipse at 12% 0%, rgba(92, 80, 190, .20), transparent 34%),
            radial-gradient(ellipse at 95% 15%, rgba(38, 143, 194, .13), transparent 30%),
            var(--bg);
        color: var(--text);
        font-family: 'DM Sans', sans-serif;
    }
    h1, h2, h3, h4, p, label, .stMarkdown {
        font-family: 'DM Sans', sans-serif;
    }
    h1, h2, h3 { color: var(--text) !important; }
    p, label, .stCaption { color: #c0cbe0; }
    [data-testid="stSidebar"] {
        background: #0d1426;
        border-right: 1px solid var(--border);
    }
    [data-testid="stSidebar"] p { color: #b8c5df; }
    .hero {
        padding: 28px 30px;
        border-radius: 24px;
        border: 1px solid rgba(155, 140, 255, .26);
        background: linear-gradient(120deg, rgba(105, 87, 210, .23), rgba(38, 142, 186, .12) 60%, rgba(18, 26, 45, .75));
        margin: 6px 0 22px 0;
    }
    .eyebrow {
        color: #b9adff;
        text-transform: uppercase;
        font-size: .76rem;
        font-weight: 800;
        letter-spacing: .16em;
        margin-bottom: 10px;
    }
    .hero h1 {
        font-family: 'Manrope', sans-serif;
        font-size: clamp(2rem, 4vw, 3.1rem);
        font-weight: 800;
        line-height: 1.08;
        margin: 0 0 12px 0;
        letter-spacing: -.04em;
    }
    .hero p {
        color: #c4cce2;
        font-size: 1.02rem;
        max-width: 720px;
        margin: 0;
        line-height: 1.65;
    }
    .section-kicker {
        color: #a99cff;
        font-size: .75rem;
        font-weight: 800;
        letter-spacing: .13em;
        text-transform: uppercase;
        margin-bottom: 5px;
    }
    .metric-card {
        background: linear-gradient(145deg, rgba(24, 35, 60, .98), rgba(16, 24, 42, .98));
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 18px 19px;
        min-height: 112px;
    }
    .metric-label {
        color: #a9b7d2;
        font-size: .84rem;
        margin-bottom: 9px;
    }
    .metric-value {
        color: #f5f7ff;
        font-family: 'Manrope', sans-serif;
        font-size: 1.8rem;
        font-weight: 800;
        letter-spacing: -.04em;
    }
    .metric-foot {
        color: #7f91b5;
        font-size: .76rem;
        margin-top: 3px;
    }
    .result-card {
        border: 1px solid rgba(155, 140, 255, .28);
        border-radius: 20px;
        padding: 22px 24px;
        background: linear-gradient(120deg, rgba(113, 93, 221, .17), rgba(20, 31, 54, .86));
        margin: 8px 0 18px 0;
    }
    .result-title {
        color: #b9adff;
        font-size: .75rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: .13em;
    }
    .result-value {
        color: #fff;
        font-family: 'Manrope', sans-serif;
        font-size: 1.8rem;
        font-weight: 800;
        margin: 7px 0;
    }
    .result-copy { color: #c3cde2; line-height: 1.6; }
    .soft-card {
        background: rgba(18, 26, 45, .86);
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 18px 20px;
        height: 100%;
    }
    .tip {
        background: rgba(101, 230, 196, .08);
        border: 1px solid rgba(101, 230, 196, .20);
        border-radius: 14px;
        padding: 14px 16px;
        color: #c9f6e9;
        line-height: 1.55;
    }
    div.stButton > button, div.stFormSubmitButton > button {
        border: 0;
        border-radius: 12px;
        background: linear-gradient(100deg, #8875ff, #5bafff);
        color: #fff;
        font-weight: 800;
        min-height: 46px;
        transition: all .2s ease;
    }
    div.stButton > button:hover, div.stFormSubmitButton > button:hover {
        border: 0;
        filter: brightness(1.08);
        transform: translateY(-1px);
        color: #fff;
    }
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {
        background: #111a2d;
        border-color: rgba(155, 174, 220, .22);
        border-radius: 10px;
    }
    [data-testid="stMetric"] {
        background: rgba(18, 26, 45, .82);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 16px;
    }
    [data-testid="stDataFrame"] {
        border: 1px solid var(--border);
        border-radius: 12px;
        overflow: hidden;
    }
    .footer {
        color: #7182a5;
        text-align: center;
        font-size: .78rem;
        padding: 22px 0 8px 0;
    }
    @media (max-width: 700px) {
        .hero { padding: 22px 19px; border-radius: 18px; }
        .metric-card { padding: 14px; min-height: 100px; }
        .metric-value { font-size: 1.5rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Train demonstration ML model ----------
@st.cache_resource
def train_model():
    rng = np.random.default_rng(42)
    n = 2000

    marks = rng.uniform(0, 100, n)
    syllabus = rng.uniform(0, 100, n)
    practice = rng.uniform(0, 100, n)

    score = (
        0.25 * marks
        + 0.35 * syllabus
        + 0.40 * practice
        + rng.normal(0, 5, n)
    )

    labels = np.where(
        score < 45,
        "Needs More Practice",
        np.where(score < 70, "Getting Ready", "Well Prepared"),
    )

    X = np.column_stack([marks, syllabus, practice])
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, labels)
    return model


model = train_model()

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("## ⚡ZAPPYBOO")
    st.caption("AI-powered study companion")
    st.markdown("---")
    st.markdown("### ✨ How it works")
    st.markdown(
        """
        1. Add your current preparation details.
        2. Generate your study plan.
        3. Review your readiness estimate.
        4. Use your daily timetable.
        """
    )
    st.markdown("---")
    st.markdown("### 💡 Study tip")
    st.info("Short, focused sessions with regular breaks can make revision easier.")
    st.markdown("---")
    st.caption("MINI PROJECT · PYTHON + MACHINE LEARNING")
    st.caption("Demo model — educational use only")

# ---------- Hero ----------
st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">Your personal learning dashboard</div>
        <h1>Study smarter.<br>Feel more prepared.</h1>
        <p>Choose a subject and get a general timetable by default, or optionally enter topics for a day-by-day topic-wise plan.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- Input panel ----------
st.markdown('<div class="section-kicker">01 / Your preparation</div>', unsafe_allow_html=True)
st.header("Let’s plan your next study session")
st.write("Enter your latest scores and available time to generate a personalised plan.")

with st.form("study_form", border=True):
    name = st.text_input("Student name", placeholder="Enter your name")

    left, right = st.columns(2)
    with left:
        marks = st.slider("Previous exam marks (%)", 0, 100, 60)
        syllabus = st.slider("Syllabus completed (%)", 0, 100, 50)
        practice = st.slider("Practice test score (%)", 0, 100, 55)

    with right:
        days = st.number_input("Days until exam", min_value=1, max_value=180, value=7)
        hours = st.slider("Study hours available per day", 1, 12, 3)
        subject = st.selectbox(
            "Choose a subject",
            ["Operating Systems", "Python Programming", "Mathematics", "Computer Networks", "Database Management Systems", "Other / Custom Subject"],
        )
        custom_subject = ""
        if subject == "Other / Custom Subject":
            custom_subject = st.text_input("Enter your subject name", placeholder="e.g. Data Structures")

        plan_mode = st.radio(
            "Choose your plan type",
            ["General timetable", "Topic-wise plan (optional)"],
            horizontal=True,
            help="General timetable is the default. Choose topic-wise only when you want to enter topics manually.",
        )
        topics_text = ""
        if plan_mode == "Topic-wise plan (optional)":
            topics_text = st.text_area(
                "Enter topics (one topic per line)",
                value="",
                height=150,
                placeholder="Example:\nProcess Management\nCPU Scheduling\nDeadlocks",
                help="Optional: enter your own syllabus topics, one per line. Leave blank to use the general timetable instead.",
            )

    submitted = st.form_submit_button("✨ Generate my study plan", use_container_width=True)

# ---------- Results ----------
if submitted:
    student = name.strip() or "Student"
    selected_subject = custom_subject.strip() if subject == "Other / Custom Subject" else subject
    if not selected_subject:
        st.error("Please enter a subject name.")
        st.stop()
    topic_list = [topic.strip() for topic in topics_text.splitlines() if topic.strip()]
    # If the user chooses topic-wise mode but leaves the topic list empty,
    # fall back to the regular general timetable as requested.
    use_topic_plan = plan_mode == "Topic-wise plan (optional)" and bool(topic_list)

    st.markdown("---")
    st.markdown('<div class="section-kicker">02 / Your dashboard</div>', unsafe_allow_html=True)
    st.header(f"Welcome, {student} 👋")
    st.caption("Here’s your current preparation snapshot.")

    metric_cols = st.columns(4)
    metrics = [
        ("Exam marks", f"{marks}%", "Previous performance"),
        ("Syllabus done", f"{syllabus}%", "Topics covered"),
        ("Practice score", f"{practice}%", "Practice test result"),
        ("Days left", f"{int(days)}", "Until your exam"),
    ]
    for col, (label, value, foot) in zip(metric_cols, metrics):
        col.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-foot">{foot}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    prediction = model.predict(np.array([[marks, syllabus, practice]]))[0]
    messages = {
        "Needs More Practice": "Focus on core concepts, then practise a small set of questions each day.",
        "Getting Ready": "You’re building momentum. Keep revising and test yourself regularly.",
        "Well Prepared": "Keep your knowledge fresh with revision and timed mock tests.",
    }
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-kicker">03 / Readiness check</div>', unsafe_allow_html=True)
    st.header("Exam readiness estimate")

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-title">Your current status</div>
            <div class="result-value">{prediction}</div>
            <div class="result-copy">{messages[prediction]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    indicator = round(0.25 * marks + 0.35 * syllabus + 0.40 * practice)
    st.markdown("#### Preparation indicator")
    st.progress(indicator / 100)
    st.write(f"**{indicator}/100** · A weighted summary of the three inputs")

    with st.expander("About this prediction"):
        st.write(
            "This prototype's Random Forest model is trained on synthetic sample data. "
            "The result is an educational estimate, not a validated prediction of actual exam results."
        )

    st.markdown("---")
    st.markdown('<div class="section-kicker">04 / Performance</div>', unsafe_allow_html=True)
    st.header("Your performance overview")
    chart_data = pd.DataFrame(
        {
            "Category": ["Exam marks", "Syllabus completed", "Practice score"],
            "Percentage": [marks, syllabus, practice],
        }
    ).set_index("Category")
    st.bar_chart(chart_data, y="Percentage", color="#8e7cff")

    st.markdown("---")
    st.markdown('<div class="section-kicker">05 / Your study timetable</div>', unsafe_allow_html=True)
    total_minutes = int(hours * 60)

    if use_topic_plan:
        st.header(f"{selected_subject}: topic-wise study plan")
        days_for_plan = min(int(days), len(topic_list))
        # Spread topics across the days before the exam; multiple topics may share a day.
        topic_groups = [[] for _ in range(days_for_plan)]
        for i, topic in enumerate(topic_list):
            topic_groups[i % days_for_plan].append(topic)

        timetable = []
        for day_index, day_topics in enumerate(topic_groups, start=1):
            per_topic = max(10, total_minutes // max(1, len(day_topics)))
            for topic in day_topics:
                timetable.append({
                    "Study day": f"Day {day_index}",
                    "Subject": selected_subject,
                    "Topic to study": topic,
                    "Suggested time": f"{per_topic} min",
                    "Task": "Understand concepts + make short notes + solve questions",
                })

        st.markdown(
            f'<div class="tip">📅 Subject: <b>{selected_subject}</b> · Topics: <b>{len(topic_list)}</b> · '
            f'Daily study time: <b>{total_minutes} minutes</b>. This is a suggested schedule; edit the topic list to match your syllabus.</div>',
            unsafe_allow_html=True,
        )
        st.dataframe(pd.DataFrame(timetable), use_container_width=True, hide_index=True)
        csv_data = pd.DataFrame(timetable).to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Download topic-wise plan (CSV)",
            data=csv_data,
            file_name="study_buddy_topic_plan.csv",
            mime="text/csv",
        )
    else:
        st.header("General daily study timetable")
        st.caption("No topics needed — your subjects are split into balanced study sessions.")
        subject_names = [x.strip() for x in subjects.split(",") if x.strip()] if "subjects" in locals() else []
        # Use the selected subject as the general timetable's subject list by default.
        if not subject_names:
            subject_names = [selected_subject]
        base = total_minutes // len(subject_names)
        remainder = total_minutes % len(subject_names)
        general_rows = []
        for i, subject_name in enumerate(subject_names):
            allocated = base + (1 if i < remainder else 0)
            general_rows.append({
                "Study day": "Every day",
                "Subject": subject_name,
                "Daily study time": f"{allocated} min",
                "Suggested task": "Review class notes, study key concepts, practise questions, and recap",
            })
        st.markdown(
            f'<div class="tip">📅 Subject: <b>{selected_subject}</b> · Daily study time: '
            f'<b>{total_minutes} minutes</b>. Switch to Topic-wise plan only when you want to enter specific topics.</div>',
            unsafe_allow_html=True,
        )
        st.dataframe(pd.DataFrame(general_rows), use_container_width=True, hide_index=True)
        general_csv = pd.DataFrame(general_rows).to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Download general timetable (CSV)",
            data=general_csv,
            file_name="study_buddy_general_timetable.csv",
            mime="text/csv",
        )

    st.markdown("---")
    st.markdown('<div class="section-kicker">06 / Next actions</div>', unsafe_allow_html=True)
    st.header("Study recommendations")
    recommendations = []
    if syllabus < 50:
        recommendations.append(("📘", "Prioritise unfinished syllabus topics and split them into smaller tasks."))
    if practice < 50:
        recommendations.append(("✍️", "Practise questions and review the mistakes you make."))
    if marks < 50:
        recommendations.append(("🧠", "Revise the fundamentals before moving to advanced topics."))
    if syllabus >= 50 and practice >= 50 and marks >= 50:
        recommendations.append(("🎯", "Keep revising and take timed mock tests to find gaps."))
    recommendations.append(("🗓️", f"Set weekly milestones for the next {int(days)} day(s)."))
    recommendations.append(("☕", "Take short breaks and quickly recap each topic after studying."))

    rec_cols = st.columns(2)
    for i, (emoji, recommendation) in enumerate(recommendations):
        with rec_cols[i % 2]:
            st.markdown(
                f'<div class="soft-card" style="margin-bottom:12px;">'
                f'<div style="font-size:1.35rem;margin-bottom:8px;">{emoji}</div>'
                f'<div style="color:#dce5f8;line-height:1.6;">{recommendation}</div></div>',
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)
    st.success("Your study plan is ready. Keep going, one session at a time!")
else:
    st.markdown(
        """
        <div class="soft-card">
            <div class="section-kicker">Your plan starts here</div>
            <h3 style="margin-top:6px;">A little progress every day adds up.</h3>
            <p>Complete the form and choose a subject. The general timetable works by default; select topic-wise mode only if you want to enter topics manually.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="footer">Study Buddy · AI Smart Study Planner · Prototype for educational use</div>',
    unsafe_allow_html=True,
)
