package com.hamidcognition.main

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        val titleView = findViewById<TextView>(R.id.titleText)
        titleView.text = "HamidCognition Mobile v0.1"
    }
}
