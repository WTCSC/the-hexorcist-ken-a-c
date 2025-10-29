<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hexorcist — Base Converter</title>
</head>
<body>
    <h1>Hexorcist — Base Converter</h1>
    
    <p>A simple program that converts numbers between any two bases (2–36) <strong>without using built-in Python base conversion</strong>. Perfect for learning how numbers really work!</p>
    
    <h2>How It Works</h2>
    <ul>
        <li><strong>Step 1:</strong> Convert the input number to decimal using a "decoder ring" (0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ).</li>
        <li><strong>Step 2:</strong> Convert the decimal number to the target base using division and remainders.</li>
    </ul>
    
    <h2>Usage</h2>
    <ol>
        <li>Run the program: <code>python hexorcist.py</code></li>
        <li>Enter the number to convert, its current base, and the target base.</li>
        <li>The program will display the converted number.</li>
    </ol>
    
    <h2>Rules</h2>
    <p>No <code>bin()</code>, <code>hex()</code>, <code>oct()</code>, <code>format()</code>, or <code>int(..., base)</code> allowed. Only loops, math, a
