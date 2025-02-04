# 🍽️ **Cashier System**

A modern **cashier system** designed to make the connection between the **kitchen** and the **customer** more **personal**, **direct**, and **efficient**. The project integrates an **Android app** with a **Django REST API** to provide essential tools for restaurant operations while enhancing the customer experience.  

---

## 💡 **Project Idea**

The main goal of this project is to:  
- **Simplify communication** between the kitchen and the customer.  
- Provide **essential features** that every kitchen needs:  
  - **HACCP Management**  
  - **Inventory Tracking**  
  - **Staff Scheduling**  
  - **Menu Planning**  

For **customers**, the app offers a new way to interact with food:  
- **Search for dishes** instead of restaurants, making it easier to find what they crave.  
- **View reviews** on individual dishes to make better dining decisions.  
- **Rate dishes** themselves, with the option to:  
  - **Send private feedback** directly to the kitchen.  
  - **Share public reviews** with other users.  

---

## ✅ **What's Implemented So Far**

### 🔗 **Backend (Django + PostgreSQL)**
- **User Authentication** using JWT (SimpleJWT)  
- Basic CRUD operations for:  
  - **Users & Profiles**  
  - **Restaurants**  
  - **Dishes & Ingredients**  
  - **Orders & Order Items**  
  - **Reviews** (public and private feedback supported)  
- RESTful API endpoints for all key functionalities  
- Admin interface for managing data  

### 📱 **Frontend (Android - Kotlin)**
- **Login System** with token-based authentication  
- API communication setup with **Retrofit**  
- **Order Management:**  
  - View current orders  
  - Create new orders  
- Basic UI for login and order screens  
- Project structure following **MVVM architecture**  

---

## 🚀 **What's Coming Next**

### **Short-Term Goals**  
- **Frontend:**  
  - Add **dish search functionality**  
  - Implement **dish reviews**, including private feedback options  
  - Improve UI for a more intuitive user experience  
  - Connect ordering process directly to kitchen operations  

- **Backend:**  
  - Implement **HACCP management** features  
  - Add modules for **inventory tracking** and **staff scheduling**  
  - Enhance **menu planning** capabilities  
  - Refine permission handling for different user roles (kitchen staff, customers, etc.)  

---

## 🌍 **Future Scope**

- **Advanced Analytics** for kitchens: Insights from customer feedback and operational data  
- **Personalized Recommendations** based on customer preferences and dish reviews  
- **Real-Time Order Updates** between kitchen and customers  
- **Flexible Feedback System:** Options for anonymous reviews and in-depth feedback forms  

---
