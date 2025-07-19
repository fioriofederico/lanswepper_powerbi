# Lansweeper Power BI Integration

Progetto di tesi magistrale: integrazione dati da Lansweeper con Power BI, elaborati via Python e Machine Learning.

## Features

- Recupero asset da Lansweeper via API OAuth2
- Pulizia dati
- Esposizione su API REST
- Visualizzazione in Power BI
- (WIP) Analisi predittiva asset

## Setup

1. Crea un file `.env` nella root con:
```
LS_CLIENT_ID=il_tuo_client_id
LS_CLIENT_SECRET=il_tuo_client_secret
```

2. Installa i pacchetti:
```bash
pip install -r requirements.txt
```

3. Avvia l'app:
```bash
python main.py
```

Power BI → Ottieni dati → Da Web → `http://localhost:5000/api/assets`
