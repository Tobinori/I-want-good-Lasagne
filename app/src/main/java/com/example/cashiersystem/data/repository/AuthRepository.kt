package com.example.cashiersystem.data.repository

import android.content.Context
import android.util.Log
import com.example.cashiersystem.data.api.ApiClient
import com.example.cashiersystem.data.api.AuthApi
import com.example.cashiersystem.data.api.LoginRequest
import com.example.cashiersystem.data.api.LoginResponse
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class AuthRepository(private val context: Context) {
    private val authApi = ApiClient.instance.create(AuthApi::class.java)
    private val tokenManager = TokenManager(context)

    fun login(username: String, password: String, callback: (Boolean) -> Unit) {
        val request = LoginRequest(username, password)

        authApi.login(request).enqueue(object : Callback<LoginResponse> {
            override fun onResponse(call: Call<LoginResponse>, response: Response<LoginResponse>) {
                if (response.isSuccessful) {
                    val token = response.body()?.tokens?.access
                    if (token != null) {
                        tokenManager.saveToken(token)
                        Log.d("AuthRepository", "Token saved: $token")
                    }
                    callback(true)
                } else {
                    val errorBody = response.errorBody()?.string()
                    Log.e("AuthRepository", "Login failed! Error: $errorBody")
                    callback(false)
                }
            }

            override fun onFailure(call: Call<LoginResponse>, t: Throwable) {
                Log.e("AuthRepository", "Login request failed: ${t.message}")
                callback(false)
            }
        })
    }
}
