# TGG Schema Implementation Guide

Interactive reference tool for the TGG Product JSON-LD schema update project.

## Tabs

- **State Matrix** — click any cell to see decision inputs, schema changes, and before/after JSON
- **Decision Flow** — full if-this-then-that map across all 21 purchase state × lifecycle combinations

## Run locally

```bash
pip install streamlit
streamlit run app.py
```

## Deploy to Streamlit Cloud

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set main file to `app.py`
5. Deploy
