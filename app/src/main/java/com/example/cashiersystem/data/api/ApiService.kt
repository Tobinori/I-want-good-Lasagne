package com.example.cashiersystem.data.api

import com.example.cashiersystem.data.model.*
import retrofit2.Response
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.http.Path

interface ApiService {

    // 🏢 Get all restaurants
    @GET("api/restaurants/")
    suspend fun getRestaurants(): Response<List<Restaurant>>

    // 🍽️ Get dishes for a restaurant
    @GET("api/dishes/")
    suspend fun getDishes(): Response<List<Dish>>

    // 🛒 Place an order
    @POST("api/orders/")
    suspend fun createOrder(@Body order: OrderRequest): Response<OrderRequest>
}
