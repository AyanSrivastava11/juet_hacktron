import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def show_team_page():
    """Display the team page with custom styling"""
    # Custom CSS
    st.markdown("""
    <style>
        .team-section {
            text-align: center;
            padding: 20px;
        }
        
        .team-section h2 {
            font-size: 2.5rem;
            margin-bottom: 40px;
            color: #fff;
        }
        
        .team-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 30px;
            margin-bottom: 40px;
        }
        
        .team-card {
            background: #295f4e;
            border-radius: 15px;
            width: 250px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(255,255,255,0.1);
            transition: transform 0.3s ease;
            color: #fff;
        }
        
        .team-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 6px 12px rgba(255,255,255,0.2);
        }
        
        .team-card img {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            object-fit: cover;
            margin-bottom: 15px;
            border: 2px solid #444;
        }
        
        .team-card h3 {
            margin: 10px 0 5px;
            font-size: 1.2rem;
            color: #fff;
        }
        
        .team-card p.role {
            color: #bbb;
            font-size: 0.9rem;
            margin-bottom: 10px;
        }
        
        .team-card p.quote {
            font-size: 0.85rem;
            color: #ccc;
            margin-bottom: 15px;
        }
        
        .social-icons a {
            margin: 0 8px;
            text-decoration: none;
            font-size: 1.5rem;
            color: #fff;
        }
        
        .social-icons a:hover {
            color: #0077b5;
        }
        
        .social-icons img {
            width: 20px;
            height: 20px;
            transition: transform 0.3s;
        }
        
        .social-icons img:hover {
            transform: scale(1.2);
        }
        
        /* Set background color */
        .stApp {
            background-color: #000;
        }
    </style>
    """, unsafe_allow_html=True)

    # Team data
    team_members = [
        {
            "name": "Ayan Srivastava",
            "role": "Team Leader",
            "quote": "The best error message is the one that never shows up.",
            "image": "https://randomuser.me/api/portraits/women/1.jpg",
            "linkedin": "https://www.linkedin.com/in/ayan-srivastava-017a89259/",
            "github": "https://github.com/AyanSrivastava11"
        },
        {
            "name": "Aditi Singh",
            "role": "Team Member",
            "quote": "Computers are fast; programmers keep it slow",
            "image": "https://randomuser.me/api/portraits/men/2.jpg",
            "linkedin": "https://www.linkedin.com/in/aditi-singh-266456253",
            "github": "https://github.com/AditisS12"
        },
        {
            "name": "Aditi Gupta",
            "role": "Team Member",
            "quote": "Software is a great combination of artistry and engineering.",
            "image": "https://randomuser.me/api/portraits/women/3.jpg",
            "linkedin": "https://www.linkedin.com/in/guptaaditi18",
            "github": "https://github.com/Aditi-code123"
        }
    ]

    # Team page content
    st.markdown("""
    <div class="team-section">
        <h2>Meet the Team</h2>
        <div class="team-container">
    """, unsafe_allow_html=True)

    # Create team cards
    cols = st.columns(3)
    for idx, member in enumerate(team_members):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="team-card">
                <img src="{member['image']}" alt="{member['name']}">
                <h3>{member['name']}</h3>
                <p class="role">{member['role']}</p>
                <p class="quote">"{member['quote']}"</p>
                <div class="social-icons">
                    <a href="{member['linkedin']}" target="_blank">
                        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="24">
                    </a>
                    <a href="{member['github']}" target="_blank">
                        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="24">
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)