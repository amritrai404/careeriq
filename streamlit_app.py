"""
CareerIQ - Streamlit Frontend
-----------------------------
AI Career Intelligence Platform.
Upload a resume PDF + paste a job description,
and CareerIQ will analyze skill alignment with ML-powered insights.
"""

import streamlit as st

from app.resume_parser import extract_text_from_pdf
from app.skill_extractor import extract_skills
from app.skill_matcher import match_skills
from app.skill_gap import categorize_missing_skills
from app.recommendations import (
    get_learning_suggestions,
    get_project_ideas,
    get_resume_tips,
)
from app.visualizations import (
    plot_matched_vs_missing,
    compute_category_coverage,
    plot_category_coverage,
)
from app.role_predictor import (
    predict_roles,
    is_model_available as role_model_ok,
)
from app.quality_scorer import (
    predict_quality,
    is_model_available as quality_model_ok,
)
from app.profile_matcher import (
    find_similar_profiles,
    is_model_available as profiles_model_ok,
)


# ---------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------
st.set_page_config(
    page_title="CareerIQ",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------------
st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1250px;
    }
    .hero-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2.2rem 2rem;
        border-radius: 18px;
        color: white;
        text-align: center;
        box-shadow: 0 6px 24px rgba(102, 126, 234, 0.25);
        margin-bottom: 1.5rem;
    }
    .hero-card .label {
        font-size: 0.85rem;
        letter-spacing: 2px;
        opacity: 0.85;
        margin: 0;
        font-weight: 600;
    }
    .hero-card h1 {
        font-size: 4rem;
        margin: 0.3rem 0;
        font-weight: 800;
        letter-spacing: -2px;
        line-height: 1;
    }
    .hero-card .badge {
        display: inline-block;
        padding: 0.45rem 1.1rem;
        background: rgba(255, 255, 255, 0.22);
        border-radius: 100px;
        margin-top: 0.8rem;
        font-weight: 600;
        font-size: 0.95rem;
    }
    .skill-chip {
        display: inline-block;
        padding: 0.35rem 0.85rem;
        border-radius: 100px;
        font-size: 0.85rem;
        font-weight: 500;
        margin: 0.2rem 0.25rem 0.2rem 0;
        border: 1px solid;
    }
    .chip-matched  { background:#e8f5e9; color:#2e7d32; border-color:#a5d6a7; }
    .chip-missing  { background:#ffebee; color:#c62828; border-color:#ef9a9a; }
    .chip-extra    { background:#e3f2fd; color:#1565c0; border-color:#90caf9; }
    .chip-critical { background:#ffebee; color:#b71c1c; border-color:#e57373; }
    .chip-important{ background:#fff8e1; color:#f57f17; border-color:#ffcc80; }
    .chip-nice     { background:#e8f5e9; color:#2e7d32; border-color:#a5d6a7; }
    div[data-testid="stMetric"] {
        background:#f8f9fa; padding:1rem 1.2rem;
        border-radius:12px; border:1px solid #e9ecef;
    }
    section[data-testid="stSidebar"] { background:#f8f9fa; }
    h2, h3 { margin-top: 0.6rem !important; }
    </style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------------
# Helper
# ---------------------------------------------------------------
def render_chips(skills, chip_class):
    if not skills:
        return "<em style='color:#999;'>None</em>"
    return "".join(
        f'<span class="skill-chip {chip_class}">{s}</span>' for s in skills
    )


# ---------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------
with st.sidebar:
    st.title("💼 CareerIQ")
    st.caption("AI Career Intelligence Platform")
    st.divider()

    st.subheader("📥 Input")

    resume = st.file_uploader(
        "📄 Upload Resume (PDF)",
        type=["pdf"],
        help="Upload your resume in PDF format."
    )
    job_description = st.text_area(
        "💼 Paste Job Description",
        height=220,
        placeholder="Paste the job description here..."
    )

    analyze_clicked = st.button(
        "Analyze My Career",
        use_container_width=True,
        type="primary"
    )

    st.divider()
    st.caption(
        "💡 **Tip:** Paste the full job description "
        "including requirements for best results."
    )


# ---------------------------------------------------------------
# Header
# ---------------------------------------------------------------
st.title("💼 CareerIQ")
st.write(
    "Analyze your resume against a job description "
    "and discover your career skill gaps."
)


# ---------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------
if analyze_clicked:

    if resume is None:
        st.warning("⚠️ Please upload your resume first.")
    elif not job_description.strip():
        st.warning("⚠️ Please enter a job description.")
    else:
        try:
            with st.spinner("🔍 Analyzing your resume..."):
                resume.seek(0)
                resume_text = extract_text_from_pdf(resume)

                if not resume_text:
                    st.error("❌ Could not extract text from this PDF.")
                    st.stop()

                resume_skills = extract_skills(resume_text)
                jd_skills = extract_skills(job_description)
                result = match_skills(resume_skills, jd_skills)
                gap = categorize_missing_skills(
                    result["missing"], job_description
                )

                # ML: Role Prediction
                predicted_roles = []
                if role_model_ok():
                    predicted_roles = predict_roles(resume_text, top_n=3)

                # ML: Quality Score
                quality = {"score": 0.0, "features": {}}
                if quality_model_ok():
                    quality = predict_quality(resume_text)

                # ML: Similar Profiles
                similar_profiles = []
                if profiles_model_ok():
                    similar_profiles = find_similar_profiles(
                        resume_text, top_n=5
                    )

            # =================================================
            # Hero Score
            # =================================================
            score = result["match_score"]
            st.markdown(f"""
                <div class="hero-card">
                    <p class="label">🎯 CAREER MATCH SCORE</p>
                    <h1>{score}%</h1>
                    <div class="badge">{result['status']}</div>
                </div>
            """, unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("✅ Matched Skills", result["total_matched"])
            with col2:
                st.metric("❌ Missing Skills", len(result["missing"]))
            with col3:
                st.metric("📋 Required Skills", result["total_required"])

            # =================================================
            # ML Insights
            # =================================================
            st.divider()
            st.subheader("🤖 AI-Powered Insights")

            ml_col1, ml_col2 = st.columns(2)

            with ml_col1:
                st.markdown("**🎯 Predicted Career Roles**")
                if predicted_roles:
                    for r in predicted_roles:
                        st.write(f"• {r['role']} — **{r['confidence']}%**")
                else:
                    st.info("Model not available.")

            with ml_col2:
                st.markdown("**📊 Resume Quality Score**")
                if quality["score"] > 0:
                    st.metric("Quality", f"{quality['score']}/100")
                else:
                    st.info("Model not available.")

            # =================================================
            # Matched vs Missing
            # =================================================
            st.divider()
            col_left, col_right = st.columns(2)

            with col_left:
                st.subheader("✅ Matched Skills")
                st.markdown(
                    render_chips(result["matched"], "chip-matched"),
                    unsafe_allow_html=True
                )
            with col_right:
                st.subheader("❌ Missing Skills")
                st.markdown(
                    render_chips(result["missing"], "chip-missing"),
                    unsafe_allow_html=True
                )

            # =================================================
            # Skill Gap Priority
            # =================================================
            if result["missing"]:
                st.divider()
                st.subheader("🎯 Skill Gap Priority")

                g1, g2, g3 = st.columns(3)
                with g1:
                    st.markdown("**🔴 Critical**")
                    st.markdown(
                        render_chips(gap["critical"], "chip-critical"),
                        unsafe_allow_html=True
                    )
                with g2:
                    st.markdown("**🟡 Important**")
                    st.markdown(
                        render_chips(gap["important"], "chip-important"),
                        unsafe_allow_html=True
                    )
                with g3:
                    st.markdown("**🟢 Nice to Have**")
                    st.markdown(
                        render_chips(gap["nice_to_have"], "chip-nice"),
                        unsafe_allow_html=True
                    )

            # =================================================
            # Visual Analytics
            # =================================================
            st.divider()
            st.subheader("📊 Visual Analytics")

            viz1, viz2 = st.columns(2)
            with viz1:
                fig1 = plot_matched_vs_missing(
                    result["matched"], result["missing"]
                )
                st.pyplot(fig1, use_container_width=True)
            with viz2:
                coverage = compute_category_coverage(
                    resume_skills, jd_skills
                )
                fig2 = plot_category_coverage(coverage)
                if fig2 is not None:
                    st.pyplot(fig2, use_container_width=True)
                else:
                    st.info("No category data to visualize.")

            # =================================================
            # Similar Profiles (ML)
            # =================================================
            st.divider()
            with st.expander("👥 Similar Profiles (ML)"):
                if similar_profiles:
                    st.caption(
                        "Top 5 most similar resumes from our dataset "
                        "(based on TF-IDF similarity)."
                    )
                    for i, p in enumerate(similar_profiles, 1):
                        st.write(
                            f"{i}. **{p['category']}** — "
                            f"Similarity: {p['similarity']}%"
                        )
                else:
                    st.info(
                        "Similar profiles feature is available in "
                        "local deployment only. It requires the full "
                        "resume dataset (56 MB), which is not pushed "
                        "to GitHub to keep the repository lightweight."
                    )

            # =================================================
            # Extracted Skills
            # =================================================
            with st.expander("🔍 View Extracted Skills"):
                st.write("**Resume Skills:**")
                st.markdown(
                    render_chips(resume_skills, "chip-extra"),
                    unsafe_allow_html=True
                )
                st.write("**Job Description Skills:**")
                st.markdown(
                    render_chips(jd_skills, "chip-extra"),
                    unsafe_allow_html=True
                )

            # =================================================
            # Recommendations
            # =================================================
            if result["missing"]:
                st.divider()
                st.subheader("📚 Career Recommendations")

                t1, t2, t3 = st.tabs([
                    "🎓 Learning Path",
                    "🛠️ Project Ideas",
                    "📄 Resume Tips",
                ])

                with t1:
                    for item in get_learning_suggestions(result["missing"]):
                        st.markdown(
                            f"**{item['skill']}** _({item['category']})_"
                        )
                        st.write(f"→ {item['suggestion']}")

                with t2:
                    ideas = get_project_ideas(result["missing"])
                    if ideas:
                        for idea in ideas:
                            st.write(f"• {idea}")
                    else:
                        st.write("_No project ideas available._")

                with t3:
                    for tip in get_resume_tips(result["missing"]):
                        st.write(f"• {tip}")
            else:
                st.success(
                    "🎉 Your resume already covers all required skills!"
                )

        except Exception as e:
            st.error(f"❌ Error processing resume: {e}")


# ---------------------------------------------------------------
# Footer
# ---------------------------------------------------------------
st.divider()
st.caption(
    "Built by [Amrit Rai](https://github.com/amritrai404) · "
    "CareerIQ is a learning tool and not a substitute for "
    "professional career advice."
)