import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime, date, time, timedelta

st.set_page_config(
    page_title="ZAPPYBOO | AI Study Planner",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)
# ---------- ZAPPYBOO PREMIUM HEADER ----------
import streamlit as st

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(ellipse at 50% 8%,
            rgba(0, 145, 255, 0.20), transparent 42%),
        radial-gradient(ellipse at 15% 35%,
            rgba(112, 65, 220, 0.12), transparent 45%),
        linear-gradient(145deg, #080c18, #101a30 55%, #080c18);
    color: #f5f7ff;
}

/* Hide top toolbar */
[data-testid="stToolbar"] {
    visibility: hidden;
}

/* Center logo */
.zappy-logo {
    text-align: center;
    padding: 12px 0 0;
}

/* Hero card */
.zappy-hero {
    max-width: 900px;
    margin: 8px auto 28px;
    padding: 28px 24px;
    border: 1px solid rgba(155, 140, 255, 0.30);
    border-radius: 24px;
    background: linear-gradient(
        120deg,
        rgba(55, 43, 105, 0.42),
        rgba(12, 42, 64, 0.48)
    );
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.18);
}

.zappy-kicker {
    color: #b9a7ff;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 20px;
}

.zappy-title {
    color: #f7f8ff;
    font-size: clamp(34px, 6vw, 54px);
    line-height: 1.12;
    font-weight: 850;
    letter-spacing: -1.5px;
    margin: 0 0 18px;
}

.zappy-description {
    color: #c1cbe0;
    font-size: clamp(16px, 2.5vw, 20px);
    line-height: 1.8;
    margin: 0;
}

/* Form container */
div[data-testid="stForm"] {
    border: 1px solid rgba(145, 160, 200, 0.28);
    border-radius: 18px;
    padding: 22px;
    background: rgba(10, 16, 32, 0.55);
}

