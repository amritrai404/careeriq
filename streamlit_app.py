"""
CareerIQ - Streamlit Frontend
-----------------------------
AI Career Intelligence Platform.
Upload a resume PDF + paste a job description,
and CareerIQ will analyze skill alignment.
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


# ---------------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------------
st.set_page_config(
    page_title="CareerIQ",
    page_icon="🚀",
    layout="wide"
)


# ---------------------------------------------------------------
# Header
# ---------------------------------------------------------------
st.title("🚀 CareerIQ")
st.subheader("AI Career Intelligence Platform")

st.write(
    "Analyze your resume against a job description "
    "and discover your career skill gaps."
)


# ---------------------------------------------------------------
# Inputs
# ---------------------------------------------------------------
st.header("📄 Upload your Resume")

resume = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"],
    help="Upload your resume in PDF format."
)

st.header("💼 Job Description")

job_description = st.text_area(
    "Paste Job Description",
    height=250,
    placeholder="Paste the job description here..."
)


# ---------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------
if st.button("🚀 Analyze My Career"):

    if resume is None:
        st.warning("⚠️ Please upload your resume first.")

    elif not job_description.strip():
        st.warning("⚠️ Please enter a job description.")

    else:
        try:
            # ----- Extract resume text -----
            resume.seek(0)
            resume_text = extract_text_from_pdf(resume)

            if not resume_text:
                st.error(
                    "❌ Could not extract text from this PDF. "
                    "Please upload a text-based PDF resume."
                )

            else:
                # ----- Extract skills -----
                resume_skills = extract_skills(resume_text)
                jd_skills = extract_skills(job_description)

                # ----- Match skills -----
                result = match_skills(resume_skills, jd_skills)

                # ----- Categorize missing skills -----
                gap = categorize_missing_skills(
                    result["missing"], job_description
                )

                st.success("✅ Analysis complete!")

                # =================================================
                # Match Score (Hero metric)
                # =================================================
                st.header("🎯 Career Match Score")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        label="Match Score",
                        value=f"{result['match_score']}%"
                    )

                with col2:
                    st.metric(
                        label="Matched Skills",
                        value=result["total_matched"]
                    )

                with col3:
                    st.metric(
                        label="Required Skills",
                        value=result["total_required"]
                    )

                st.progress(min(int(result["match_score"]), 100) / 100)
                st.write(f"**Status:** {result['status']}")

                st.divider()

                # =================================================
                # Matched vs Missing Skills
                # =================================================
                col_left, col_right = st.columns(2)

                with col_left:
                    st.subheader("✅ Matched Skills")
                    if result["matched"]:
                        for skill in result["matched"]:
                            st.write(f"✓ {skill}")
                    else:
                        st.info("No matched skills found.")

                with col_right:
                    st.subheader("❌ Missing Skills")
                    if result["missing"]:
                        for skill in result["missing"]:
                            st.write(f"✗ {skill}")
                    else:
                        st.success("No missing skills. Great match! 🎉")

                st.divider()

                # =================================================
                # Skill Gap Priority
                # =================================================
                if result["missing"]:
                    st.subheader("🎯 Skill Gap Priority")

                    gap_col1, gap_col2, gap_col3 = st.columns(3)

                    with gap_col1:
                        st.markdown("**🔴 Critical**")
                        if gap["critical"]:
                            for skill in gap["critical"]:
                                st.write(f"• {skill}")
                        else:
                            st.write("_None_")

                    with gap_col2:
                        st.markdown("**🟡 Important**")
                        if gap["important"]:
                            for skill in gap["important"]:
                                st.write(f"• {skill}")
                        else:
                            st.write("_None_")

                    with gap_col3:
                        st.markdown("**🟢 Nice to Have**")
                        if gap["nice_to_have"]:
                            for skill in gap["nice_to_have"]:
                                st.write(f"• {skill}")
                        else:
                            st.write("_None_")

                # =================================================
                # Visual Analytics
                # =================================================
                st.divider()
                st.subheader("📊 Visual Analytics")

                viz_col1, viz_col2 = st.columns(2)

                with viz_col1:
                    fig1 = plot_matched_vs_missing(
                        result["matched"], result["missing"]
                    )
                    st.pyplot(fig1, use_container_width=True)

                with viz_col2:
                    coverage = compute_category_coverage(
                        resume_skills, jd_skills
                    )
                    fig2 = plot_category_coverage(coverage)
                    if fig2 is not None:
                        st.pyplot(fig2, use_container_width=True)
                    else:
                        st.info("No category data to visualize.")

                st.divider()

                # =================================================
                # Extracted Skills (for transparency)
                # =================================================
                with st.expander("🔍 View Extracted Skills"):
                    st.write("**Resume Skills:**")
                    if resume_skills:
                        st.write(", ".join(resume_skills))
                    else:
                        st.write("_No skills detected in resume._")

                    st.write("**Job Description Skills:**")
                    if jd_skills:
                        st.write(", ".join(jd_skills))
                    else:
                        st.write("_No skills detected in job description._")

                    if result["extra"]:
                        st.write(
                            "**Extra Skills (in resume but not required):**"
                        )
                        st.write(", ".join(result["extra"]))

                # =================================================
                # Career Recommendations
                # =================================================
                if result["missing"]:
                    st.divider()
                    st.subheader("📚 Career Recommendations")

                    rec_tab1, rec_tab2, rec_tab3 = st.tabs([
                        "🎓 Learning Path",
                        "🛠️ Project Ideas",
                        "📄 Resume Tips",
                    ])

                    with rec_tab1:
                        suggestions = get_learning_suggestions(
                            result["missing"]
                        )
                        for item in suggestions:
                            st.markdown(
                                f"**{item['skill']}** "
                                f"_({item['category']})_"
                            )
                            st.write(f"→ {item['suggestion']}")

                    with rec_tab2:
                        ideas = get_project_ideas(result["missing"])
                        if ideas:
                            for idea in ideas:
                                st.write(f"• {idea}")
                        else:
                            st.write("_No project ideas available._")

                    with rec_tab3:
                        tips = get_resume_tips(result["missing"])
                        for tip in tips:
                            st.write(f"• {tip}")
                else:
                    st.success(
                        "🎉 Your resume already covers all required skills!"
                    )

        except Exception as e:
            st.error(f"❌ Error processing resume: {e}")