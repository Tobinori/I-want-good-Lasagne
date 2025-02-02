// OrderRequest.kt
package com.example.cashiersystem.data.model

data class OrderRequest(
    val user: Int,
    val restaurant: Int,
    val items: List<OrderItem>
)

data class OrderItem(
    val dish: Int,
    val amount: Int
)
