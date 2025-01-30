package com.example.cashiersystem.viewmodel

import android.content.Context
import androidx.lifecycle.ViewModel
import com.example.cashiersystem.data.repository.AuthRepository

class LoginViewModel(context: Context) : ViewModel() {
    private val authRepository = AuthRepository(context)

    fun login(username: String, password: String, callback: (Boolean) -> Unit) {
        authRepository.login(username, password, callback)

    }
}
