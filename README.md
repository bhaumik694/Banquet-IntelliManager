# 🏛️ Banquet-IntelliManager

> A full-stack banquet management and intelligence platform designed to unify sales, finance, operations, and guest experience into a single, data-driven system.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
- [Environment Variables](#environment-variables)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**Banquet-IntelliManager** is a comprehensive, full-stack platform built to digitize and streamline banquet hall operations. It brings together all critical business functions — sales pipeline, financial tracking, event operations, and guest experience management — into one unified, data-driven system.

Whether you're managing a single venue or a chain of banquet facilities, this platform gives operations teams real-time visibility and control across every touchpoint of an event lifecycle.

---

## ✨ Features

- **Event & Booking Management** — Create, update, and track bookings from inquiry to post-event follow-up.
- **Sales Pipeline Tracking** — Monitor leads, quotations, and conversion rates across your sales team.
- **Finance & Billing** — Generate invoices, track payments, and manage outstanding balances.
- **Operations Dashboard** — Coordinate staff assignments, hall configurations, and vendor management.
- **Guest Experience** — Manage guest profiles, preferences, dietary requirements, and communications.
- **AI-Powered Intelligence** — FastAPI-backed analytics layer providing insights and recommendations.
- **Role-Based Access Control** — Distinct portals and permissions for admins, sales staff, operations, and finance teams.
- **Reports & Analytics** — Data-driven dashboards for revenue trends, booking patterns, and operational KPIs.

---

## 🛠️ Tech Stack

| Layer       | Technology                          |
|-------------|--------------------------------------|
| **Frontend**  | JavaScript (React.js / Next.js)    |
| **Backend**   | Node.js (Express.js)               |
| **AI/ML API** | Python (FastAPI)                   |
| **Database**  | MongoDB / PostgreSQL *(inferred)*  |
| **Styling**   | CSS / Tailwind CSS *(inferred)*    |

---

## 📁 Project Structure

```
Banquet-IntelliManager/
├── frontend/          # React/Next.js client application
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   └── package.json
│
├── backend/           # Node.js/Express REST API server
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   └── package.json
│
├── fastapi/           # Python FastAPI service for analytics & AI features
│   ├── main.py
│   ├── routers/
│   └── requirements.txt
│
├── .vscode/           # Editor settings
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- [Node.js](https://nodejs.org/) (v18 or higher)
- [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/)
- [Python](https://www.python.org/) (v3.9 or higher)
- [pip](https://pip.pypa.io/)

---

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/bhaumik694/Banquet-IntelliManager.git
cd Banquet-IntelliManager
```

**2. Install Frontend dependencies**

```bash
cd frontend
npm install
```

**3. Install Backend dependencies**

```bash
cd ../backend
npm install
```

**4. Install FastAPI dependencies**

```bash
cd ../fastapi
pip install -r requirements.txt
```

---

### Running the App

Open three separate terminals and run each service:

**Frontend**
```bash
cd frontend
npm run dev
```

**Backend**
```bash
cd backend
npm run dev
```

**FastAPI (Python AI service)**
```bash
cd fastapi
uvicorn main:app --reload
```

By default:
- Frontend runs at `http://localhost:3000`
- Backend runs at `http://localhost:5000`
- FastAPI service runs at `http://localhost:8000`

