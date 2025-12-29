# Project File Structure

## Root Directory
```
WorkingSpace/
├── CHANGELOG.md                   # Project changelog
├── DIAGRAMS.md                    # Project diagrams documentation
├── ERD.md                         # Entity Relationship Diagram documentation
├── FILE_STRUCTURE.md              # This file - project structure documentation
├── requirements.txt               # Python dependencies
├── myenv/                         # Python virtual environment
└── studyapp/                      # Main Django project
```

## Django Project Structure (studyapp/)

```
studyapp/
├── manage.py                      # Django management script
│
├── studyapp/                      # Main project configuration
│   ├── __init__.py
│   ├── __pycache__/
│   ├── asgi.py                    # ASGI configuration
│   ├── settings.py                # Django settings
│   ├── urls.py                    # Main URL configuration
│   └── wsgi.py                    # WSGI configuration
│
├── account/                       # Account management app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── announcement/                  # Announcements app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── exam/                          # Exam management app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── homework/                      # Homework management app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── invoice/                       # Invoice management app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── meeting/                       # Meeting management app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── messages/                      # Messaging app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── preSigninMessages/             # Pre-signin messages app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── study/                         # Study management app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── thread/                        # Thread management app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── todo/                          # Todo/Task management app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── writing/                       # Writing services app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── templates/                     # HTML templates
│   ├── home.html
│   │
│   ├── admin/                     # Admin panel templates (19 files)
│   │   ├── admin_base.html
│   │   ├── add_cs_rep.html
│   │   ├── add_teacher.html
│   │   ├── analytics.html
│   │   ├── announcements.html
│   │   ├── assignment_requests.html
│   │   ├── content_review.html
│   │   ├── csrepcredentials.html
│   │   ├── dashboard.html
│   │   ├── feedback_report.html
│   │   ├── financial_reporting.html
│   │   ├── invoices.html
│   │   ├── messages.html
│   │   ├── notifications.html
│   │   ├── profile_settings.html
│   │   ├── profile.html
│   │   ├── student_management.html
│   │   ├── threads.html
│   │   └── user_management.html
│   │
│   ├── csrep/                     # Customer Service Rep templates (11 files)
│   │   ├── announcement.html
│   │   ├── assigned_teacher.html
│   │   ├── communication.html
│   │   ├── csrep_base.html
│   │   ├── invoice_management.html
│   │   ├── notifications.html
│   │   ├── overview.html
│   │   ├── payment.html
│   │   ├── pre_sign_in_chat.html
│   │   ├── profile.html
│   │   └── threads.html
│   │
│   ├── login/                     # Authentication templates
│   │   ├── forgot_pass.html
│   │   ├── login.html
│   │   ├── registration.html
│   │   └── reset_pass_cnfrm.html
│   │
│   ├── meetings/                  # Meeting templates (2 files)
│   │
│   ├── student/                   # Student templates (22 files)
│   │
│   └── teacher/                   # Teacher templates (16 files)
│
└── public/                        # Public static files
    ├── pics/                      # Image files
    │   ├── how_it_work.png
    │   ├── online_assignment.png
    │   ├── periodic_academic_support.png
    │   ├── Portal_management.png
    │   ├── Student_Friendly Prices.png
    │   ├── Subject_expertise.png
    │   ├── subject_specific_help.png
    │   ├── tailored_study_companion.png
    │   ├── Timely_submitions.png
    │   ├── tutor1.png
    │   ├── tutor2.png
    │   ├── tutor3.png
    │   ├── tutor4.png
    │   └── why_choos.png
    │
    ├── PNGs/                      # PNG images directory
    │
    ├── static/                    # Static assets
    │   ├── css/                   # Stylesheets (9 files)
    │   └── java/                  # JavaScript files (23 files)
    │
    └── SVGs/                      # SVG graphics
        ├── arrow.svg
        ├── bigdotleft.svg
        ├── bigdotright.svg
        ├── bluedot.svg
        ├── clipboard.svg
        ├── cross.svg
        ├── email.svg
        ├── facebook.svg
        ├── float_button.svg
        ├── gps.svg
        ├── grids.svg
        ├── How_it_work_grid.svg
        ├── line.svg
        ├── linkedIn.svg
        ├── logo.svg
        ├── message.svg
        ├── pc.svg
        ├── phone.svg
        ├── progress.svg
        ├── rectangle1.svg
        ├── report.svg
        ├── resource_cap.svg
        ├── resource_clip_pencil.svg
        ├── resource_person.svg
        ├── resource_text_file.svg
        ├── search.svg
        ├── search2.svg
        ├── seprator.svg
        ├── student.png
        ├── tutor.png
        ├── user.svg
        ├── whatsapp.svg
        ├── yellowbigdot.svg
        └── yellowdot.svg
```

## Django Apps Summary

The project consists of **12 Django apps**:

1. **account** - User account management
2. **announcement** - Announcements system
3. **exam** - Exam management
4. **homework** - Homework/assignment management
5. **invoice** - Invoice and billing
6. **meeting** - Meeting scheduling and management
7. **messages** - Messaging system
8. **preSigninMessages** - Pre-signin messages management
9. **study** - Study materials and resources
10. **thread** - Discussion threads
11. **todo** - Task/todo management
12. **writing** - Writing services

## Dependencies

From `requirements.txt`:
- django
- djangorestframework

## Template Structure

- **Admin templates**: 19 files for admin panel functionality
- **CS Rep templates**: 11 files for customer service representatives
- **Student templates**: 22 files for student interface
- **Teacher templates**: 16 files for teacher interface
- **Login templates**: 4 files for authentication
- **Meeting templates**: 2 files
- **Home template**: 1 file

## Static Assets

- **CSS files**: 9 stylesheets
- **JavaScript files**: 23 scripts
- **Images**: Multiple PNG and SVG files for UI elements

