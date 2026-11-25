
import re


# ==========================================
# 1. Extraction du fournisseur
# ==========================================

def extract_supplier(text):
    pattern = (
        r"(?im)^\s*"
        r"(?:Fournisseur|Supplier|Seller|Vendeur|"
        r"Émetteur|Emetteur|From|Billed\s+By)"
        r"\s*:\s*(.+?)\s*$"
    )

    match = re.search(pattern, text)

    if match:
        supplier = match.group(1).strip()
        supplier = re.split(
            r"\s*[—–|]\s*",
            supplier,
            maxsplit=1
        )[0]

        return supplier.strip() if supplier.strip() else None

    return None


# ==========================================
# 2. Extraction du numéro de facture
# ==========================================

def extract_invoice_number(text):
    pattern = (
        r"(?im)^\s*"
        r"(?:"
        r"Facture\s*N[°ºo]?"
        r"|N[°ºo]?\s*Facture"
        r"|Inv\.?\s*Number"
        r"|Invoice\s*(?:Number|No\.?|#)"
        r"|Bill\s*No\.?"
        r"|N[°ºo]"
        r")"
        r"\s*:\s*"
        r"([A-Z0-9][A-Z0-9/-]*)"
    )

    match = re.search(pattern, text)

    if match:
        return match.group(1).strip()

    return None


# ==========================================
# 3. Extraction de la date de facture
# ==========================================

def extract_invoice_date(text):
    pattern = (
        r"(?im)^\s*"
        r"(?:"
        r"Date\s+d['’]émission"
        r"|Issue\s+Date"
        r"|Invoice\s+Date"
        r"|Date"
        r")"
        r"\s*:\s*"
        r"(\d{1,2}[/-]\d{1,2}[/-]\d{4})"
        r"\s*$"
    )

    match = re.search(pattern, text)

    if match:
        return match.group(1).strip()

    return None


# ==========================================
# 4. Extraction du montant HT
# ==========================================


def extract_amount_ht(text):
    pattern = (
        r"(?im)^\s*[-•]?\s*"
        r"(?:Montant\s+HT|Sous[-\s]?total|"
        r"Sub[-\s]?Total|Subtotal|Net\s+Amount)"
        r"\s*:\s*"
        r"([\d,]+(?:\.\d{1,2})?)"
    )

    match = re.search(pattern, text)

    if match:
        return match.group(1).strip()

    return None



# ==========================================
# 5. Extraction du montant TTC
# ==========================================

def extract_amount_ttc(text):
    pattern = (
        r"(?im)^\s*[-•]?\s*"
        r"(?:Total\s+TTC|Grand\s+Total|Total\s+Due|"
        r"Amount\s+Due|Montant\s+d[uû]|Total)"
        r"\s*:\s*"
        r"([\d,]+(?:\.\d{1,2})?)"
    )

    match = re.search(pattern, text)

    if match:
        return match.group(1).strip()

    return None


# ==========================================
# 6. Extraction complète des informations
# ==========================================

def extract_invoice_fields(text):

    return {
        "Fournisseur": extract_supplier(text),
        "Numéro de facture": extract_invoice_number(text),
        "Date d'émission": extract_invoice_date(text),
        "Montant HT": extract_amount_ht(text),
        "Montant TTC": extract_amount_ttc(text)
    }
