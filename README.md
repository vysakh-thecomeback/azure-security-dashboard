
# Azure Security Posture & Threat Response Automation Dashboard

This project automates Azure security monitoring using Defender Secure Score, Logic Apps alerts, Power BI dashboards, and Sentinel queries.

---

# Components

- scripts/defender-secure-score-api.py  
  Retrieves Secure Score via REST API; saves to `secure_score_data.json`.

- logic-apps/alert-response-workflow.json  
  Logic App JSON to fetch Defender alerts every 5 minutes, filter high-severity, and send email notifications.

- sentinel-kql/suspicious-logins.kql  
  Kusto query to identify top users with failed sign-ins (useful in Sentinel).

- docs/  
  - `architecture.png` – solution architecture  
  - `dashboard-screenshot.png` – Power BI visuals of Secure Score

---

# Setup Guide

1. Clone repo  
   ```bash
   git clone https://github.com/yourusername/azure-security-dashboard.git
   cd azure-security-dashboard
