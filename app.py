from dotenv import load_dotenv
load_dotenv()  # BUG FIX: Must be called before any other import that uses env vars

import streamlit as st

from agents.classifier import ClassifierAgent
from agents.brute_force import BruteForceAgent
from agents.optimal import OptimalAgent
from agents.complexity import ComplexityAgent
from agents.translator import TranslatorAgent
from agents.reviewer import ReviewerAgent
from database.db import DatabaseManager

from utils.helpers import (
    SUPPORTED_LANGUAGES,
    generate_filename
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="DSA Solver AI",
    page_icon="🚀",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>
.block-container{
    padding-top:1rem;
    max-width:1400px;
}
.hero{
    text-align:center;
    padding:30px;
    border-radius:20px;
    background:linear-gradient(135deg,#0f172a,#1e293b);
    margin-bottom:20px;
}
.hero h1{ color:white; font-size:3rem; margin-bottom:10px; }
.hero p{ color:#cbd5e1; font-size:1.1rem; }
</style>
""", unsafe_allow_html=True)

# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown("""
<div class="hero">
    <h1>🚀 DSA Solver AI</h1>
    <p>Brute Force • Optimal Solution • Complexity Analysis • Code Translation</p>
</div>
""", unsafe_allow_html=True)

# ==========================================================
# INPUT SECTION
# ==========================================================

left, right = st.columns([4, 1])

with left:
    problem = st.text_area(
        "Enter DSA Problem",
        height=250,
        placeholder="""
Example:

Given an array nums and an integer target,
return indices of the two numbers such that
they add up to target.
"""
    )

with right:
    language = st.selectbox(
        "Programming Language",
        SUPPORTED_LANGUAGES
    )

    solve_btn = st.button(
        "🚀 Solve Problem",
        use_container_width=True
    )

# ==========================================================
# SOLVER
# ==========================================================

if solve_btn:

    if not problem.strip():
        st.warning("Please enter a DSA problem.")

    else:

        try:

            with st.spinner("Analyzing problem..."):

                classification = ClassifierAgent.classify(problem)
                brute = BruteForceAgent.generate(problem, language)
                optimal = OptimalAgent.generate(problem, language)
                complexity = ComplexityAgent.analyze(problem, optimal["code"])
                review = ReviewerAgent.review(problem, optimal["code"])

                # BUG FIX: Save to database after solving
                # (was missing entirely in original app.py)
                try:
                    db = DatabaseManager()
                    db.save_solution(
                        problem_statement=problem,
                        language=language,
                        topic=classification.get("topic", ""),
                        pattern=classification.get("pattern", ""),
                        difficulty=classification.get("difficulty", ""),
                        time_complexity=complexity.get("time_complexity", ""),
                        space_complexity=complexity.get("space_complexity", ""),
                        brute_force_code=brute.get("code", ""),
                        optimal_code=optimal.get("code", ""),
                        interview_optimal=optimal.get("interview_optimal", ""),
                        theoretical_optimal=optimal.get("theoretical_optimal", "")
                    )
                except Exception as db_err:
                    st.warning(f"Could not save to history: {db_err}")

            st.success("Solution Generated Successfully!")

            # ======================================
            # PROBLEM ANALYSIS
            # ======================================

            st.subheader("📊 Problem Analysis")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric("Topic", classification.get("topic", "Unknown"))
            with c2:
                st.metric("Pattern", classification.get("pattern", "Unknown"))
            with c3:
                st.metric("Difficulty", classification.get("difficulty", "Unknown"))

            st.divider()

            # ======================================
            # ALGORITHM SELECTION
            # ======================================

            st.subheader("🏆 Algorithm Selection")

            c1, c2 = st.columns(2)

            with c1:
                st.metric("Interview Optimal", optimal.get("interview_optimal", "Unknown"))
            with c2:
                st.metric("Theoretical Optimal", optimal.get("theoretical_optimal", "Unknown"))

            st.divider()

            # ======================================
            # COMPLEXITY
            # ======================================

            st.subheader("⚡ Complexity Analysis")

            c1, c2 = st.columns(2)

            with c1:
                st.metric("Time Complexity", complexity.get("time_complexity", "Unknown"))
            with c2:
                st.metric("Space Complexity", complexity.get("space_complexity", "Unknown"))

            st.divider()

            # ======================================
            # REVIEW
            # ======================================

            st.subheader("🔍 Solution Review")

            st.info(f"Optimal: {review.get('is_optimal', 'Unknown')}")

            st.write(f"**Better Algorithm:** {review.get('better_algorithm', 'None')}")

            st.write(review.get("reason", "No review available."))

            st.divider()

            # ======================================
            # TABS
            # ======================================

            tab1, tab2, tab3 = st.tabs([
                "🔥 Brute Force",
                "🚀 Optimal",
                "🌍 Translate"
            ])

            with tab1:

                st.code(brute["code"], language.lower())

                st.download_button(
                    label="⬇ Download Brute Force",
                    data=brute["code"],
                    file_name=generate_filename(language, "brute_force")
                )

                st.markdown("### Explanation")
                st.write(brute["explanation"])

            with tab2:

                st.code(optimal["code"], language.lower())

                st.download_button(
                    label="⬇ Download Optimal",
                    data=optimal["code"],
                    file_name=generate_filename(language, "optimal")
                )

                st.markdown("### Explanation")
                st.write(optimal["explanation"])

            with tab3:

                target_language = st.selectbox(
                    "Translate To",
                    [lang for lang in SUPPORTED_LANGUAGES if lang != language]
                )

                if st.button("Translate Code"):

                    translated = TranslatorAgent.translate(
                        optimal["code"],
                        target_language
                    )

                    # BUG FIX: Check success flag before displaying,
                    # show error message if translation failed
                    if translated.get("success"):
                        st.code(
                            translated["translated_code"],
                            target_language.lower()
                        )
                    else:
                        st.error(
                            f"Translation failed: {translated.get('error', 'Unknown error')}"
                        )

        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.exception(e)  # BUG FIX: Show full traceback in dev mode for easier debugging
