# ETF Premium Tracker

A Python-based FastAPI service that calculates the **premium or discount of an ETF** by comparing its market price with its indicative NAV (iNAV).

## Features

* Fetches ETF market prices using **Yahoo Finance (`yfinance`)**
* Retrieves iNAV data from **AMFI**
* Calculates ETF premium/discount percentage
* Exposes the result through a **FastAPI REST API**
* Uses **SQLAlchemy** for database persistence
* Separates market-price and iNAV retrieval using provider components
* Uses a service/repository-based architecture
* Supports scheduled processing with **APScheduler**
* Includes structured logging and custom exception handling

## Architecture

```text
Client
  │
FastAPI
  │
ETF Service
  ├── Market Price Provider  → Yahoo Finance
  ├── iNAV Provider          → AMFI
  └── Repository             → SQLAlchemy / SQLite
              │
        APScheduler
```

## Premium Calculation

```text
Premium / Discount (%) =
((Market Price - iNAV) / iNAV) × 100
```

## Tech Stack

**Python | FastAPI | SQLAlchemy | SQLite | yfinance | Requests | APScheduler | Uvicorn**

## Running Locally

```bash
git clone https://github.com/ArunK2654/ETF_Premium_Tracker.git
cd ETF_Premium_Tracker

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload
```

## Example

```text
Market Price: ₹123.45
iNAV:         ₹121.20
Premium:      1.86%
Status:       Premium
```

