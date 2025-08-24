# 📘 Project Euler Solutions (in Python)

Welcome to my repository of Project Euler solutions 🎯  
Each solution is written in Python and formatted in **HackerRank-style (input/output ready)**.

<p align="left">
  <a href="#-overview">Overview</a> •
  <a href="#-problems-2–10">Problems 2–10</a> •
  <a href="#-how-to-run">How to Run</a> •
  <a href="#-progress-tracker">Progress Tracker</a> •
  <a href="#-contributing">Contributing</a>
</p>

---

## 📂 Table of Contents
- [🌟 Overview](#-overview)
- [🔢 Problems 2–10](#-problems-2–10)
  - [🚀 Problem 2 — Even Fibonacci Numbers](#-problem-2-even-fibonacci-numbers)
  - [🔍 Problem 3 — Largest Prime Factor](#-problem-3-largest-prime-factor)
  - [🔢 Problem 4 — Largest Palindrome Product](#-problem-4-largest-palindrome-product)
  - [📏 Problem 5 — Smallest Multiple](#-problem-5-smallest-multiple)
  - [🧮 Problem 6 — Sum Square Difference](#-problem-6-sum-square-difference)
  - [🔑 Problem 7 — 10001st Prime](#-problem-7-10001st-prime)
  - [📊 Problem 8 — Largest Product in a Series](#-problem-8-largest-product-in-a-series)
  - [📐 Problem 9 — Special Pythagorean Triplet](#-problem-9-special-pythagorean-triplet)
  - [🔢 Problem 10 — Summation of Primes](#-problem-10-summation-of-primes)
- [🎯 How to Run](#-how-to-run)
- [🏆 Progress Tracker](#-progress-tracker)
- [🤝 Contributing](#-contributing)

---

## 🌟 Overview

This repo contains my Python solutions for **Project Euler problems #2 to #10**.  
Each problem is solved with:

- ✅ **Efficient algorithm**
- ✅ **HackerRank-style input/output**
- ✅ **Clean & readable code**

> **Note:** All scripts read from `stdin` and print to `stdout`, making them drop-in friendly for coding platforms.

---

## 🔢 Problems 2–10

### 🚀 Problem 2: Even Fibonacci Numbers
**Task:** Find the sum of even Fibonacci numbers ≤ `N`.  
**I/O:** Input: integer `N` • Output: sum (integer)  
**👉 Go to Solution:** [`problems/problem2.py`](problems/problem2.py)

---

### 🔍 Problem 3: Largest Prime Factor
**Task:** Find the largest prime factor of `N`.  
**I/O:** Input: integer `N` • Output: largest prime factor (integer)  
**👉 Go to Solution:** [`problems/problem3.py`](problems/problem3.py)

---

### 🔢 Problem 4: Largest Palindrome Product
**Task:** Find the largest palindrome product of two 3-digit numbers ≤ `N`.  
**I/O:** Input: integer `N` (max factor) • Output: largest palindrome (integer)  
**👉 Go to Solution:** [`problems/problem4.py`](problems/problem4.py)

---

### 📏 Problem 5: Smallest Multiple
**Task:** Find the smallest number evenly divisible by all numbers from `1` to `N`.  
**I/O:** Input: integer `N` • Output: LCM from `1..N` (integer)  
**👉 Go to Solution:** [`problems/problem5.py`](problems/problem5.py)

---

### 🧮 Problem 6: Sum Square Difference
**Task:** Difference between the square of the sum and the sum of the squares of the first `N` natural numbers.  
**I/O:** Input: integer `N` • Output: difference (integer)  
**👉 Go to Solution:** [`problems/problem6.py`](problems/problem6.py)

---

### 🔑 Problem 7: 10001st Prime
**Task:** Find the `N`-th prime number.  
**I/O:** Input: integer `N` • Output: `N`-th prime (integer)  
**👉 Go to Solution:** [`problems/problem7.py`](problems/problem7.py)

---

### 📊 Problem 8: Largest Product in a Series
**Task:** Find the largest product of `K` consecutive digits in a given numeric string.  
**I/O:**  
- Line 1: two integers `L K` (length and window size)  
- Line 2: numeric string of length `L`  
**Output:** maximum product (integer)  
**👉 Go to Solution:** [`problems/problem8.py`](problems/problem8.py)

---

### 📐 Problem 9: Special Pythagorean Triplet
**Task:** Find the **largest product** `a*b*c` where `a + b + c = N` and `a² + b² = c²`.  
**I/O:** Input: integer `N` • Output: maximum product `abc` (integer), or `-1` if none  
**👉 Go to Solution:** [`problems/problem9.py`](problems/problem9.py)

---

### 🔢 Problem 10: Summation of Primes
**Task:** Find the sum of all primes ≤ `N`.  
**I/O:** Input: integer `N` • Output: sum (integer)  
**👉 Go to Solution:** [`problems/problem10.py`](problems/problem10.py)

---

## 🎯 How to Run

```bash
# Clone repository
git clone https://github.com/your-username/project-euler-python.git
cd project-euler-python

# (Optional) Create virtual environment
python3 -m venv .venv && source .venv/bin/activate

# Run any problem (example: Problem 3)
python3 problems/problem3.py < input.txt
# or interactively
python3 problems/problem3.py
