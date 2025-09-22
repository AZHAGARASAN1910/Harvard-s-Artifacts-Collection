import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# -----------------------------
# MySQL Connection Function
# -----------------------------
def get_connection():
    # create SQLAlchemy engine
    engine = create_engine("mysql+pymysql://root:Azhagu1910%40@localhost/Harvard_Artifactse")
    return engine


# -----------------------------
# Query Runner
# -----------------------------
def run_query(sql):
    conn = get_connection()
    df = pd.read_sql(sql, conn)
    return df

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="🎨🏛 Harvard’s Artifacts Collection", layout="wide")

# -----------------------------
# Header
# -----------------------------
st.markdown("<h1 style='text-align:center;'>🎨🏛 Harvard’s Artifacts Collection</h1>", unsafe_allow_html=True)

# -----------------------------
# Tabs
# -----------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📥 Collect Data",
    "📤 Migrate to SQL",
    "🗂 SQL Queries",
    "📊 View Tables"
])

# -----------------------------
# TAB 1 – Collect Data
# -----------------------------
with tab1:
    classification = st.text_input("Enter a classification:", placeholder="Paintings")
    if st.button("Collect data"):
        # Placeholder: Replace with actual Harvard API call
        st.success(f"Dummy data collected for classification: {classification}")
        st.write("**Metadata**", [{"id": 1, "title": "Sample Artifact", "culture": "Byzantine", "century": "11th century"}])
        st.write("**Media**", [{"objectid": 1, "imagecount": 2, "mediacount": 2}])
        st.write("**Colours**", [{"objectid": 1, "color": "Red", "hue": 0, "percent": 50}])

# -----------------------------
# TAB 2 – Migrate to SQL
# -----------------------------
with tab2:
    st.write("Insert the collected data")
    if st.button("Insert"):
        # Here you'd insert collected data into MySQL
        st.success("Data Inserted successfully")

# -----------------------------
# TAB 3 – SQL Queries
# -----------------------------
with tab3:
    queries = {
        "1. Artifacts from 17th century & Japanese culture":
            "SELECT * FROM artifact_metadata WHERE century = '17th century' AND culture = 'Japanese';",

        "2. Unique cultures represented":
            "SELECT DISTINCT culture FROM artifact_metadata WHERE culture IS NOT NULL;",

        "3. Artifacts from the Edo Period (1615–1868)":
            "SELECT * FROM artifact_metadata WHERE period = 'Edo period, 1615-1868';",

        "4. Artifact titles ordered by accession year (descending)":
            "SELECT title FROM artifact_metadata ORDER BY accessionyear DESC;",

        "5. Artifact count per department":
            "SELECT department, COUNT(*) AS artifact_count FROM artifact_metadata GROUP BY department;",

        "6. Artifacts with more than 3 images":
            "SELECT * FROM artifact_media WHERE imagecount > 3;",

        "7. Average rank of all artifacts":
            "SELECT AVG(`rank`) AS avg_rank FROM artifact_media;",

        "8. Artifacts with mediacount < colorcount":
            "SELECT * FROM artifact_media WHERE mediacount < colorcount;",

        "9. Artifacts created between 1500 and 1600":
            "SELECT * FROM artifact_media WHERE datebegin >= 1500 AND dateend <= 1600;",

        "10. Number of artifacts with no media files":
            "SELECT COUNT(*) AS no_media_count FROM artifact_media WHERE mediacount = 0;",

        "11. Distinct colors used in the dataset":
            "SELECT DISTINCT color FROM artifact_colors;",

        "12. Top 5 most used colors by frequency":
            "SELECT color, COUNT(*) AS frequency FROM artifact_colors GROUP BY color ORDER BY frequency DESC LIMIT 5;",

        "13. Average coverage percentage for each hue":
            "SELECT hue, AVG(percent) AS avg_percentage FROM artifact_colors WHERE hue IS NOT NULL GROUP BY hue ORDER BY avg_percentage DESC;",

        "14. Colors for artifact ID 192476":
            "SELECT color FROM artifact_colors WHERE objectid = 192476;",

        "15. Total number of color entries":
            "SELECT COUNT(*) AS total_color_entries FROM artifact_colors;",

        "16. Titles & hues for artifacts in Byzantine culture":
            "SELECT m.title, c.hue FROM artifact_metadata m JOIN artifact_colors c ON m.id = c.objectid WHERE m.culture = 'Byzantine';",

        "17. Each artifact title with its associated hues":
            "SELECT m.title, c.hue FROM artifact_metadata m JOIN artifact_colors c ON m.id = c.objectid;",

        "18. Titles, cultures, and media ranks where period is not null":
            "SELECT m.title, m.culture, me.rank FROM artifact_metadata m JOIN artifact_media me ON m.id = me.objectid WHERE m.period IS NOT NULL;",

        "19. Top 10 ranked artifacts with hue 'Grey'":
            "SELECT T1.title, T2.hue, T3.rank FROM artifact_metadata T1 JOIN artifact_colors T2 ON T1.id = T2.objectid JOIN artifact_media T3 ON T1.id = T3.objectid WHERE T2.hue = 'Grey' ORDER BY T3.rank DESC LIMIT 10;",

        "20. Artifacts per classification and avg media count":
            "SELECT m.classification, COUNT(*) AS total_artifacts, AVG(me.mediacount) AS avg_media_count FROM artifact_metadata m JOIN artifact_media me ON m.id = me.objectid GROUP BY m.classification;",

        "21. Artifacts that have a known medium":
            "SELECT * FROM artifact_metadata WHERE medium IS NOT NULL;",

        "22. Count of unique periods":
            "SELECT COUNT(DISTINCT period) AS unique_periods FROM artifact_metadata;",

        "23. Artifact titles that belong to 'Paintings' classification":
            "SELECT title FROM artifact_metadata WHERE classification = 'Paintings';",

        "24. Earliest and latest accession years":
            "SELECT MIN(accessionyear) AS earliest_accession, MAX(accessionyear) AS latest_accession FROM artifact_metadata;",

        "25. Artifacts where department is 'Harvard University Portrait Collection'":
            "SELECT * FROM artifact_metadata WHERE department = 'Harvard University Portrait Collection';"
    }

    choice = st.selectbox("Select a query to run", list(queries.keys()))
    if st.button("Run Query"):
        sql = queries[choice]
        df = run_query(sql)
        st.dataframe(df, use_container_width=True)

# -----------------------------
# TAB 4 – View Tables
# -----------------------------
with tab4:
    st.markdown("### View Full Tables")

    table_choice = st.selectbox(
        "Select a table to view:",
        ["artifact_metadata", "artifact_media", "artifact_colors"]
    )

    if st.button("Show Table"):
        sql = f"SELECT * FROM {table_choice} LIMIT 100;"  # Limit to 100 rows
        df = run_query(sql)
        st.dataframe(df, use_container_width=True)