# Nano Problem - Development Roadmap

This document outlines the remaining development tasks for the Nano Problem platform, based on the `ERD.md` and `DIAGRAMS.md` specifications.

---

## 📋 Phase 0: Foundations (COMPLETED)
*   **Account App**: Custom User model, Role-based auth (Student, Teacher, CS Rep, Admin).
*   **Profile Management**: Dynamic profiles for all roles with automatic ID generation.
*   **Dashboard Framework**: Dynamic section loading (AJAX) for Admin, Teacher, CS Rep, and Student.
*   **User Management**: Admin tools to block/unblock users and reset passwords with real database data.
*   **Logout Redirection**: Secure POST-based logout with role-based routing.

---

## 🚀 Phase 1: Assignment & Workflow Engine (PostgreSQL Focus)
*Goal: Implement the core business logic of requesting and assigning work.*

1.  **Assignments App Implementation**: 
    *   Create models: `ASSIGNMENTS`, `ASSIGNMENT_FILES`.
    *   **Student Flow**: "Request New Assignment" form with file uploads.
    *   **Student Tracker**: Dashboard view to see the status of all requests.
2.  **Teacher Assignment Logic**:
    *   Create models: `TEACHER_ASSIGNMENTS`.
    *   **Admin/CS Rep Tool**: Functional section to assign primary/helper teachers to assignments.
    *   **Teacher View**: "My Assignments" section to view and accept pending tasks.
3.  **Specialized Service Modules**:
    *   Implement models/views for **Writing**, **Homework**, and **Exam** apps.
    *   **Teacher Delivery**: Specific portals for teachers to submit completed papers, solutions, or exam results.

---

## 💰 Phase 2: Invoicing & Billing System (PostgreSQL Focus)
*Goal: Monetize the platform and handle financial transactions.*

1.  **Invoices Module**:
    *   Create models: `INVOICES`.
    *   **CS Rep Tool**: Form to generate invoices linked to specific assignments.
    *   **Admin Tool**: Approval workflow for generated invoices.
2.  **Payments Integration**:
    *   Create models: `PAYMENTS`.
    *   **Student View**: "Pay Now" buttons and complete transaction history.
    *   **External Integration**: Connect with Stripe/PayPal API for real transactions.

---

## 💬 Phase 3: Database-Driven Communication (PostgreSQL Focus)
*Goal: Build the structure for messaging and support without real-time yet.*

1.  **Threaded Messaging**:
    *   Create models: `THREADS`, `THREAD_PARTICIPANTS`, `MESSAGES`, `MESSAGE_ATTACHMENTS`.
    *   **Inbox UI**: Build the interface for users to communicate (using AJAX polling).
2.  **Pre-Sign-In Chat (Lead Conversion)**:
    *   Create models: `PRE_SIGNIN_SESSIONS`, `PRE_SIGNIN_MESSAGES`.
    *   **Visitor Widget**: Functional chat on the Home page that saves messages to the DB.
    *   **CS Rep View**: Section to respond to visitors and convert them to registered students.

---

## 🛠️ Phase 4: Support & Utilities (PostgreSQL Focus)

1.  **Meetings Module**:
    *   Create models: `MEETINGS`, `MEETING_PARTICIPANTS`.
    *   **Scheduling**: Logic for teachers/students to schedule 1-on-1 tutoring sessions.
2.  **Notifications & Announcements**:
    *   **Site-wide Announcements**: Admin interface to push updates to all users.
    *   **User Notifications**: Database-driven alert system for new messages, assignments, or invoices.
3.  **Audit Logs**:
    *   Implement `AUDIT_LOGS` to track critical administrative actions for accountability.

---

## ⚡ Phase 5: Real-Time Layer (Django Channels + Redis)
*Goal: Upgrade the platform to be instant and interactive.*

1.  **Instant Messaging**: Upgrade the Messages app to use WebSockets for no-latency chat.
2.  **Live Notifications**: Implement push-style notifications that appear without page refreshes.
3.  **Live Visitor Chat**: Upgrade Pre-Sign-In chat to be truly real-time for immediate conversion.
4.  **Meeting Signaling**: Use Channels for signaling in audio/video tutoring sessions.

---

## 🛠️ Module Mapping Summary

| Module | Core Data (PostgreSQL) | Real-Time (Channels) |
| :--- | :--- | :--- |
| **Assignments** | ✅ Models, Uploads, Status | ❌ (Not Required) |
| **Invoices** | ✅ Billing, Approvals | ❌ (Not Required) |
| **Messaging** | ✅ Threads, Message History | 🔄 Real-time Upgrade |
| **Pre-Sign-In** | ✅ Lead Capture, History | 🔄 Live Support Upgrade |
| **Meetings** | ✅ Scheduling, Logins | 🔄 Signaling Upgrade |
| **Notifications** | ✅ History, Badges | 🔄 Push Alerts Upgrade |

---
*Roadmap generated on: 2025-12-22*

