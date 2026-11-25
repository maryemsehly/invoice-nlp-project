
import streamlit as st
import pandas as pd

from preprocessing import clean_invoice_text
from extraction import extract_invoice_fields


# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Smart Invoice Analyzer",
    page_icon="🧾",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# 2. INVOICE EXAMPLES
# ==========================================

examples = {
    "French invoice": """FACTURE

Fournisseur: Société Informatique Plus
Facture N°: FAC-2026-105
Date d'émission: 12/10/2026

Montant HT: 1200.00
TVA: 228.00
Total TTC: 1428.00""",

    "English invoice": """INVOICE

Seller: Global Technology Ltd
Invoice Number: INV-2026-205
Invoice Date: 20/10/2026

Net Amount: 850.00
VAT: 161.50
Amount Due: 1011.50""",

    "Alternative labels": """COMMERCIAL INVOICE

Billed By: Digital Services SARL
Bill No.: DS-2026-310
Date: 05/11/2026

Sub-total: 2400.00
VAT: 456.00
Total: 2856.00"""
}


# ==========================================
# 3. SESSION STATE
# ==========================================

if "invoice_text" not in st.session_state:
    st.session_state.invoice_text = ""

if "extraction_results" not in st.session_state:
    st.session_state.extraction_results = None

if "cleaned_text" not in st.session_state:
    st.session_state.cleaned_text = None


def load_example():
    selected = st.session_state.example_choice
    st.session_state.invoice_text = examples[selected]
    st.session_state.extraction_results = None
    st.session_state.cleaned_text = None


# ==========================================
# 4. CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

.main-header {
    padding: 28px;
    border-radius: 16px;
    background: linear-gradient(120deg, #1D4ED8, #2563EB, #0F766E);
    color: white;
    margin-bottom: 25px;
}

.main-header h1 {
    color: white;
    font-size: 32px;
    margin-bottom: 8px;
}

.main-header p {
    color: #E0E7FF;
    font-size: 15px;
    margin-bottom: 0;
}

.section-title {
    font-size: 21px;
    font-weight: 650;
    margin-bottom: 12px;
}

div[data-testid="stMetric"] {
    background: var(--secondary-background-color);
    border: 1px solid var(--border-color);
    padding: 18px;
    border-radius: 12px;
}

div[data-testid="stMetricValue"] {
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 5. SIDEBAR
# ==========================================

with st.sidebar:

    st.title("🧾 Smart Invoice")
    st.caption("NLP Information Extraction")

    st.divider()

    st.subheader("Test examples")

    st.selectbox(
        "Choose an invoice example",
        list(examples.keys()),
        key="example_choice"
    )

    st.button(
        "📥 Load selected example",
        on_click=load_example,
        use_container_width=True
    )

    st.divider()

    st.subheader("About the system")

    st.write(
        "This application extracts five important "
        "information fields from invoice text."
    )

    st.markdown("""
    - Supplier
    - Invoice number
    - Invoice date
    - Amount HT
    - Amount TTC
    """)

    st.divider()

    st.caption("Academic NLP Project — 2026")


# ==========================================
# 6. MAIN HEADER
# ==========================================

st.markdown("""
<div class="main-header">
    <h1>🧾 Smart Invoice Analyzer</h1>
    <p>
        Intelligent invoice information extraction
        using Natural Language Processing and Regular Expressions.
    </p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# 7. INPUT SECTION
# ==========================================

st.markdown(
    '<div class="section-title">📄 Invoice input</div>',
    unsafe_allow_html=True
)

st.write(
    "Paste the text content of your invoice below, "
    "or load one of the examples from the sidebar."
)

invoice_text = st.text_area(
    "Invoice content",
    key="invoice_text",
    height=280,
    placeholder=(
        "Paste your invoice text here...\n\n"
        "Supplier: Example Company\n"
        "Invoice Number: INV-2026-001\n"
        "Issue Date: 15/11/2026\n"
        "Subtotal: 500.00\n"
        "Grand Total: 595.00"
    ),
    label_visibility="collapsed"
)

col_button, col_info = st.columns([1, 2])

with col_button:
    analyze = st.button(
        "🔍 Analyze invoice",
        type="primary",
        use_container_width=True
    )

with col_info:
    st.caption(
        "The system will clean the text and apply "
        "the five validated Regex extraction functions."
    )


# ==========================================
# 8. EXTRACTION
# ==========================================

if analyze:

    if not invoice_text.strip():

        st.warning("Please enter invoice text before analysis.")

        st.session_state.extraction_results = None

    else:

        try:
            cleaned = clean_invoice_text(invoice_text)

            results = extract_invoice_fields(cleaned)

            st.session_state.cleaned_text = cleaned
            st.session_state.extraction_results = results

            st.success("Invoice analysis completed.")

        except Exception as error:

            st.error(f"An error occurred: {error}")


# ==========================================
# 9. RESULTS
# ==========================================

if st.session_state.extraction_results is not None:

    results = st.session_state.extraction_results

    found = sum(
        value is not None and str(value).strip() != ""
        for value in results.values()
    )

    total = len(results)
    missing = total - found

    st.divider()

    st.markdown(
        '<div class="section-title">📊 Extraction results</div>',
        unsafe_allow_html=True
    )

    # Summary metrics
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total fields",
        total
    )

    col2.metric(
        "Fields extracted",
        found,
        delta=f"{found}/{total}"
    )

    col3.metric(
        "Missing fields",
        missing
    )

    # Progress
    progress = found / total if total else 0

    st.progress(
        progress,
        text=f"Extraction coverage: {progress:.0%}"
    )

    st.divider()

    # Result cards
    st.subheader("Extracted information")

    columns = st.columns(2)

    for index, (label, value) in enumerate(results.items()):

        with columns[index % 2]:

            with st.container(border=True):

                st.caption(label)

                if value is not None and str(value).strip():

                    st.success(str(value), icon="✅")

                else:

                    st.warning(
                        "Information not detected",
                        icon="⚠️"
                    )

    # Overall status
    st.divider()

    if found == total:

        st.success(
            "All five fields were detected. "
            "Please verify the extracted values."
        )

    elif found > 0:

        st.warning(
            f"{missing} field(s) were not detected. "
            "Check the invoice text or its labels."
        )

    else:

        st.error(
            "No information was extracted. "
            "Please check the invoice content."
        )

    # Download
    st.subheader("Export results")

    results_df = pd.DataFrame(
        [
            {"Field": key, "Extracted Value": value or ""}
            for key, value in results.items()
        ]
    )

    csv_data = results_df.to_csv(
        index=False,
        encoding="utf-8-sig"
    )

    st.download_button(
        "⬇️ Download extraction results (CSV)",
        data=csv_data,
        file_name="invoice_extraction_results.csv",
        mime="text/csv",
        use_container_width=True
    )

    # Additional information
    tab1, tab2 = st.tabs([
        "Preprocessed text",
        "Original invoice text"
    ])

    with tab1:

        st.text_area(
            "Cleaned text",
            value=st.session_state.cleaned_text or "",
            height=220,
            disabled=True
        )

    with tab2:

        st.text_area(
            "Original text",
            value=invoice_text,
            height=220,
            disabled=True
        )


# ==========================================
# 10. FOOTER
# ==========================================

st.divider()

st.caption(
    "Smart Invoice Analyzer | NLP Academic Project | 2026"
)
