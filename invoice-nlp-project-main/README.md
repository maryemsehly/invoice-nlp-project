

\# Smart Invoice Analyzer



An NLP-based application designed to automatically extract key information from invoices written in French and English using text preprocessing and Regular Expressions (Regex).



\## Project Overview



Invoice processing often involves manually identifying important information such as supplier names, invoice numbers, dates, and financial amounts.



The objective of this project is to simplify this process by developing an automated information extraction system based on Natural Language Processing (NLP) techniques.



The application allows users to enter invoice text, process it, and retrieve the extracted information through an interactive web interface.



\## Objectives



The system aims to extract five important fields from invoice documents:



\- \*\*Supplier:\*\* Name of the invoice issuer.

\- \*\*Invoice Number:\*\* Unique invoice identifier.

\- \*\*Invoice Date:\*\* Date of invoice issuance.

\- \*\*Amount HT:\*\* Amount before taxes.

\- \*\*Amount TTC:\*\* Total amount including taxes.



\## Features



\- Text cleaning and normalization.

\- Tokenization and lemmatization.

\- French and English language processing.

\- Regex-based information extraction.

\- Text, date, and numerical value normalization.

\- Extraction results visualization.

\- CSV export functionality.

\- Interactive web interface using Streamlit.



\## Dataset



The project uses the \[Arabic-Latin Invoices Synthetic dataset](https://huggingface.co/datasets/KhalfounMehdi/arabic-latin-invoices-synthetic) from Hugging Face.



Although the original dataset contains Arabic, French, and English invoices, this project focuses exclusively on French and English documents.



Dataset preparation:



\- Original dataset: 4,014 invoices.

\- Eligible French and English invoices: 1,320.

\- Selected invoices: 70.

\- Development set: 50 invoices.

\- Test set: 20 invoices.



The dataset provides structured reference information used to evaluate the extraction results.



\## NLP Pipeline



The application follows these main processing steps:



1\. \*\*Text Input:\*\* The user provides the invoice text.

2\. \*\*Text Cleaning:\*\* Unicode normalization, removal of unnecessary formatting and extra spaces.

3\. \*\*Tokenization:\*\* Division of the text into smaller linguistic units.

4\. \*\*Lemmatization:\*\* Transformation of words into their canonical forms using spaCy.

5\. \*\*Information Extraction:\*\* Application of predefined regular expressions to the cleaned text.

6\. \*\*Normalization:\*\* Standardization of extracted text, dates, and amounts.

7\. \*\*Evaluation:\*\* Comparison with reference values from the dataset.



\*\*Note:\*\* Tokenization and lemmatization are used for NLP preprocessing and linguistic analysis. Regex extraction is performed directly on the cleaned text.



\## Technologies Used



| Technology | Purpose |

|---|---|

| Python | Main programming language |

| Regular Expressions (Regex) | Information extraction |

| spaCy | Tokenization and lemmatization |

| Pandas | Data manipulation and evaluation |

| Streamlit | Interactive web interface |

| Hugging Face | Dataset source |



\## Project Structure



```text

invoice\_nlp\_project/

│

├── app.py

├── preprocessing.py

├── extraction.py

├── requirements.txt

├── README.md

├── .gitignore

│

└── images/

&#x20;   ├── interface\_principale.png

&#x20;   ├── resultats\_extraction.png

&#x20;   └── pretraitement\_export.png

```



\## Installation



\### 1. Clone the repository



```bash

git clone https://github.com/maram20034/invoice-nlp-project.git

cd invoice-nlp-project

```



\### 2. Create a virtual environment



```bash

python -m venv venv

```



\### 3. Activate the environment



On Windows:



```bash

venv\\Scripts\\activate

```



\### 4. Install dependencies



```bash

pip install -r requirements.txt

```



\### 5. Download spaCy language models



```bash

python -m spacy download fr\_core\_news\_sm

python -m spacy download en\_core\_web\_sm

```



\### 6. Run the application



```bash

streamlit run app.py

```



The application will be available locally in your web browser.



\## Evaluation Results



The system was evaluated on a development set of 50 invoices and a separate test set of 20 invoices.



The observed results were:



\- Development set: 100% for the evaluated extraction metrics.

\- Test set: 100% for the evaluated extraction metrics.



All five target fields were correctly extracted from the 20 test invoices.



These results are specific to the selected synthetic dataset and evaluation sample. Further testing on real-world invoices is necessary to assess generalization.



\## Limitations and Future Improvements



Current limitations:



\- Regex rules depend on predefined labels and formats.

\- Unusual invoice layouts may cause extraction errors.

\- The current application processes text rather than invoice images.

\- Evaluation is based on a relatively small synthetic dataset.



Possible improvements:



\- Integration of OCR to process invoice images and PDFs.

\- Support for additional languages.

\- More flexible extraction rules.

\- Testing on real-world invoices.

\- Integration of advanced NLP models.



\## Author



\*\*Maram Jeghib\*\*



Academic NLP Project – 2026



\## License



This project was developed for academic purposes.



