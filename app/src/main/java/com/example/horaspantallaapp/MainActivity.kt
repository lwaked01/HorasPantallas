package com.example.horaspantallaapp

import android.os.Bundle
import android.webkit.WebChromeClient
import android.webkit.WebView
import android.webkit.WebViewClient
import android.widget.LinearLayout
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.viewinterop.AndroidView
import com.example.horaspantallaapp.ui.theme.HorasPantallaAppTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            HorasPantallaAppTheme {
                WebPage(url = "https://horaspantallas-lwg.streamlit.app/")
            }
        }
    }
}

@Composable
fun WebPage(url: String) {
    AndroidView(
        modifier = Modifier.fillMaxSize(),
        factory = { context ->
            WebView(context).apply {
                webViewClient = WebViewClient()
                webChromeClient = WebChromeClient() // Soporte JS avanzado

                settings.javaScriptEnabled = true
                settings.domStorageEnabled = true // Habilita localStorage
                settings.databaseEnabled = true // Habilita WebSQL (algunos sitios lo usan)

                settings.loadWithOverviewMode = true
                settings.useWideViewPort = true

                loadUrl(url)
                layoutParams = LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.MATCH_PARENT,
                    LinearLayout.LayoutParams.MATCH_PARENT
                )
            }
        }
    )
}
