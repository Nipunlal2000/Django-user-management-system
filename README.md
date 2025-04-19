# 🚀 Retool Admin Dashboard
![🌐 Landing Page](Screenshot%204.png)

# 👥 Group Views
## 🛡️ Admin 
### (superuser | can add, view, edit, delete, and ban users and mods)
![🔒 Admin View](Screenshot%201.png)

## 🛠️ Moderator 
### (can add, view, edit, and delete other users' posts)
![📝 Moderator View](Screenshot%202.png)

## 🙋 Default User 
### (can add and view posts)
![📄 User View](Screenshot%203.png)

# 🚀 User Management System

This user management system is developed using:
- **Python**: For backend logic and framework support.
- **Django**: As the web framework for rapid development, user authentication, and permission handling.
- **PostgreSQL**: For efficient data storage and retrieval.
- **Supabase.com**: Hosting the PostgreSQL database publicly, replacing pgAdmin's private hosting.
- **Retool.com**: Customizable admin dashboard creation with interactive charts and query execution by linking the Supabase-hosted database with Django.

---

## 🛠️ System Functionality

This system provides comprehensive **user management** and post creation functionality, leveraging role-based access control across three distinct user groups:

### 🙋 Default Users
- **Permissions**:
  - Can create and view posts.
- **Role**:
  - Designed for regular users to interact with content.

### 🛠️ Moderators
- **Permissions**:
  - Can create, view, edit, and delete posts created by other users.
- **Role**:
  - Responsible for content moderation to ensure platform integrity.

### 🛡️ Admins (Superusers)
- **Permissions**:
  - Can add, view, edit, delete, and ban users (including moderators).
  - Has full control over user policies and website management.
- **Role**:
  - Oversees all operations and ensures seamless management of the platform.

---

## 📊 Interactive Dashboard

The system integrates **Retool.com** for a fully customizable admin dashboard:
1. **Visual Insights**:
   - Admins can monitor user activity, posts, and statistics through interactive charts.
2. **SQL Query Execution**:
   - Admins can write and execute custom SQL queries by connecting the Supabase database directly to Retool.
3. **Enhanced Workflow**:
   - Simplifies data management and provides a user-friendly interface for administrative tasks.

---

### 🚀 Deployment
The application is deployed using:
- **Django**: For secure and scalable backend operations.
- **Supabase.com**: Public hosting of the PostgreSQL database.
- **Retool.com**: For real-time data visualization and query management.

This user management system is ideal for forums, social platforms, and tools requiring role-based access control and dynamic user permissions.
