package com.example.foodcredit15.ui.theme

import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val LightColors = lightColorScheme(
    primary = Color(0xFF4CAF50),
    onPrimary = Color.White,
    secondary = Color(0xFF8BC34A),
    onSecondary = Color.Black,
    background = Color(0xFFF1F8E9),
    onBackground = Color.Black,
    surface = Color.White,
    onSurface = Color.Black
)

private val DarkColors = darkColorScheme(
    primary = Color(0xFF81C784),
    onPrimary = Color.Black,
    secondary = Color(0xFF558B2F),
    onSecondary = Color.White,
    background = Color(0xFF2E7D32),
    onBackground = Color.White,
    surface = Color(0xFF1B5E20),
    onSurface = Color.White
)

@Composable
fun FoodCreditTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit
) {
    val colors = if (darkTheme) DarkColors else LightColors

    MaterialTheme(
        colorScheme = colors,
        typography = Typography(), // You can customize if needed
        content = content
    )
}
