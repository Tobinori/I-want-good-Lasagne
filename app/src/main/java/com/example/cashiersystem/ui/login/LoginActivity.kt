package com.example.cashiersystem.ui.login

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.activity.viewModels
import androidx.appcompat.app.AppCompatActivity
import com.example.cashiersystem.R
import com.example.cashiersystem.data.repository.TokenManager

import android.util.Log
import com.example.cashiersystem.ui.orders.OrdersActivity
import com.example.cashiersystem.viewmodel.LoginViewModel

class LoginActivity : AppCompatActivity() {
    private lateinit var loginViewModel: LoginViewModel
    private lateinit var tokenManager: TokenManager

    override fun onCreate(savedInstanceState: Bundle?) {
        class LoginActivity : AppCompatActivity() {
            override fun onCreate(savedInstanceState: Bundle?) {
                super.onCreate(savedInstanceState)
                Log.d("DEBUG", "LoginActivity started")  // Add this line
                setContentView(R.layout.activity_login)
            }
        }
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        loginViewModel = LoginViewModel(applicationContext)
        tokenManager = TokenManager(applicationContext)

        val etUsername = findViewById<EditText>(R.id.etUsername)
        val etPassword = findViewById<EditText>(R.id.etPassword)
        val btnLogin = findViewById<Button>(R.id.btnLogin)

        val savedToken = tokenManager.getToken()
        if (!savedToken.isNullOrEmpty()) {
            Log.d("LoginActivity", "User already logged in with token: $savedToken")
            navigateToOrders()
            return // Exit the function so login fields are not shown
        }

        btnLogin.setOnClickListener {
            val username = etUsername.text.toString()
            val password = etPassword.text.toString()


            loginViewModel.login(username, password) { success ->
                if (success) {
                    Toast.makeText(this, "Login Successful", Toast.LENGTH_SHORT).show()
                    // TODO: Uncomment this after creating OrdersActivity
                    startActivity(Intent(this, OrdersActivity::class.java))
                } else {
                    Toast.makeText(this, "Invalid Credentials", Toast.LENGTH_SHORT).show()
                }
            }
        }


    }
    private fun navigateToOrders() {
        //TODO Uncomment this after creating OrdersActivity
        startActivity(Intent(this, OrdersActivity::class.java))
        finish() // Close the login screen
    }
}