/* Buttons */
div.stButton > button,
div.stFormSubmitButton > button {
    background: linear-gradient(100deg, #6555f5, #168de0);
    color: white;
    border: none;
    border-radius: 12px;
    min-height: 46px;
    font-weight: 750;
}

div.stButton > button:hover,
div.stFormSubmitButton > button:hover {
    box-shadow: 0 0 22px rgba(70, 140, 255, 0.35);
    border: none;
}

/* Mobile layout */
@media (max-width: 600px) {
    .zappy-hero {
        padding: 22px 18px;
        border-radius: 20px;
    }

    .zappy-kicker {
        font-size: 10px;
        letter-spacing: 2px;
    }
}
</style>
""", unsafe_allow_html=True)

# Centered logo
left, center, right = st.columns([1, 2, 1])

with center:
    st.markdown(
        '<div class="zappy-logo"></div>',
        unsafe_allow_html=True
    )
    st.image("zappyboo_logo (2).png", width=220)

# Hero section
st.markdown(
    """
    <div style="text-align:center; padding:24px;">
        <h1>Study smarter.<br>Feel more prepared.</h1>
        <p>
            Choose a subject and get a general timetable by default,
            or optionally enter topics for a day-by-day topic-wise plan.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
    [data-testid="stToolbar"] {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
    #GithubIcon {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
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
    st.markdown("## ⚡ZAPPYBOO💡")
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
    # ---------- Smart Study Calendar ----------
st.markdown("---")
st.markdown("## 📅 ZAPPYBOO Smart Study Calendar")
st.write("Plan your subjects and daily study sessions.")

from datetime import date, timedelta

today = date.today()

calendar_days = st.number_input(
    "How many days do you want to plan?",
    min_value=1,
    max_value=30,
    value=7,
    key="calendar_days"
)

calendar_subjects = st.text_input(
    "Enter subjects (comma-separated)",
    "Operating Systems, Mathematics, Python",
    key="calendar_subjects"
)

if st.button("✨ Create Study Calendar", key="create_calendar"):
    subject_list_calendar = [
        s.strip()
        for s in calendar_subjects.split(",")
        if s.strip()
    ]

    if not subject_list_calendar:
        st.warning("Bro, at least one subject enter pannu!")
    else:
        calendar_rows = []

        for day_num in range(int(calendar_days)):
            study_date = today + timedelta(days=day_num)
            subject = subject_list_calendar[
                day_num % len(subject_list_calendar)
            ]

            calendar_rows.append({
                "Date": study_date.strftime("%d-%m-%Y"),
                "Day": study_date.strftime("%A"),
                "Subject": subject,
                "Task": "Study + Practice Questions",
                "Completed": False
            })

        st.session_state["study_calendar"] = pd.DataFrame(
            calendar_rows
        )

if "study_calendar" in st.session_state:
    edited_calendar = st.data_editor(
        st.session_state["study_calendar"],
        use_container_width=True,
        hide_index=True,
        disabled=["Date", "Day", "Subject", "Task"],
        key="calendar_editor"
    )

    st.session_state["study_calendar"] = edited_calendar

    completed_days = int(
        edited_calendar["Completed"].sum()
    )
    total_days = len(edited_calendar)

    st.progress(completed_days / total_days)
    st.write(
        f"📈 Calendar progress: {completed_days}/{total_days} days completed"
    )

    st.download_button(
        "⬇️ Download Study Calendar",
        data=edited_calendar.to_csv(index=False).encode("utf-8"),
        file_name="zappyboo_study_calendar.csv",
        mime="text/csv",
        key="download_calendar"
    )
    st.markdown("---")
    # ---------- ZAPPYBOO Exam Countdown Timetable ----------
from datetime import datetime, date, time, timedelta

st.markdown("---")
st.markdown("## ⚡ ZAPPYBOO Exam Countdown Planner")
st.write(
    "Enter your exam details to create a revision schedule "
    "with focused study sessions and breaks."
)

with st.container(border=True):
    exam_subject = st.text_input(
        "📘 Exam subject",
        placeholder="e.g. Operating Systems",
        key="countdown_subject",
    )

    exam_topics_text = st.text_area(
        "📝 Topics to revise (one topic per line)",
        placeholder="Process Management\nCPU Scheduling\nDeadlocks",
        key="countdown_topics",
    )

    exam_date = st.date_input(
        "📅 Exam date",
        value=date.today() + timedelta(days=1),
        min_value=date.today(),
        key="countdown_date",
    )

    exam_time = st.time_input(
        "⏰ Exam start time",
        value=time(9, 0),
        key="countdown_time",
    )

    available_hours = st.number_input(
        "⌛ Study hours available per day",
        min_value=1,
        max_value=16,
        value=6,
        key="countdown_hours",
    )

    start_time = st.time_input(
        "🌅 Daily study start time",
        value=time(9, 0),
        key="countdown_start_time",
    )

    if st.button(
        "🚀 Generate Countdown Timetable",
        use_container_width=True,
        key="generate_countdown",
    ):
        topics = [
            topic.strip()
            for topic in exam_topics_text.splitlines()
            if topic.strip()
        ]

        now = datetime.now()
        exam_datetime = datetime.combine(exam_date, exam_time)
        study_start = datetime.combine(date.today(), start_time)

        if not exam_subject.strip():
            st.warning("Bro, exam subject enter pannu.")
        elif not topics:
            st.warning("Bro, at least one topic enter pannu.")
        elif exam_datetime <= now:
            st.warning("Exam date and time future-la irukkanum bro.")
        elif exam_date == date.today() and study_start <= now:
            st.warning(
                "Innaikku study start time past-la irukku. "
                "Future time select pannu bro."
            )
        else:
            st.session_state["countdown_plan_data"] = {
                "subject": exam_subject.strip(),
                "topics": topics,
                "exam_datetime": exam_datetime,
                "available_hours": int(available_hours),
                "start_time": start_time,
            }

if "countdown_plan_data" in st.session_state:
    plan = st.session_state["countdown_plan_data"]
    now = datetime.now()
    exam_datetime = plan["exam_datetime"]
    remaining = exam_datetime - now

    if remaining.total_seconds() > 0:
        total_hours_left = remaining.total_seconds() / 3600

        st.success(
            f"⏳ Exam in approximately {total_hours_left:.1f} hours"
        )

        st.caption(
            f"Subject: {plan['subject']} · "
            f"Exam: {exam_datetime.strftime('%d-%m-%Y %I:%M %p')}"
        )

        # Make a schedule for each available day.
        schedule_rows = []
        topics = plan["topics"]
        hours_per_day = plan["available_hours"]
        current_day = date.today()
        final_study_day = exam_datetime.date()

        while current_day <= final_study_day:
            day_start = datetime.combine(
                current_day, plan["start_time"]
            )
            day_end = datetime.combine(
                current_day, time(21, 0)
            )

            if current_day == date.today():
                day_start = max(day_start, now + timedelta(minutes=5))

            if current_day == final_study_day:
                day_end = min(
                    day_end,
                    exam_datetime - timedelta(minutes=60)
                )

            available_minutes = max(
                0, int((day_end - day_start).total_seconds() // 60)
            )
            target_minutes = min(
                hours_per_day * 60, available_minutes
            )

            # 50-minute study sessions with 10-minute breaks.
            session_count = target_minutes // 60
            leftover_minutes = target_minutes % 60

            day_topic_index = (
                (current_day - date.today()).days * max(1, session_count)
            ) % len(topics)

            cursor = day_start
            minutes_used = 0
            session_number = 0

            while (
                minutes_used < target_minutes
                and cursor < day_end
            ):
                study_minutes = min(
                    50,
                    target_minutes - minutes_used,
                    int((day_end - cursor).total_seconds() // 60),
                )

                if study_minutes <= 0:
                    break

                topic = topics[
                    (day_topic_index + session_number) % len(topics)
                ]

                session_end = cursor + timedelta(minutes=study_minutes)

                schedule_rows.append({
                    "Date": current_day.strftime("%d-%m-%Y"),
                    "Time": (
                        f"{cursor.strftime('%I:%M %p')} - "
                        f"{session_end.strftime('%I:%M %p')}"
                    ),
                    "Session": f"Study: {topic}",
                    "Duration": f"{study_minutes} min",
                })

                cursor = session_end
                minutes_used += study_minutes
                session_number += 1

                if minutes_used < target_minutes and cursor < day_end:
                    break_minutes = min(
                        10,
                        target_minutes - minutes_used,
                        int((day_end - cursor).total_seconds() // 60),
                    )

                    if break_minutes > 0:
                        break_end = cursor + timedelta(
                            minutes=break_minutes
                        )

                        schedule_rows.append({
                            "Date": current_day.strftime("%d-%m-%Y"),
                            "Time": (
                                f"{cursor.strftime('%I:%M %p')} - "
                                f"{break_end.strftime('%I:%M %p')}"
                            ),
                            "Session": "☕ Short break",
                            "Duration": f"{break_minutes} min",
                        })

                        cursor = break_end
                        minutes_used += break_minutes

            current_day += timedelta(days=1)

        if schedule_rows:
            countdown_df = pd.DataFrame(schedule_rows)
            st.markdown("### 📚 Your revision sessions")
            st.dataframe(
                countdown_df,
                use_container_width=True,
                hide_index=True,
            )

            st.download_button(
                "⬇️ Download revision timetable (CSV)",
                data=countdown_df.to_csv(index=False).encode("utf-8"),
                file_name="zappyboo_exam_countdown.csv",
                mime="text/csv",
                key="download_countdown",
            )
        else:
            st.warning(
                "Exam-ku munnadi schedule create panna time illa. "
                "Available time check pannu bro."
            )
    else:
        st.warning("Exam time vandhuduchu. New exam details enter pannu.")

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
    '<div class="footer">ZAPPYBOO💡 · AI Smart Study Planner · Prototype for educational use</div>',
    unsafe_allow_html=True,
)
def render_multi_subject_calendar():
    import streamlit as st
    import pandas as pd
    from datetime import datetime, date, time, timedelta

    st.subheader("⚡ Smart Study Calendar")
    st.write(
        "Plan Operating Systems, Python Programming, "
        "and Mathematics in one combined timetable."
    )

    subjects = [
        "Operating Systems",
        "Python Programming",
        "Mathematics",
    ]

    with st.form("multi_subject_calendar_form"):
        plans = []

        for i, subject in enumerate(subjects):
            st.markdown(f"### 📘 {subject}")

            topics_text = st.text_area(
                f"Enter {subject} topics (one topic per line)",
                key=f"calendar_topics_{i}",
                placeholder="Topic 1\nTopic 2\nTopic 3",
            )

            exam_date = st.date_input(
                f"{subject} exam date",
                value=date.today() + timedelta(days=1),
                min_value=date.today(),
                key=f"calendar_date_{i}",
            )

            exam_time = st.time_input(
                f"{subject} exam time",
                value=time(9, 0),
                key=f"calendar_time_{i}",
            )

            hours_per_day = st.number_input(
                f"Available study hours per day for {subject}",
                min_value=1,
                max_value=12,
                value=2,
                key=f"calendar_hours_{i}",
            )

            plans.append({
                "subject": subject,
                "topics": topics_text,
                "exam_date": exam_date,
                "exam_time": exam_time,
                "hours": int(hours_per_day),
            })

        study_start = st.time_input(
            "Daily study start time",
            value=time(17, 0),
            key="calendar_start_time",
        )

        session_minutes = st.selectbox(
            "Study duration per topic",
            [25, 30, 45, 60],
            index=2,
            key="calendar_session_minutes",
        )

        break_minutes = st.selectbox(
            "Break after each study session",
            [5, 10, 15],
            index=1,
            key="calendar_break_minutes",
        )

        submitted = st.form_submit_button(
            "✨ Generate Combined Timetable",
            use_container_width=True,
        )

    if submitted:
        now = datetime.now()
        errors = []
        pending = []

        for plan in plans:
            topic_list = [
                topic.strip()
                for topic in plan["topics"].splitlines()
                if topic.strip()
            ]

            exam_dt = datetime.combine(
                plan["exam_date"], plan["exam_time"]
            )

            if not topic_list:
                errors.append(
                    f"{plan['subject']}: Enter at least one topic."
                )

            if exam_dt <= now:
                errors.append(
                    f"{plan['subject']}: Choose a future exam date and time."
                )

            plan["topic_list"] = topic_list
            plan["exam_dt"] = exam_dt

            for topic in topic_list:
                pending.append({
                    "subject": plan["subject"],
                    "topic": topic,
                    "exam_dt": exam_dt,
                    "hours": plan["hours"],
                })

        if errors:
            for error in errors:
                st.error(error)
        else:
            pending.sort(key=lambda item: item["exam_dt"])
            sessions = []
            cursor = datetime.combine(now.date(), study_start)

            if cursor < now:
                cursor = now + timedelta(minutes=5)

            for item in pending:
                candidate = cursor
                slot_found = False

                while candidate < item["exam_dt"]:
                    day_start = datetime.combine(
                        candidate.date(), study_start
                    )
                    day_end = day_start + timedelta(
                        hours=item["hours"]
                    )

                    if candidate < day_start:
                        candidate = day_start

                    session_end = candidate + timedelta(
                        minutes=session_minutes
                    )

                    if (
                        candidate >= day_start
                        and session_end <= day_end
                        and session_end < item["exam_dt"]
                    ):
                        sessions.append({
                            "_sort": candidate,
                            "Date": candidate.strftime("%d-%m-%Y"),
                            "Start": candidate.strftime("%I:%M %p"),
                            "End": session_end.strftime("%I:%M %p"),
                            "Subject": item["subject"],
                            "Topic": item["topic"],
                            "Break (minutes)": break_minutes,
                        })

                        cursor = session_end + timedelta(
                            minutes=break_minutes
                        )
                        slot_found = True
                        break

                    candidate = day_start + timedelta(days=1)
                    cursor = candidate

                if not slot_found:
                    st.warning(
                        f"Could not schedule: {item['subject']} — "
                        f"{item['topic']}. Try more study hours or an "
                        "earlier start time."
                    )

            if sessions:
                result = pd.DataFrame(sessions)
                result = result.sort_values("_sort").drop(
                    columns=["_sort"]
                )

                st.success("Your combined timetable is ready!")
                st.dataframe(
                    result,
                    use_container_width=True,
                    hide_index=True,
                )

                st.download_button(
                    "⬇️ Download Combined Timetable (CSV)",
                    data=result.to_csv(index=False).encode("utf-8"),
                    file_name="zappyboo_combined_timetable.csv",
                    mime="text/csv",
                )
            else:
                st.error(
                    "No sessions could be scheduled. "
                    "Please adjust your study settings."
                )
                render_multi_subject_calendar()
