import streamlit as st
import random

st.set_page_config(page_title="CampusMate", page_icon="🎓")

st.title("🎓 Your CampusMate")

# Keep chat history
if "messages" not in st.session_state:
    st.session_state.messages = []  # list of {"role": "user"/"assistant", "content": str, "type": "text"/"image"}

# simple rule based response
def get_response(user_input: str):
    text = user_input.lower()
    words = text.split()  

    # Small talk
    if any(kw in words for kw in ["hi", "hello", "hey"]):
        return {"type": "text", "content": "👋 Hi there! How are you today?"}
    elif "how are you" in text:
        return {"type": "text", "content": "😊 I'm doing great, thanks for asking! How about you?"}
    elif any(kw in words for kw in ["good", "fine", "great", "okay", "happy", "excited"]):
        return {"type": "text", "content": "👍 Glad to hear that! Let’s keep going."}
    elif any(kw in text for kw in ["bad", "not good", "sad", "unhappy", "tired"]):
        return {"type": "text", "content": "💙 I'm sorry to hear that. Remember, tough days don’t last forever. You’ve got this! 💪"}
    elif any(kw in text for kw in ["bye", "see you", "goodbye"]):
        return {"type": "text", "content": "👋 Bye! Have a nice day at university!"}
    elif any(kw in text for kw in ["fact", "interesting", "share", "tell me", "something"]):
        facts = [
            "📖 Did you know? Research shows that studying in short sessions of 25–30 minutes with breaks (Pomodoro method) helps improve memory retention.",
            "🧠 Your brain actually uses more energy when you’re learning something new compared to when you’re resting!",
            "📝 Writing notes by hand has been proven to help students remember information better than just typing them.",
            "☕ Drinking coffee or tea before studying can boost focus, but too much caffeine may reduce memory performance.",
            "🎓 Studies show that students who join clubs and societies in university tend to perform better academically and socially."
        ]
        return {"type": "text", "content": random.choice(facts)}

    # University-related Q&A
    elif "map" in text or "utar map" in text:
        return {"type": "image", "content": "Kampar_Campus_Map.jpg"}

    elif "library" in text:
        return {"type": "text", "content": "📚 The library is located at Block I (Heritage Hall area). It opens from 8 AM to 9 PM."}

    elif any(kw in text for kw in ["exam", "register", "enroll", "course"]):
        return {"type": "text", "content": "📝 Register for exams or courses via the UTAR portal under 'Academics'."}

    elif any(kw in text for kw in ["canteen", "food", "cafeteria", "restaurant"]):
        return {"type": "text", "content": "🍔 The main canteen is behind Block C near Heritage Hall. There are also smaller cafeterias around Block D and Block K."}

    elif any(kw in text for kw in ["sports", "gym", "fitness", "stadium"]):
        return {"type": "text", "content": "⚽ The Sports Complex is at Block J, near the lake. The gym is located in Block C."}

    elif any(kw in text for kw in ["wifi", "internet", "network"]):
        return {"type": "text", "content": "🌐 Connect to 'utarwifi'. Username = student ID, password = IC number."}

    elif any(kw in text for kw in ["hostel", "dorm", "accommodation"]):
        return {"type": "text", "content": "🏠 UTAR does not provide hostels on-campus, but private rental houses and apartments are available around Kampar. Many students stay in Westlake Homes nearby."}

    elif any(kw in text for kw in ["bus", "shuttle", "transport"]):
        return {"type": "text", "content": "🚌 Shuttle buses run from the East Gate and South Gate to nearby housing areas. Frequency: every 20–30 minutes during peak hours."}

    elif any(kw in text for kw in ["clinic", "health", "medical"]):
        return {"type": "text", "content": "🏥 The UTAR clinic is at Block D (ground floor). Open Mon–Fri, 9 AM – 5 PM."}

    elif any(kw in text for kw in ["parking", "car", "motorcycle","park"]):
        return {"type": "text", "content": "🚗 Student parking zones are marked in yellow on the campus map. Apply for a parking sticker from the Admin Office."}

    elif any(kw in text for kw in ["scholarship", "financial aid", "loan"]):
        return {"type": "text", "content": "💰 Scholarships, study loans, and financial aid are available at the Financial Aid Office in Block E."}

    elif any(kw in text for kw in ["counseling", "mental health", "support"]):
        return {"type": "text", "content": "💙 Free counseling services are available at Block J. Book appointments through the Student Affairs Office."}

    elif any(kw in text for kw in ["lab", "laboratory", "computer room","computer"]):
        return {"type": "text", "content": "🖥️ Computer labs are in Block B and Block F. Labs are open from 8 AM – 6 PM. Bring your student ID for access."}

    elif any(kw in text for kw in ["events", "club", "society", "activities"]):
        return {"type": "text", "content": "🎉 Student clubs and societies are managed at Block K (Student Pavilion). You can join or start clubs there."}

    elif any(kw in text for kw in ["lecture hall", "classroom", "hall"]):
        return {"type": "text", "content": "🏫 Lecture Halls (Block L) and tutorial rooms are spread across Blocks B, C, D, and F."}

    elif any(kw in text for kw in ["study room", "reading room", "quiet area"]):
        return {"type": "text", "content": "📖 The Library also has dedicated quiet study rooms on the 2nd floor for group or individual study."}

    elif any(kw in text for kw in ["heritage hall", "events hall", "graduation"]):
        return {"type": "text", "content": "🎓 Heritage Hall, near the South Gate, is used for major events, exams, and graduation ceremonies."}

    # Fallback
    else:
        return {"type": "text", "content": "🤔 Sorry, I don’t know that yet. Please check with the student help desk."}



# Show existing chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["type"] == "text":
            st.markdown(msg["content"])
        elif msg["type"] == "image":
            st.image(msg["content"], caption="📷 University View", use_container_width=True)

# Input pinned at the bottom
if prompt := st.chat_input("Ask question about university  or just say hi…"):
    st.session_state.messages.append({"role": "user", "content": prompt, "type": "text"})
    with st.chat_message("user"):
        st.markdown(prompt)

    reply = get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": reply["content"], "type": reply["type"]})
    with st.chat_message("assistant"):
        if reply["type"] == "text":
            st.markdown(reply["content"])
        elif reply["type"] == "image":
            st.image(reply["content"], caption="📷 University View", use_container_width=True)

# Reset button
with st.sidebar:
    if st.button("🧹 Clear chat"):
        st.session_state.messages = []
        st.rerun()
