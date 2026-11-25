
import re
import unicodedata


def clean_invoice_text(text):
    """Nettoie le texte brut d'une facture."""

    text = unicodedata.normalize("NFKC", str(text))

    # Supprimer le formatage Markdown
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)

    # Supprimer les séparateurs de tableaux
    text = re.sub(
        r"^\s*\|?[\s|:-]+\|?\s*$",
        "",
        text,
        flags=re.MULTILINE
    )

    text = text.replace("|", " ")
    text = re.sub(r"[ \t]+", " ", text)

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    return "\n".join(lines)
