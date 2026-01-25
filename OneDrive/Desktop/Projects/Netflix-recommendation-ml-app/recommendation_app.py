import streamlit as st
from netflix_recommendation import recommend

st.title("🎬 Netflix Movie & TV Show Recommender")

user_input = st.text_input("Enter a movie or show you like")

if user_input:
    recs = recommend(user_input)
    st.subheader("Recommendations")
    for rec in recs:
        if 'error' in rec:
            st.error(rec['error'])
            break
        with st.expander(f"🎥 {rec['title']}"):
            if rec['poster']:
                st.image(rec['poster'], width=200)
            st.write(f"**Description:** {rec['description']}")
            st.write(f"**Release Year:** {rec['release_year']}")
            st.write(f"**Rating:** {rec['rating']}")
            genres_clean = rec['genres'].strip('[]').replace("'", "").replace('"', '')
            st.write(f"**Genres:** {genres_clean}")
            st.write(f"**Seasons:** {rec['seasons']}")
            st.write(f"**IMDb Score:** {rec['imdb_score']}")
