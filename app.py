import streamlit as st
import pandas as pd
import altair as alt
import os
import base64

# إعدادات الصفحة
st.set_page_config(
    page_title="بوابة الأكاديمية المهنية للمعلمين - فرع الجيزة", 
    page_icon="🏫", 
    layout="wide"
)

# تخصيص CSS
st.markdown("""
    <style>
    html, body, [class*="css"] { direction: rtl; text-align: right; }
    h3, .stMarkdown h3 { direction: rtl !important; text-align: right !important; }
    [data-testid="collapsedControl"] { display: none !important; }
    
    .app-header-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 40px 20px; border-radius: 16px; color: white;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3); margin-bottom: 30px;
        border: 1px solid #334155; text-align: center;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
    }
    .app-logo-img {
        width: 180px !important; min-width: 180px !important; max-width: 180px !important;
        height: auto !important; border-radius: 12px; object-fit: contain;
        background: rgba(255, 255, 255, 0.05); padding: 8px;
        border: 1px solid rgba(255, 255, 255, 0.15); margin-bottom: 20px;
    }
    .app-main-title { font-size: 34px !important; font-weight: 800 !important; margin: 0 0 10px 0 !important; color: #ffffff !important; }
    .app-sub-title { font-size: 18px !important; color: #38bdf8 !important; font-weight: 600 !important; margin: 0 !important; }

    .metric-card-1 { background: linear-gradient(135deg, #1f4037 0%, #99f2c8 100%); padding: 15px; border-radius: 12px; color: white; text-align: center; margin-bottom: 10px; }
    .metric-card-2 { background: linear-gradient(135deg, #2b5876 0%, #4e4376 100%); padding: 15px; border-radius: 12px; color: white; text-align: center; margin-bottom: 10px; }
    .metric-card-3 { background: linear-gradient(135deg, #f7971e 0%, #ffd200 100%); padding: 15px; border-radius: 12px; color: #333; text-align: center; margin-bottom: 10px; }
    .metric-card-4 { background: linear-gradient(135deg, #833ab4 0%, #fd1d1d 50%, #fcb045 100%); padding: 15px; border-radius: 12px; color: white; text-align: center; margin-bottom: 10px; }
    .metric-card-5 { background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%); padding: 15px; border-radius: 12px; color: white; text-align: center; margin-bottom: 10px; }
    .metric-card-6 { background: linear-gradient(135deg, #cb356b 0%, #bd3f32 100%); padding: 15px; border-radius: 12px; color: white; text-align: center; margin-bottom: 10px; }
    
    .cpd-card-box { background: #1e293b; border: 1px solid #334155; padding: 15px; border-radius: 12px; color: white; margin-bottom: 15px; }
    .cpd-total-box { background: linear-gradient(135deg, #0f172a 100%, #1e3a8a 0%); border: 2px solid #3b82f6; padding: 18px; border-radius: 14px; color: white; margin-bottom: 25px; }
    .cpd-title { font-size: 15px; font-weight: bold; color: #38bdf8; margin-bottom: 10px; border-bottom: 1px solid #475569; padding-bottom: 5px; }
    .cpd-total-title { font-size: 17px; font-weight: bold; color: #facc15; margin-bottom: 12px; border-bottom: 1px solid #3b82f6; padding-bottom: 6px; text-align: center; }
    .cpd-stats { display: flex; justify-content: space-around; text-align: center; font-size: 13px; }
    .stat-item span { display: block; font-size: 16px; font-weight: bold; margin-top: 4px; }
    .card-title { font-size: 14px !important; font-weight: bold; margin-bottom: 5px; }
    .card-number { font-size: 22px; font-weight: bold; }
    .program-header { font-size: 20px !important; font-weight: bold; color: #1e293b; border-bottom: 2px solid #3b82f6; padding-bottom: 8px; margin-top: 20px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# صلاحيات الأدمن
st.sidebar.markdown("### 🔐 لوحة التحكم وصلاحيات الأدمن")
admin_password = st.sidebar.text_input("أدخل كلمة مرور الأدمن للتنزيل:", type="password")
ADMIN_SECRET_KEY = "Giza2026"
is_admin = (admin_password == ADMIN_SECRET_KEY)

if not is_admin:
    st.markdown("<style>[data-testid='stDataFrameToolbar'] { display: none !important; }</style>", unsafe_allow_html=True)
else:
    st.sidebar.success("✅ تم تفعيل صلاحيات الأدمن بنجاح")

# الشعار
found_logo_path = None
for name in ["logo.png", "Logo.png", "logo.jpg", "Logo.jpg"]:
    if os.path.exists(name):
        found_logo_path = name
        break

if found_logo_path:
    with open(found_logo_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    mime_type = "image/jpeg" if found_logo_path.lower().endswith(('jpg', 'jpeg')) else "image/png"
    logo_display_html = f'<img src="data:{mime_type};base64,{encoded_string}" class="app-logo-img">'
else:
    logo_display_html = '<div style="color: #f87171; font-size: 12px;">⚠️ لم يتم العثور على الشعار</div>'

st.markdown(f"""
    <div class="app-header-box">
        {logo_display_html}
        <div class="app-main-title">الأكاديمية المهنية للمعلمين - فرع الجيزة</div>
        <div class="app-sub-title">بوابة الخدمات الرقمية وإدارة بيانات المعلمين المتكاملة</div>
    </div>
""", unsafe_allow_html=True)

# 🚀 دالة تحميل الملفات مع التخزين المؤقت لسرعة الفتح (Caching)
@st.cache_data
def load_excel_file(filename):
    if os.path.exists(filename):
        try:
            df = pd.read_excel(filename)
            df.index = range(1, len(df) + 1)
            df.index.name = "م"
            return df
        except Exception:
            return None
    return None

# دالة لتصفية الملف الكلي بحسب سنة/كلمة مفتاحية إن لم يتوفر ملف مستقل
def filter_dataframe_by_keyword(df, keyword):
    if df is not None:
        mask = df.astype(str).apply(lambda x: x.str.contains(str(keyword), case=False, na=False)).any(axis=1)
        filtered_df = df[mask]
        if not filtered_df.empty:
            filtered_df = filtered_df.copy()
            filtered_df.index = range(1, len(filtered_df) + 1)
            filtered_df.index.name = "م"
            return filtered_df
    return None

# تحميل الملفات الأساسية والمستقلة
df_training = load_excel_file("training.xlsx")
df_job = load_excel_file("job.xlsx")
df_cader = load_excel_file("cader.xlsx")
df_reassign = load_excel_file("160.xlsx")
df_batch1 = load_excel_file("batch1.xlsx")
df_batch2 = load_excel_file("batch2.xlsx")
df_cpd = load_excel_file("CPD To 12-5-2026.xlsx")

# 📁 تحميل الأقسام المضافة (سواء كانت ملفات منفصلة أو تصفية تلقائية من الملفات الأساسية)
df_tot_2023 = load_excel_file("tot2023.xlsx") or load_excel_file("tot_2023.xlsx") or filter_dataframe_by_keyword(df_training, "2023")
df_cader_2024 = load_excel_file("cader2024.xlsx") or load_excel_file("cader_2024.xlsx") or filter_dataframe_by_keyword(df_cader, "2024")
df_cader_2025 = load_excel_file("cader2025.xlsx") or load_excel_file("cader_2025.xlsx") or filter_dataframe_by_keyword(df_cader, "2025")
df_cader_2026 = load_excel_file("cader2026.xlsx") or load_excel_file("cader_2026.xlsx") or filter_dataframe_by_keyword(df_cader, "2026")

# حساب الأعداد
c_training = len(df_training) if df_training is not None else 0
c_job = len(df_job) if df_job is not None else 0
c_cader = len(df_cader) if df_cader is not None else 0
c_reassign = len(df_reassign) if df_reassign is not None else 0
c_batch1 = len(df_batch1) if df_batch1 is not None else 0
c_batch2 = len(df_batch2) if df_batch2 is not None else 0

# 🚀 دالة حساب إحصائيات CPD مصنعة ومخزنة مؤقتاً
@st.cache_data
def get_cpd_exact_stats(df, program_keyword):
    if df is not None:
        prog_col = next((c for c in df.columns if "البرنامج" in str(c)), df.columns[4] if len(df.columns) > 4 else df.columns[-2])
        result_col = next((c for c in df.columns if "النتيجة" in str(c) or "الحالة" in str(c)), df.columns[-1])
            
        sub_df = df[df[prog_col].astype(str).str.contains(program_keyword, case=False, na=False)]
        total = len(sub_df)
        if total == 0: return 0, 0, 0, 0
            
        res_series = sub_df[result_col].astype(str).str.strip()
        passed = len(sub_df[res_series.str.contains("^اجتياز$", case=False, regex=True, na=False)])
        failed = len(sub_df[res_series.str.contains("عدم الاجتياز|عدم اجتياز", case=False, na=False)])
        absent = len(sub_df[res_series.str.contains("عدم الحضور|عدم حضور", case=False, na=False)])
        
        return total, passed, failed, absent
    return 0, 0, 0, 0

cpd_p1_total, cpd_p1_pass, cpd_p1_fail, cpd_p1_abs = get_cpd_exact_stats(df_cpd, "التطبيقات التربوية")
cpd_p2_total, cpd_p2_pass, cpd_p2_fail, cpd_p2_abs = get_cpd_exact_stats(df_cpd, "مدير/ وكيل إدارة مدرسية")
cpd_p3_total, cpd_p3_pass, cpd_p3_fail, cpd_p3_abs = get_cpd_exact_stats(df_cpd, "التوجيه الفنى")
cpd_p4_total, cpd_p4_pass, cpd_p4_fail, cpd_p4_abs = get_cpd_exact_stats(df_cpd, "إدارة تعليمية")

cpd_grand_total = cpd_p1_total + cpd_p2_total + cpd_p3_total + cpd_p4_total
cpd_grand_pass = cpd_p1_pass + cpd_p2_pass + cpd_p3_pass + cpd_p4_pass
cpd_grand_fail = cpd_p1_fail + cpd_p2_fail + cpd_p3_fail + cpd_p4_fail
cpd_grand_abs = cpd_p1_abs + cpd_p2_abs + cpd_p3_abs + cpd_p4_abs

# 🌟 التبويبات بعد إضافة اعتماد ToT 2023 والتسكين بالأعوام (2024, 2025, 2026)
selected_section = st.tabs([
    "🏠 الرئيسية والبحث الشامل",
    "📁 معد البرامج",
    "🎓 اعتماد مدربين (ToT) 2023",
    "📁 المسمى الوظيفي",
    "📁 التسكين علي الكادر الشامل",
    "📊 تسكين الكادر 2024",
    "📊 تسكين الكادر 2025",
    "📊 تسكين الكادر 2026",
    "📁 قرار 160",
    "📁 معلم مساعد الدفعة 1",
    "📁 معلم مساعد الدفعة 2",
    "📁 منصة الوزارة CPD"
])

# 1. الرئيسية
with selected_section[0]:
    st.markdown("### 🔎 البحث الشامل بالكود في كافة الملفات والبرامج")
    global_search_code = st.text_input("أدخل كود المعلم للبحث الفوري عنه:", placeholder="مثال: 3089097")

    if global_search_code:
        st.markdown("---")
        st.subheader("🎯 نتائج البحث الشامل:")
        
        def check_and_display(df, program_name):
            if df is not None:
                mask = df.astype(str).apply(lambda x: x.str.contains(global_search_code, case=False, na=False)).any(axis=1)
                result = df[mask]
                if not result.empty:
                    st.markdown(f"#### تم العثور على نتائج في برنامج: <span style='color: #2563eb;'>{program_name}</span>", unsafe_allow_html=True)
                    st.dataframe(result, use_container_width=True)

        check_and_display(df_training, "معد البرامج التدريبية")
        check_and_display(df_tot_2023, "اعتماد مدربين (ToT) 2023")
        check_and_display(df_job, "المسمى الوظيفي")
        check_and_display(df_cader, "التسكين علي الكادر الشامل")
        check_and_display(df_cader_2024, "تسكين الكادر 2024")
        check_and_display(df_cader_2025, "تسكين الكادر 2025")
        check_and_display(df_cader_2026, "تسكين الكادر 2026")
        check_and_display(df_reassign, "إعادة التعيين (قرار 160)")
        check_and_display(df_batch1, "معلم مساعد الدفعة الأولى")
        check_and_display(df_batch2, "معلم مساعد الدفعة الثانية")
        check_and_display(df_cpd, "برامج منصة الوزارة CPD")
        st.markdown("---")

    st.markdown("### 📌 مؤشرات الإحصاء العامة لبرامج الفرع")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="metric-card-1"><div class="card-title">معد البرامج التدريبية</div><div class="card-number">{c_training}</div></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="metric-card-4"><div class="card-title">إعادة التعيين (قرار 160)</div><div class="card-number">{c_reassign}</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card-2"><div class="card-title">المسمى الوظيفي</div><div class="card-number">{c_job}</div></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="metric-card-5"><div class="card-title">معلم مساعد (الدفعة الأولى)</div><div class="card-number">{c_batch1}</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card-3"><div class="card-title">التسكين علي الكادر الإجمالي</div><div class="card-number">{c_cader}</div></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="metric-card-6"><div class="card-title">معلم مساعد (الدفعة الثانية)</div><div class="card-number">{c_batch2}</div></div>', unsafe_allow_html=True)

    st.markdown("### 📊 نتيجة منصة CPD حتي 12-5-2026 ")
    st.markdown(f"""
        <div class="cpd-total-box">
            <div class="cpd-total-title">🌟 الإجمالي العام لجميع برامج منصة الوزارة CPD</div>
            <div class="cpd-stats">
                <div class="stat-item" style="color: #38bdf8;">إجمالي المتدربين<span>{cpd_grand_total}</span></div>
                <div class="stat-item" style="color: #4ade80;">إجمالي الاجتياز<span>{cpd_grand_pass}</span></div>
                <div class="stat-item" style="color: #f87171;">إجمالي عدم الاجتياز<span>{cpd_grand_fail}</span></div>
                <div class="stat-item" style="color: #fbbf24;">إجمالي عدم الحضور<span>{cpd_grand_abs}</span></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    cpd_col1, cpd_col2 = st.columns(2)
    with cpd_col1:
        st.markdown(f'<div class="cpd-card-box"><div class="cpd-title">📚 التطبيقات التربوية للمعلم المساعد 2026/2025</div><div class="cpd-stats"><div class="stat-item" style="color: #38bdf8;">الإجمالي<span>{cpd_p1_total}</span></div><div class="stat-item" style="color: #4ade80;">اجتياز<span>{cpd_p1_pass}</span></div><div class="stat-item" style="color: #f87171;">عدم اجتياز<span>{cpd_p1_fail}</span></div><div class="stat-item" style="color: #fbbf24;">عدم حضور<span>{cpd_p1_abs}</span></div></div></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="cpd-card-box"><div class="cpd-title">👔 تدريب القيادات / التوجيه الفنى 2026/2025</div><div class="cpd-stats"><div class="stat-item" style="color: #38bdf8;">الإجمالي<span>{cpd_p3_total}</span></div><div class="stat-item" style="color: #4ade80;">اجتياز<span>{cpd_p3_pass}</span></div><div class="stat-item" style="color: #f87171;">عدم اجتياز<span>{cpd_p3_fail}</span></div><div class="stat-item" style="color: #fbbf24;">عدم حضور<span>{cpd_p3_abs}</span></div></div></div>', unsafe_allow_html=True)
    with cpd_col2:
        st.markdown(f'<div class="cpd-card-box"><div class="cpd-title">🏫 تدريب القيادات مدير/ وكيل إدارة مدرسية 2026/2025</div><div class="cpd-stats"><div class="stat-item" style="color: #38bdf8;">الإجمالي<span>{cpd_p2_total}</span></div><div class="stat-item" style="color: #4ade80;">اجتياز<span>{cpd_p2_pass}</span></div><div class="stat-item" style="color: #f87171;">عدم اجتياز<span>{cpd_p2_fail}</span></div><div class="stat-item" style="color: #fbbf24;">عدم حضور<span>{cpd_p2_abs}</span></div></div></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="cpd-card-box"><div class="cpd-title">🏢 تدريب القيادات مدير/ وكيل إدارة تعليمية 2026/2025</div><div class="cpd-stats"><div class="stat-item" style="color: #38bdf8;">الإجمالي<span>{cpd_p4_total}</span></div><div class="stat-item" style="color: #4ade80;">اجتياز<span>{cpd_p4_pass}</span></div><div class="stat-item" style="color: #f87171;">عدم اجتياز<span>{cpd_p4_fail}</span></div><div class="stat-item" style="color: #fbbf24;">عدم حضور<span>{cpd_p4_abs}</span></div></div></div>', unsafe_allow_html=True)

    st.markdown("### 📈 التحليل البصري ومقارنة أعداد السجلات للبرامج")
    chart_data = pd.DataFrame({
        "البرنامج": ["معد البرامج", "المسمى الوظيفي", "التسكين", "قرار 160", "معلم مساعد 1", "معلم مساعد 2", "منصة الوزارة CPD"],
        "عدد السجلات": [c_training, c_job, c_cader, c_reassign, c_batch1, c_batch2, (len(df_cpd) if df_cpd is not None else 0)]
    })

    chart = alt.Chart(chart_data).mark_bar(color="#3b82f6", cornerRadiusTopLeft=4, cornerRadiusTopRight=4).encode(
        x=alt.X("البرنامج:N", sort=None, title="", axis=alt.Axis(labelAngle=0, labelFontSize=11)),
        y=alt.Y("عدد السجلات:Q", title="إجمالي السجلات"),
        tooltip=["البرنامج", "عدد السجلات"]
    ).properties(height=320)

    st.altair_chart(chart, use_container_width=True)

# 🚀 دالة عرض الأقسام التفصيلية المسرّعة
def render_section(title, df, tab_index, file_hint=""):
    with selected_section[tab_index]:
        st.markdown(f'<p class="program-header">📁 {title}</p>', unsafe_allow_html=True)
        if df is not None and not df.empty:
            st.metric(label=f"إجمالي السجلات في هذا الكشف", value=len(df))
            search_query = st.text_input(f"🔍 بحث مخصص داخل كشف {title}:", key=f"search_{title}_{tab_index}")
            display_df = df
            if search_query:
                mask = df.astype(str).apply(lambda x: x.str.contains(search_query, case=False, na=False)).any(axis=1)
                display_df = df[mask]
                st.info(f"عدد النتائج المطابقة للبحث: {len(display_df)}")
            
            st.dataframe(display_df, use_container_width=True)
        else:
            hint_msg = f" (يمكنك وضع ملف بالإسم: `{file_hint}` في المجلد)" if file_hint else ""
            st.warning(f"⚠️ تعذر العثور على سجلات سابقة لـ '{title}'{hint_msg}.")

# 🌟 عرض جميع المحتويات شاملة الأقسام الجديدة المطلوبة
render_section("معد البرامج التدريبية", df_training, 1)
render_section("اعتماد مدربين (ToT) 2023", df_tot_2023, 2, file_hint="tot2023.xlsx")
render_section("المسمى الوظيفي", df_job, 3)
render_section("التسكين علي الكادر الشامل", df_cader, 4)
render_section("التسكين علي الكادر 2024", df_cader_2024, 5, file_hint="cader2024.xlsx")
render_section("التسكين علي الكادر 2025", df_cader_2025, 6, file_hint="cader2025.xlsx")
render_section("التسكين علي الكادر 2026", df_cader_2026, 7, file_hint="cader2026.xlsx")
render_section("إعادة التعيين (قرار 160)", df_reassign, 8)
render_section("معلم مساعد الدفعة الأولى", df_batch1, 9)
render_section("معلم مساعد الدفعة الثانية", df_batch2, 10)
render_section("نتيجة برامج منصة الوزارة CPD", df_cpd, 11)

# الفوتر
st.markdown("""
    <div style="text-align: center; padding: 15px; margin-top: 30px; border-top: 1px solid #e2e8f0; color: #475569; font-size: 14px; font-weight: bold; background-color: #f8fafc; border-radius: 8px;">
        تصميم وتنفيذ: <span style="color: #2563eb;">أحمد الجنزوري</span> 🌟
    </div>
""", unsafe_allow_html=True)
