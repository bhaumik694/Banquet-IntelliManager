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
  - [Environment Variables](#environment-variables)
  - [Installation & Running](#installation--running)
- [API Overview](#api-overview)
- [ML Models](#ml-models)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**Banquet-IntelliManager** is an end-to-end banquet and event management platform built for modern hospitality businesses. It integrates a Node.js REST API backend, a React (Vite) frontend, and a Python AI/ML microservice layer — all working together to manage events, guests, menus, payments, venues, and real-time notifications in one unified system.

The platform features role-based dashboards (Admin, Sales, Finance, User), Stripe payment processing, WhatsApp notifications, QR code generation for guest check-in, Cloudinary image uploads, Redis caching, and ML-powered menu recommendations.

---

## ✨ Features

- **Authentication & Authorization** — JWT-based auth with role-based access control (Admin, Sales, Finance, User)
- **Event Management** — Full CRUD for banquet events with detailed event models
- **Guest Management** — Guest profiles, QR code check-in scanning, and entry tracking
- **Menu Management** — Dynamic menu creation with ML-powered recommendations
- **Payment Processing** — Stripe integration for online payments with success handling
- **Venue Management** — Venue creation and assignment to events
- **WhatsApp Notifications** — Automated WhatsApp messaging for event updates
- **QR Code Generation** — Auto-generated QR codes for guest check-in stored in `/backend/qr_codes/`
- **Cloudinary Integration** — Image upload and management via Cloudinary
- **Redis Caching** — Performance layer using Redis
- **Audit Logs** — Full audit trail of system actions
- **Real-time WebSocket Server** — Live updates via `ws-server.js`
- **Role-based Dashboards** — Separate dashboard views for Admin, Sales, Finance, and regular Users
- **Operational Synergy AI** — GenAI-powered service for cross-department operational recommendations
- **ML Menu Recommendations** — Trained scikit-learn model (`menu_model.pkl`) for intelligent menu suggestions

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React 18, Vite, Zustand, Axios |
| Backend | Node.js, Express.js |
| Database | MongoDB (via Mongoose) |
| Cache | Redis |
| Payments | Stripe |
| Media | Cloudinary |
| Messaging | WhatsApp API |
| AI / ML Service | Python, FastAPI / Flask |
| ML Model | scikit-learn (`.pkl`) |
| GenAI | Google Generative AI |
| Real-time | WebSockets |
| Auth | JWT |

---

## 📁 Project Structure

```
Banquet-IntelliManager/
│
├── .vscode/
│   └── settings.json                  # Editor workspace settings
│
├── backend/                           # Node.js Express API server
│   ├── server.js                      # Main Express app entry point
│   ├── ws-server.js                   # WebSocket server for real-time updates
│   ├── package.json
│   │
│   ├── config/
│   │   ├── db.js                      # MongoDB connection setup
│   │   ├── cloudinary.js              # Cloudinary SDK configuration
│   │   ├── redis.js                   # Redis client configuration
│   │   └── stripe.js                  # Stripe SDK configuration
│   │
│   ├── consts/
│   │   ├── menuOptions.js             # Predefined menu option constants
│   │   └── Tier_Pricing.js            # Pricing tier definitions (WIP)
│   │
│   ├── controllers/
│   │   ├── authController.js          # Register, login, logout logic
│   │   ├── eventController.js         # Event CRUD operations
│   │   ├── guestController.js         # Guest management logic
│   │   ├── menuController.js          # Menu creation and management
│   │   ├── paymentController.js       # Stripe payment intent & webhook handling
│   │   ├── venueController.js         # Venue CRUD
│   │   ├── qrController.js            # QR code generation for guest check-in
│   │   ├── whatsappController.js      # WhatsApp message sending
│   │   └── brownieController.js       # Brownie points / loyalty logic
│   │
│   ├── middlewares/
│   │   └── authMiddleware.js          # JWT verification & role-based access guard
│   │
│   ├── models/
│   │   ├── userModel.js               # User schema (name, email, role, password)
│   │   ├── eventModel.js              # Event schema (date, venue, guests, menu, status)
│   │   ├── guestModel.js              # Guest schema (name, contact, check-in status)
│   │   ├── menuModel.js               # Menu schema (items, categories, pricing)
│   │   ├── paymentModel.js            # Payment schema (amount, status, Stripe IDs)
│   │   ├── venueModel.js              # Venue schema (name, capacity, location)
│   │   ├── notificationModel.js       # Notification schema for in-app alerts
│   │   ├── auditLog.js                # Audit log schema (who did what and when)
│   │   └── brownieModel.js            # Brownie points / reward tracking schema
│   │
│   ├── routes/
│   │   ├── authRoute.js               # POST /register, POST /login, POST /logout
│   │   ├── eventRoutes.js             # GET/POST/PUT/DELETE /events
│   │   ├── guestRoutes.js             # GET/POST /guests
│   │   ├── menuRoutes.js              # GET/POST /menu
│   │   ├── paymentRoute.js            # POST /payment/create-intent, /webhook
│   │   ├── venueRoutes.js             # GET/POST/PUT/DELETE /venues
│   │   ├── qrRoute.js                 # GET /qr/:guestId
│   │   ├── whatsappRoute.js           # POST /whatsapp/send
│   │   └── brownieRoutes.js           # GET/POST /brownie
│   │
│   ├── services/
│   │   └── qrservice.js               # QR code generation logic (uses qrcode library)
│   │
│   ├── utils/
│   │   └── encrypt.js                 # Password hashing / encryption helpers
│   │
│   └── qr_codes/                      # Generated QR code images stored here
│       └── qr_1774426204503.png
│
├── fastapi/                           # Python AI/ML microservices
│   │
│   ├── MenuRecomm_Model/              # Menu Recommendation ML Model
│   │   ├── train_model.py             # Training script for the recommendation model
│   │   ├── ml_api.py                  # FastAPI endpoint that serves the model
│   │   ├── menu_model.pkl             # Trained scikit-learn model (serialized)
│   │   ├── menu_ml_dataset.json       # Training dataset (66KB)
│   │   └── menuItems_balanced_counts.json  # Balanced item frequency data
│   │
│   └── OperationalSynergy_Model/      # Operational Synergy AI Service
│       └── operational_synergy/
│           └── flask-backend/         # Flask microservice
│               ├── app.py             # Flask app entry point
│               ├── requirements.txt
│               ├── models/
│               │   └── db.py          # Database connection for Flask service
│               ├── routes/
│               │   ├── synergy.py     # Synergy analysis API routes
│               │   ├── auth.py        # Auth routes (WIP)
│               │   └── event.py       # Event routes (WIP)
│               └── services/
│                   ├── genai_service.py     # Google GenAI integration for AI insights
│                   └── synergy_engine.py    # Core logic for operational synergy scoring
│
└── frontend/                          # React + Vite SPA
    ├── index.html                     # HTML entry shell
    ├── vite.config.js                 # Vite bundler configuration
    ├── eslint.config.js               # ESLint rules
    ├── package.json
    │
    ├── public/
    │   ├── favicon.svg                # App favicon
    │   └── icons.svg                  # SVG icon sprite
    │
    └── src/
        ├── main.jsx                   # React app bootstrap / ReactDOM.render
        ├── App.jsx                    # Root component
        ├── App.css                    # Global styles
        ├── index.css                  # Base CSS / Tailwind imports
        ├── Routes.jsx                 # App-wide route definitions (React Router)
        ├── ProtectRoute.jsx           # Auth guard HOC for protected routes
        │
        ├── assets/
        │   ├── hero.png               # Landing page hero image
        │   ├── react.svg
        │   └── vite.svg
        │
        ├── components/
        │   ├── Navbar.jsx             # Top navigation bar
        │   └── createEventModal.jsx   # Modal form for creating a new event
        │
        ├── pages/
        │   ├── Home.jsx               # Public landing page
        │   ├── Login.jsx              # Login page
        │   ├── Register.jsx           # Registration / signup page
        │   ├── Dashboard.jsx          # Dashboard shell / role-based router
        │   ├── Loading.jsx            # Loading spinner screen
        │   ├── NotFound.jsx           # 404 page
        │   ├── Payment.jsx            # Payment initiation page
        │   ├── PaymentSuccess.jsx     # Post-payment success confirmation screen
        │   ├── AuditLogs.jsx          # Audit log viewer
        │   ├── CloudinaryUpload.jsx   # Image upload interface (Cloudinary)
        │   │
        │   ├── DashboardPages/
        │   │   ├── adminDashboard.jsx     # Admin overview & management dashboard
        │   │   ├── salesDashboard.jsx     # Sales pipeline & metrics (largest page at 15KB)
        │   │   ├── financeDashboard.jsx   # Finance & revenue dashboard
        │   │   └── userDashboard.jsx      # Standard user event view
        │   │
        │   └── EventPages/
        │       ├── EventDetail.jsx    # Single event detail view (18KB)
        │       ├── GuestEntry.jsx     # Guest check-in & QR scanning interface (43KB — largest file)
        │       └── Menu.jsx           # Event menu viewer with ML recommendations (33KB)
        │
        ├── stores/                    # Zustand global state stores
        │   ├── useAuthStore.js        # Auth state (user, token, login/logout actions)
        │   ├── useEventStore.js       # Event state (WIP)
        │   └── useVenueStore.js       # Venue list state
        │
        ├── services/
        │   └── eventService.js        # Axios wrapper for event API calls
        │
        ├── lib/
        │   ├── axios.js               # Axios instance with base URL & interceptors
        │   ├── cloudinary.js          # Cloudinary upload helper functions
        │   └── utils.js               # Shared utility/helper functions
        │
        └── data/
            └── events.js              # Static/mock event data for development
```

---

## 🚀 Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) v18+
- [Python](https://www.python.org/) v3.10+
- [MongoDB](https://www.mongodb.com/) (local or Atlas)
- [Redis](https://redis.io/)
- A [Stripe](https://stripe.com/) account
- A [Cloudinary](https://cloudinary.com/) account
- A [Google AI](https://ai.google.dev/) API key (for the GenAI synergy service)

---

### Environment Variables

Create a `.env` file inside `backend/`:

```env
PORT=5000
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret
REDIS_URL=your_redis_url

STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_WEBHOOK_SECRET=your_stripe_webhook_secret

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret

WHATSAPP_API_KEY=your_whatsapp_api_key
```

Create a `.env` inside `frontend/`:

```env
VITE_API_BASE_URL=http://localhost:5000
VITE_CLOUDINARY_CLOUD_NAME=your_cloud_name
VITE_CLOUDINARY_UPLOAD_PRESET=your_upload_preset
```

---

### Installation & Running

**1. Clone the repo**
```bash
git clone https://github.com/bhaumik694/Banquet-IntelliManager.git
cd Banquet-IntelliManager
```

**2. Backend**
```bash
cd backend
npm install
node server.js
```
WebSocket server (separate terminal):
```bash
node ws-server.js
```

**3. Frontend**
```bash
cd frontend
npm install
npm run dev
```

**4. Menu Recommendation — FastAPI** (port 8001)
```bash
cd fastapi/MenuRecomm_Model
pip install fastapi uvicorn scikit-learn
uvicorn ml_api:app --reload --port 8001
```

**5. Operational Synergy — Flask** (port 5001)
```bash
cd fastapi/OperationalSynergy_Model/operational_synergy/flask-backend
pip install flask google-generativeai pymongo
python app.py
```


## 🤖 ML Models

### Menu Recommendation (`fastapi/MenuRecomm_Model/`)
- **`train_model.py`** — Trains a scikit-learn classifier on `menu_ml_dataset.json` and saves it as `menu_model.pkl`
- **`ml_api.py`** — Serves the model via a FastAPI endpoint; accepts event parameters and returns menu item recommendations
- **Dataset** — `menu_ml_dataset.json` (66KB) with class-balanced item frequency data in `menuItems_balanced_counts.json`

To retrain the model:
```bash
python train_model.py
```

### Operational Synergy (`fastapi/OperationalSynergy_Model/`)
- **`synergy_engine.py`** — Scores and identifies operational synergies across departments (sales, ops, finance)
- **`genai_service.py`** — Wraps Google Generative AI to produce natural-language operational insight reports
- **`routes/synergy.py`** — Exposes the synergy analysis as a REST endpoint

---

