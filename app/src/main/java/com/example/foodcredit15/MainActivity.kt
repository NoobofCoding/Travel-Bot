package com.example.foodcredit15

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.foodcredit15.ui.screens.AccountTypeScreen
import com.example.foodcredit15.ui.screens.UserLoginScreen
import com.example.foodcredit15.ui.screens.EmployeeLoginScreen

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                Surface(color = MaterialTheme.colorScheme.background) {
                    val navController = rememberNavController()
                    NavHost(
                        navController = navController,
                        startDestination = "accountType"
                    ) {
                        composable("accountType") {
                            AccountTypeScreen(navController)
                        }
                        composable("userLogin") {
                            UserLoginScreen(navController)
                        }
                        composable("employeeLogin") {
                            EmployeeLoginScreen(navController)
                        }
                    }
                }
            }
        }
    }
}
