import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="แผนที่วัดเชียงใหม่",
    page_icon="⛩",
    layout="wide"
)

temples = [
    {
        "id": 1,
        "name": "วัดพระธาตุดอยสุเทพราชวรวิหาร",
        "lat": 18.8048,
        "lng": 98.9216,
        "history": "วัดพระธาตุดอยสุเทพราชวรวิหาร เป็นปูชนียสถานที่สำคัญและเป็นสัญลักษณ์ของเมืองเชียงใหม่มาช้านาน สร้างขึ้นตั้งแต่สมัยพญากือนาเมื่อกว่า 600 ปีที่แล้ว ภายในวัดเป็นที่ประดิษฐานขององค์พระเจดีย์ทรงเชียงแสนสีทองอร่าม ที่บรรจุพระบรมสารีริกธาตุขององค์สมเด็จพระสัมมาสัมพุทธเจ้าไว้",
        "famous": "มีความเชื่อว่าหากได้มากราบไหว้สักการะครบทั้งสี่ทิศ พร้อมเดินเวียนขวา 3 รอบ จะช่วยให้ชีวิตพบเจอแต่ความราบรื่นและประสบความสำเร็จตามที่ปรารถนา",
        "category": "พระธาตุ",
        "color": "#D4A017",
    },
    {
        "id": 2,
        "name": "วัดอุโมงค์ (สวนพุทธธรรม)",
        "lat": 18.7779,
        "lng": 98.9676,
        "history": "วัดโบราณที่สร้างขึ้นตั้งแต่สมัยพญามังราย มีอายุเก่าแก่กว่า 700 ปี จุดเด่นของวัดแห่งนี้คือ อุโมงค์เก่าแก่ ที่สร้างขึ้นในสมัยพญากือนาเพื่อถวายให้พระมหาเถรจันทร์ได้ใช้เป็นสถานที่ปฏิบัติธรรม ภายในอุโมงค์เป็นทางเดินเชื่อมถึงกันหลายช่อง",
        "famous": "เหมาะสำหรับผู้ที่ต้องการขอพรให้ชีวิตได้พบเจอหนทางใหม่ หรือเริ่มต้นสิ่งดี ๆ อีกครั้ง บรรยากาศเงียบสงบ ร่มรื่นไปด้วยต้นไม้นานาพันธุ์",
        "category": "วัดสมาธิ",
        "color": "#2E7D32",
    },
    {
        "id": 3,
        "name": "วัดพระธาตุดอยคำ",
        "lat": 18.7674,
        "lng": 98.9425,
        "history": "วัดเก่าแก่ที่มีอายุมากกว่า 1,300 ปี ตั้งอยู่บนเนินเขาสูงจากตัวเมือง ซึ่งในอดีตสร้างขึ้นในสมัยพระนางจามเทวี และเป็นที่รู้จักกันในนาม วัดสุวรรณบรรพต",
        "famous": "พระพุทธรูปหลวงพ่อทันใจ มีชื่อเสียงโดดเด่นในเรื่องความศักดิ์สิทธิ์มากที่สุด โดยเฉพาะในด้านการเงิน การงาน โชคลาภ และการเสี่ยงโชค",
        "category": "พระธาตุ",
        "color": "#D4A017",
    },
    {
        "id": 4,
        "name": "วัดป่าแดด",
        "lat": 18.7533,
        "lng": 98.9873,
        "history": "วัดที่เหมาะสำหรับผู้ที่ต้องการขอพรเรื่องการงาน ความสำเร็จ และความก้าวหน้าในชีวิต ภายในวัดมีเอกสารแนะนำขั้นตอนการไหว้ขอพรให้สมหวัง",
        "famous": "ขึ้นชื่อเรื่องความศักดิ์สิทธิ์ของ องค์พระพิฆเนศ หรือที่รู้จักกันในนาม อุตรศรีคณปติ ซึ่งเป็นเทพเจ้าแห่งความสำเร็จและผู้ขจัดอุปสรรคทั้งปวง",
        "category": "วัดมงคล",
        "color": "#C62828",
    },
    {
        "id": 5,
        "name": "วัดอุปคุต",
        "lat": 18.7797,
        "lng": 98.9984,
        "history": "วัดศักดิ์สิทธิ์เชียงใหม่ที่ตั้งอยู่ในย่านช้างคลาน ขึ้นชื่อเรื่องการขอพรจาก พระอุปคุต ซึ่งประดิษฐานอยู่บนวิหาร ผู้ที่มาสักการะเชื่อกันว่าการขอพรจากพระอุปคุตจะช่วยเปิดทางให้ชีวิตเจริญรุ่งเรือง",
        "famous": "ประเพณีตักบาตรเที่ยงคืน หรือที่ชาวล้านนาเรียกว่า ตักบาตรเป็งปุ๊ด ซึ่งจัดขึ้นเฉพาะในคืนวันเพ็ญที่ตรงกับวันพุธเท่านั้น",
        "category": "วัดมงคล",
        "color": "#C62828",
    },
    {
        "id": 6,
        "name": "วัดเจดีย์หลวงวรวิหาร",
        "lat": 18.7868,
        "lng": 98.9872,
        "history": "วัดเก่าแก่ที่มีความสำคัญทางประวัติศาสตร์และสถาปัตยกรรมมาอย่างยาวนานกว่า 600 ปี ใจกลางเมืองเชียงใหม่ เป็นที่ประดิษฐานของพระเจดีย์หลวง ซึ่งเคยเป็นเจดีย์ที่ใหญ่ที่สุดในภาคเหนือ มีความสูงถึง 92 เมตร",
        "famous": "มีศาลหลักเมือง หรือเสาอินทขิล สร้างความมั่นคงให้ชาวเชียงใหม่ และ ท้าวเวสสุวรรณ ที่นิยมในการขอพรเพื่อความเป็นสิริมงคลและความเจริญรุ่งเรือง",
        "category": "วัดประวัติศาสตร์",
        "color": "#6A1B9A",
    },
    {
        "id": 7,
        "name": "วัดพระสิงห์วรมหาวิหาร",
        "lat": 18.7874,
        "lng": 98.9836,
        "history": "พระอารามหลวงชั้นเอกที่ตั้งอยู่ใจกลางคูเมืองเชียงใหม่ มีประวัติยาวนานกว่า 600 ปี สร้างขึ้นโดยพญาผายู กษัตริย์องค์ที่ 5 แห่งราชวงศ์มังราย",
        "famous": "เป็นที่ประดิษฐานของ พระพุทธสิหิงค์ หรือ พระสิงห์ ขึ้นชื่อเรื่องความเมตตาและเสน่ห์เมตตามหานิยม ทำให้มีแต่คนรักใคร่และเอ็นดู เป็นวัดประจำปีเกิดของคนปีมะโรง",
        "category": "พระอารามหลวง",
        "color": "#E65100",
    },
    {
        "id": 8,
        "name": "วัดดวงดี",
        "lat": 18.7892,
        "lng": 98.9881,
        "history": "เดิมชื่อ วัดต้นหมากเหนือ ตั้งอยู่ในเขตเมืองเก่าของเชียงใหม่ โดดเด่นด้วยสถาปัตยกรรมแบบล้านนาอันงดงามที่สร้างจากไม้แกะสลักอย่างประณีต มีอายุยาวนานกว่า 100 ปี",
        "famous": "ชื่อเป็นมงคล ขึ้นชื่อเรื่องการขอพรให้โชคดีในด้านการเงินและโชคลาภ สายมูนิยมมาเสริมดวงชะตาและปัดเป่าความโชคร้าย",
        "category": "วัดมงคล",
        "color": "#C62828",
    },
    {
        "id": 9,
        "name": "วัดลอยเคราะห์",
        "lat": 18.7841,
        "lng": 98.9936,
        "history": "เดิมชื่อ วัดร้อยข้อ สร้างขึ้นในสมัยพญากือนาเมื่อกว่า 500 ปีที่แล้ว ตั้งอยู่ใจกลางเมืองเชียงใหม่ โดดเด่นด้วยสถาปัตยกรรมแบบล้านนาอันงดงาม",
        "famous": "เป็นที่ประดิษฐานของ พระพุทธศุภโชคศรีลอยเคราะห์มิ่งมงคล และ พระเจ้าทันใจ นิยมมากราบไหว้เพื่อเสริมดวงชะตา ลอยเคราะห์ ลอยโศก",
        "category": "วัดมงคล",
        "color": "#C62828",
    },
    {
        "id": 10,
        "name": "วัดหมื่นล้าน",
        "lat": 18.7882,
        "lng": 98.9899,
        "history": "หรือ วัดหมื่นสามล้าน ตั้งอยู่บนถนนราชดำเนิน สร้างขึ้นในช่วงรัชสมัยพระเจ้าติโลกราช เพื่ออุทิศส่วนบุญกุศลให้แก่แม่ทัพที่เสียชีวิตในสนามรบ",
        "famous": "ชื่อวัดสื่อถึงความมั่งคั่ง ผู้คนนิยมมาขอพรด้านการเงิน โชคลาภ โดดเด่นด้วยสถาปัตยกรรมแบบพม่าผสมล้านนา มีลวดลายไม้แกะสลักรูปนกยูงรำแพน",
        "category": "วัดประวัติศาสตร์",
        "color": "#6A1B9A",
    },
    {
        "id": 11,
        "name": "วัดล่ามช้าง",
        "lat": 18.7843,
        "lng": 98.9853,
        "history": "วัดราษฎร์เก่าแก่ที่สร้างขึ้นในสมัยพญามังรายตั้งแต่ปี พ.ศ. 1839 ชื่อของวัดได้มาจากการที่ในอดีตเคยเป็นสถานที่ล่ามช้างคู่พระบารมีของกษัตริย์",
        "famous": "พระเจ้ามุกดอกไม้ สมปรารถนาศรีเมืองเชียงใหม่ สร้างจากดอกไม้แห้งผสมมวลสารศักดิ์สิทธิ์ เชื่อว่าหากได้กลิ่นหอมอ่อน ๆ ของดอกไม้ จะช่วยให้เรื่องร้ายกลายเป็นดี",
        "category": "วัดประวัติศาสตร์",
        "color": "#6A1B9A",
    },
    {
        "id": 12,
        "name": "วัดดับภัย",
        "lat": 18.7862,
        "lng": 98.9914,
        "history": "เดิมมีชื่อว่า วัดอภัย หรือ วัดตุงกระด้าง เป็นที่ประดิษฐานของ พระเจ้าดับภัย พระพุทธรูปศักดิ์สิทธิ์ที่เชื่อกันว่ามีอานุภาพในการขจัดปัดเป่าทุกข์ภัยและโรคภัยไข้เจ็บ",
        "famous": "มีกิจกรรมพิธีสืบชะตาสะเดาะเคราะห์ในช่วงเดือนพฤษภาคมของทุกปี ผู้คนนิยมมาสักการะเพื่อสะเดาะเคราะห์และเสริมดวงชะตา",
        "category": "วัดมงคล",
        "color": "#C62828",
    },
    {
        "id": 13,
        "name": "วัดโลกโมฬี",
        "lat": 18.7944,
        "lng": 98.9821,
        "history": "วัดเก่าแก่กว่า 500 ปี ย่านคูเมืองเชียงใหม่ โดดเด่นด้วยวิหารไม้สักสถาปัตยกรรมล้านนา และเจดีย์โบราณที่งดงาม บรรยากาศสงบร่มเย็น",
        "famous": "เป็นที่นิยมในการมาสักการะ พระนางจิรประภามหาเทวี เพื่อขอพรด้านความรัก ความราบรื่นในการงานและชีวิต และชมโคมยี่เป็งหลากสีในช่วงปลายปี",
        "category": "วัดประวัติศาสตร์",
        "color": "#6A1B9A",
    },
    {
        "id": 14,
        "name": "วัดพันเตา",
        "lat": 18.7863,
        "lng": 98.9884,
        "history": "สร้าง พ.ศ.1934 เคยเป็นเขตสังฆาวาสของวัดโชติการาม (วัดเจดีย์หลวง) สันนิษฐานว่าบริเวณที่ตั้งเคยเป็นสถานที่ตั้งเส้าพันเตา เป็นเตาที่ใช้หลอมทองหล่อพระอัฎฐารส",
        "famous": "จุดเด่นวิหารหอคำ สร้างด้วยไม้สัก ภายในประดิษฐาน พระเจ้าปันเต้า มีความหมายว่า มีความสำเร็จเพิ่มพูนเป็นร้อยเท่าพันเท่า",
        "category": "วัดประวัติศาสตร์",
        "color": "#6A1B9A",
    },
    {
        "id": 15,
        "name": "วัดเด่นสะหลีศรีเมือง",
        "lat": 18.7959,
        "lng": 98.9742,
        "history": "เดิมชื่อวัดบ้านเด่น ตั้งแต่ครูบาเจ้าเทืองมาจำพรรษา จากที่ไม่เคยมีต้นโพธิ์เลยก็มีต้นโพธิ์ขึ้นมากมาย ชาวเมืองเหนือเรียกต้นโพธิ์ว่า ต้นสะหลี ซึ่งมีความหมายว่าเป็นมงคลดี",
        "famous": "วัดตั้งอยู่ในเขตเมืองเก่าโบราณชื่อเมืองแกน ชาวบ้านเรียกชื่อเต็มว่า วัดเด่นสะหลีศรีเมืองแกน ขึ้นชื่อเรื่องต้นโพธิ์ศักดิ์สิทธิ์และความเป็นมงคล",
        "category": "วัดมงคล",
        "color": "#C62828",
    },
]

