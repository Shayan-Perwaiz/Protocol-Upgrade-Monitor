# Protocol Upgrade Monitor

## Overview

The **Protocol Upgrade Monitor** is a high-performance system designed to track blockchain network events, predict volatility and liquidity shifts, and provide actionable insights for trading strategies. It integrates with blockchain APIs (Etherscan, Tally) and market data streams (CoinGecko) to deliver real-time risk assessments for protocol upgrades and governance activities. Built with FastAPI, the system offers a robust and scalable API for monitoring contract events, analyzing governance risks, calculating market volatility, and computing comprehensive risk scores.

The source code is located in the `src` directory.

## Features

- **Event Monitoring**: Tracks and decodes blockchain contract events using Etherscan APIs.
- **Governance Risk Analysis**: Evaluates governance proposals from Tally to assess protocol stability.
- **Market Volatility Tracking**: Calculates token volatility based on CoinGecko price history.
- **Risk Scoring**: Combines governance, price volatility, and liquidity metrics for a unified risk score.
- **Real-Time Insights**: Connects to external APIs for up-to-date blockchain and market data.
- **Scalable Architecture**: Utilizes FastAPI for high-performance, asynchronous API endpoints.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Real-Time Input Examples](#real-time-input-examples)
- [Project Structure](#project-structure)

## Prerequisites

To run the Protocol Upgrade Monitor, ensure you have the following installed:

- **Python**: 3.8 or higher
- **pip**: Python package manager
- **Git**: For cloning the repository
- **API Keys**:
  - [Etherscan API Key](https://etherscan.io/apis) (free tier available)
  - [CoinGecko Pro API Key](https://www.coingecko.com/en/api) (pro tier required for some endpoints)
  - [Tally API Key](https://docs.tally.xyz/api/api-keys) (contact Tally for access)
- **Optional**: Virtual environment tool (e.g., `venv` or `virtualenv`)

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Shayan-Perwaiz/Protocol-Upgrade-Monitor.git
   cd Protocol-Upgrade-Monitor
   ```

## Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

## Configure Environment Variables

**Create a .env file in the root directory and add your API keys**:

ETHERSCAN_API_KEY=your_etherscan_api_key
COINGECKO_API_KEY=your_coingecko_api_key
TALLY_API_KEY=your_tally_api_key

## Running the Project

**Start the FastAPI Server**:
uvicorn src.main:app --reload

# API Endpoints

| Endpoint               | Method | Description                                                     | Query Parameters                                |
| ---------------------- | ------ | --------------------------------------------------------------- | ----------------------------------------------- |
| `/`                    | GET    | Verifies the server is running                                  | None                                            |
| `/monitor/decode-logs` | GET    | Decodes blockchain contract event logs using Etherscan          | `address` (required), `topic0` (optional)       |
| `/governance/risk`     | GET    | Analyzes governance risk based on Tally proposals               | `governor_id` (required)                        |
| `/volatility`          | GET    | Calculates token volatility using CoinGecko price history       | `token_id` (required)                           |
| `/risk-score`          | GET    | Computes a risk score based on governance, price, and liquidity | `token_id` (required), `protocol_id` (required) |

# Real-Time Input Examples

Below are real-time input examples for each API endpoint, using publicly available Ethereum-based values as of July 2025. Interviewers can use these to test the project’s functionality.

> ⚠️ Valid API keys are required. Free-tier keys may have rate limits.

---

### 1. Root Endpoint
**Purpose**: Verify the server is running.

```bash
curl http://localhost:8000/
```
**Expected Output**:
```json
{"message": "Protocol upgrade monitor is running"}
```

---

### 2. Decode Contract Logs (`/monitor/decode-logs`)
**Purpose**: Fetch and decode event logs for the Uniswap V3 Factory contract.

```bash
curl "http://localhost:8000/monitor/decode-logs?address=0x1F98431c8aD98523631AE4a59f267346ea31F984"
```
**Details**:
- `address`: `0x1F98431c8aD98523631AE4a59f267346ea31F984` (Uniswap V3 Factory on Ethereum Mainnet)
- `topic0`: Optional; use `0x783cca1c0412dd0d6955f6990f7a9a76f6a873f2a97f1b7d335ecef27e8496f1` for PoolCreated events

**Expected Output** (example):
```json
[
  {
    "event": "PoolCreated",
    "args": {
      "token0": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
      "token1": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
      "fee": 3000,
      "tickSpacing": 60,
      "pool": "0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f4A27"
    }
  },
  {
    "error": "No matching event ABI found for topic0",
    "log": { ... }
  }
]
```

---

### 3. Governance Risk Analysis (`/governance/risk`)
**Purpose**: Analyze governance risk for Aave’s governance contract.

```bash
curl "http://localhost:8000/governance/risk?governor_id=eip155:1:0xEC5685aA8E856fB9dA2C8c4F716C2cDa3C6f5eB8"
```
**Details**:
- `governor_id`: `eip155:1:0xEC5685aA8E856fB9dA2C8c4F716C2cDa3C6f5eB8` (Aave Governance V2 on Ethereum Mainnet)

**Expected Output** (example):
```json
{
  "governance_risk": "Moderate",
  "proposal_count": 8,
  "active_proposals": [
    {
      "proposalId": "123456",
      "title": "Aave V3 Upgrade Proposal",
      "state": "ACTIVE",
      "createdAt": "2025-07-01T12:00:00Z",
      "eta": "2025-07-15T12:00:00Z",
      "votes": {
        "against": 1500,
        "for": 4500
      }
    }
  ]
}
```

---

### 4. Token Volatility (`/volatility`)
**Purpose**: Calculate 7-day price volatility for Uniswap’s UNI token.

```bash
curl "http://localhost:8000/volatility?token_id=uniswap"
```
**Details**:
- `token_id`: `uniswap` (CoinGecko ID for UNI token)

**Expected Output** (example):
```json
{
  "token_id": "uniswap",
  "volatility_score": 6.85
}
```

---

### 5. Risk Score (`/risk-score`)
**Purpose**: Compute a risk score for UNI token and Aave governance.

```bash
curl "http://localhost:8000/risk-score?token_id=uniswap&protocol_id=eip155:1:0xEC5685aA8E856fB9dA2C8c4F716C2cDa3C6f5eB8"
```
**Details**:
- `token_id`: `uniswap`
- `protocol_id`: `eip155:1:0xEC5685aA8E856fB9dA2C8c4F716C2cDa3C6f5eB8` (Aave Governance V2)

**Expected Output** (example):
```json
{
  "risk_score": 55,
  "details": {
    "governance_risk": "Active proposal in progress",
    "price_risk": "High volatility (6.85%)",
    "liquidity_risk": "High market cap ($4,800,000,000)"
  }
}
```

---

📌 **Note**: You can find `token_id` on [CoinGecko](https://www.coingecko.com/) and `governor_id` on [Tally](https://www.tally.xyz/). Replace with other tokens/protocols to test different real-time values.

Protocol-Upgrade-Monitor/
├── src/
│   ├── main.py                    # FastAPI application entry point
│   ├── config/
│   │   └── apiConfig.py           # API key configuration
│   ├── controller/
│   │   ├── governance_controller.py  # Governance risk endpoints
│   │   ├── market_controller.py      # Market volatility endpoints
│   │   ├── monitor_controller.py     # Event monitoring endpoints
│   │   └── risk_controller.py        # Risk scoring endpoints
│   ├── service/
│   │   ├── GovernanceService/
│   │   │   └── governance_service.py  # Governance risk analysis logic
│   │   ├── etherscan_service/
│   │   │   ├── log_decoder.py         # Log decoding logic
│   │   │   └── monitor_service.py     # Event fetching logic
│   │   ├── market_analysis/
│   │   │   └── volatility_service.py  # Volatility calculation logic
│   │   └── risk_analysis/
│   │       └── risk_scoring_service.py # Risk scoring logic
│   ├── repository/
│   │   ├── etherscan/
│   │   │   ├── etherscan_repo.py      # Etherscan log fetching
│   │   │   └── etherscanABI_repo.py   # Etherscan ABI fetching
│   │   ├── GovernanceProposal/
│   │   │   └── governanceProposal_repo.py # Tally proposal fetching
│   │   └── marketData/
│   │       └── coinGecko_repo.py      # CoinGecko market data fetching
│   └── helpers/
│       └── etherscanhelpers.py        # Utility functions for Etherscan
├── .env                           # Environment variables (API keys)
├── requirements.txt               # Project dependencies
└── README.md                     # Project documentation
