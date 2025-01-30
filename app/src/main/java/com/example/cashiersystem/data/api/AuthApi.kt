package com.example.cashiersystem.data.api

import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.POST

data class LoginRequest(val username: String, val password: String)
data class LoginResponse(val tokens: Tokens)

data class Tokens(val refresh: String, val access: String)

interface AuthApi {
    @POST("login/")
    fun login(@Body request: LoginRequest): Call<LoginResponse>
}