category_colors = {
    "พระธาตุ": "#D4A017",
    "วัดสมาธิ": "#2E7D32",
    "วัดมงคล": "#C62828",
    "วัดประวัติศาสตร์": "#6A1B9A",
    "พระอารามหลวง": "#E65100",
}

# --- Header ธีมล้านนา ---
st.markdown("""
    <style>
    .stApp { background-color: #FBF0DC; }
    .lanna-header {
        background: linear-gradient(135deg, #6B2D2D 0%, #8B3A3A 40%, #A0522D 100%);
        border-bottom: 3px solid #D4A017;
        padding: 16px 24px;
        border-radius: 8px;
        margin-bottom: 16px;
        text-align: center;
        box-shadow: 0 2px 12px rgba(0,0,0,0.35);
    }
    .lanna-title { color: #FFF3D0; font-size: 2rem; font-weight: 700; margin: 0; }
    .lanna-subtitle { color: #D4A017; font-size: 1rem; margin: 4px 0 0; }
    .lanna-ornament { color: #D4A017; font-size: 1.3rem; }
    .temple-card {
        background: #FFF8EC;
        border: 1.5px solid rgba(212,160,23,0.3);
        border-radius: 8px;
        padding: 10px 12px;
        margin-bottom: 6px;
        cursor: pointer;
    }
    .temple-card:hover { border-color: #D4A017; background: #FFF3D0; }
    .popup-title { font-weight: 700; font-size: 1rem; margin: 0 0 6px; }
    .popup-section { margin-top: 8px; }
    .popup-label { font-weight: 700; color: #6B2D2D; font-size: 0.85rem; }
    .popup-text { font-size: 0.85rem; line-height: 1.5; color: #3B1A00; }
    div[data-testid="stSidebar"] { background-color: #F5E6C8; }
    </style>
    <div class="lanna-header">
        <div>
            <p class="lanna-ornament">✦ ✦ ✦</p>
            <h1 class="lanna-title">⛩ แผนที่วัดเชียงใหม่</h1>
            <p class="lanna-subtitle">15 วัดชื่อดังแห่งดินแดนล้านนา</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- Sidebar: รายชื่อวัด + กรองหมวดหมู่ ---
with st.sidebar:
    st.markdown("## 🗺️ รายชื่อวัด")
    categories = ["ทั้งหมด"] + list(category_colors.keys())
    selected_category = st.selectbox("กรองตามหมวดหมู่", categories)

    st.markdown("---")
    filtered = temples if selected_category == "ทั้งหมด" else [t for t in temples if t["category"] == selected_category]

    selected_temple = None
    for temple in filtered:
        color = category_colors.get(temple["category"], "#C62828")
        label = f"**{temple['id']}.** {temple['name']}"
        if st.button(label, key=f"btn_{temple['id']}", use_container_width=True):
            selected_temple = temple
            st.session_state["selected_id"] = temple["id"]

    st.markdown("---")
    st.markdown("**สีตามหมวดหมู่:**")
    for cat, color in category_colors.items():
        st.markdown(f"<span style='color:{color}'>●</span> {cat}", unsafe_allow_html=True)

# --- สร้างแผนที่ Folium ---
if "selected_id" in st.session_state:
    focus = next((t for t in temples if t["id"] == st.session_state["selected_id"]), None)
    center = [focus["lat"], focus["lng"]] if focus else [18.7867, 98.9867]
    zoom = 16 if focus else 13
else:
    center = [18.7867, 98.9867]
    zoom = 13

m = folium.Map(location=center, zoom_start=zoom, tiles="OpenStreetMap")

filtered_temples = temples if selected_category == "ทั้งหมด" else [t for t in temples if t["category"] == selected_category]

for temple in filtered_temples:
    color = temple["color"]
    popup_html = f"""
    <div style="font-family: 'Sarabun', sans-serif; width: 300px;">
        <div style="background:{color}; padding:12px 14px; border-radius:6px 6px 0 0;">
            <span style="color:rgba(255,255,255,0.8); font-size:0.7rem;">วัดที่ {temple['id']}</span>
            <h2 style="color:white; font-size:1rem; margin:4px 0; line-height:1.3;">{temple['name']}</h2>
            <span style="background:rgba(255,255,255,0.2); color:white; padding:2px 8px; border-radius:12px; font-size:0.7rem;">{temple['category']}</span>
        </div>
        <div style="background:#FFFBF2; padding:12px 14px; border-radius:0 0 6px 6px;">
            <p style="color:#6B2D2D; font-weight:700; font-size:0.8rem; margin:0 0 4px;">📜 ประวัติ</p>
            <p style="font-size:0.8rem; line-height:1.6; color:#3B1A00; margin:0 0 10px;">{temple['history']}</p>
            <p style="color:#6B2D2D; font-weight:700; font-size:0.8rem; margin:0 0 4px;">⭐ เรื่องขึ้นชื่อ</p>
            <p style="font-size:0.8rem; line-height:1.6; color:#3B1A00; margin:0;">{temple['famous']}</p>
        </div>
    </div>
    """
    icon_html = f"""
        <div style="
            background:{color};
            width:36px; height:36px;
            border-radius:50% 50% 50% 0;
            transform:rotate(-45deg);
            border:2px solid white;
            box-shadow:0 2px 6px rgba(0,0,0,0.4);
            display:flex; align-items:center; justify-content:center;">
            <span style="transform:rotate(45deg); font-size:16px;">⛩</span>
        </div>
    """
    folium.Marker(
        location=[temple["lat"], temple["lng"]],
        popup=folium.Popup(popup_html, max_width=320),
        tooltip=f"⛩ {temple['name']}",
        icon=folium.DivIcon(html=icon_html, icon_size=(36, 36), icon_anchor=(18, 36)),
    ).add_to(m)

st_folium(m, width=None, height=580, returned_objects=[])

st.markdown("""
    <div style="text-align:center; background:#3B1A00; color:#D4A017;
                padding:8px; border-radius:6px; margin-top:8px;
                font-size:0.8rem; letter-spacing:0.1em;">
        ล้านนา · เชียงใหม่ · ดินแดนแห่งพระธาตุและวัดศักดิ์สิทธิ์
    </div>
""", unsafe_allow_html=True)
