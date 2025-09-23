---
title: "Problem Set 1: Analysis of Racial Disparities in Felony Sentencing"
nav_exclude: true
---

{% set hw = schedule.exercises.entries[0] %}
{% set hw_num = 1 %}
{% include 'homework.html' %}

---

## Corrections & Clarifications

- **1.2.2**: Try to do so efficiently (e.g., write a function and apply to a column, rather than edit the variable repeatedly in separate line for each recoded offense)
- **1.3**: Create `sentenceymd_derived` that's a version of `SENTENCE_DATE` converted to datetime format. Also create a rounded version, `sentenceym_derived`, that's rounded down to the first day of the month (e.g., `1/5/2016` would become `1/1/2016` and `3/27/2018` would become `3/1/2018`)


## How to Submit

### Prepare Your Notebook

1. Open your `.ipynb` file (JupyterLab, VS Code).
2. **Run all cells** so outputs are visible:
    - JupyterLab: `Kernel → Restart Kernel and Run All Cells`
    - VS Code: `Restart → Run All`
3. **Save** the notebook so outputs are stored in the `.ipynb`.

### Convert Your Notebook to PDF

Choose one method below:

1. Jupyter Lab built-in
    - `File → Save and Export Notebook As → PDF`  
    - (If you see LaTeX errors, use one of the alternatives below.)
2. VS Code
    - `... → Export → PDF` (or press `Cmd+Shift+P` (Mac)/ `Ctrl+Shift+P` (Windows) and select `Jupyter: Export to PDF`).
3. Command line (`nbconvert`)
    - HTML → Browser → Print as PDF (no LaTeX needed but code can get cut off):
        ```bash
        jupyter nbconvert --to html your_notebook.ipynb
        # then open the generated .html in a browser and Print → Save as PDF
        ```
    - Direct PDF (requires LaTeX):
        ```bash
        jupyter nbconvert --to pdf your_notebook.ipynb
        ```

Before moving on: confirm the PDF shows all code, text, and output.


### Submit TWO Files on Gradescope

1. Log in to [Gradescope](https://www.gradescope.com/courses/1132872), you will see two assignments for this problem set.
2. Upload **both** `.ipynb` and `.pdf` files:
    - Assignment `PS0{{hw_num}} - ipynb`: The `.ipynb` file (with saved outputs).
    - Assignment `PS0{{hw_num}} - PDF`: The`.pdf` file you just created.
3. If prompted to **Match pages to questions**:
    - Click **Assign** and map the correct page(s) to each question.
    - Ensure all questions are assigned.


### Add Your Group Members

1. After uploading, click **Group Members** at the bottom.
2. Search and add all teammates enrolled in the course.
3. Confirm everyone is listed—Gradescope will share the submission and grade.


### Final Checks

- Open the submitted **PDF preview** to confirm everything looks correct.
- Verify you submitted both the `.ipynb` and `.pdf` files.
- Verify all your group members are listed.
- If something is wrong, feel free to resubmit before the deadline.

