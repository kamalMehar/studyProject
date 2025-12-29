# Test Users Credentials

## How to Create Test Users

Run the following command to create test users for Admin, Teacher, and CS-Rep:

```bash
python manage.py create_test_users
```

## Temporary Login Credentials

### 🔑 ADMIN USER
- **Role**: Admin
- **User ID (UUID)**: Will be displayed when you run the command
- **Username**: `admin`
- **Password**: `admin123`
- **Email**: `admin@nanoproblem.com`

### 👨‍🏫 TEACHER USER
- **Role**: Teacher
- **User ID (UUID)**: Will be displayed when you run the command
- **Username**: `teacher`
- **Password**: `teacher123`
- **Email**: `teacher@nanoproblem.com`

### 👤 CS-REP USER
- **Role**: CS-Rep
- **User ID (UUID)**: Will be displayed when you run the command
- **Username**: `csrep`
- **Password**: `csrep123`
- **Email**: `csrep@nanoproblem.com`

## Login Instructions

1. Navigate to `/account/login/` in your browser
2. Select the appropriate role from the dropdown (Admin, Teacher, or CS-Rep)
3. Enter either:
   - **User ID (UUID)** - The UUID displayed when you created the users, OR
   - **Username** - `admin`, `teacher`, or `csrep`
4. Enter the password
5. Click "Sign In"

## Notes

- You can use either the UUID or username as the User ID
- The login form sends data to `/account/api/accounts/login/`
- After successful login, users are redirected to their respective dashboards:
  - Admin → `/account/admin-dashboard/`
  - Teacher → `/account/teacher-dashboard/`
  - CS-Rep → `/account/cs-rep-dashboard/`

