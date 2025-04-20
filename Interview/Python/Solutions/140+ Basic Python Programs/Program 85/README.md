
# 🗜️ Program 85: Compress and Decompress a String

This Python program demonstrates how to **compress** and **decompress** a string using the built-in `zlib` module.

---

## 📌 Problem Statement

Write a Python program to **compress** and **decompress** the following string:

```

"hello world!hello world!hello world!hello world!"

```

---

## 🧠 Concepts Used

- `zlib` module for compression and decompression
- `encode()` and `decode()` methods for string handling

---

## 🧪 Sample Code

```python
import zlib

# Original string
text = "hello world!hello world!hello world!hello world!"
print("Original string:")
print(text)

# Compression
compressed_text = zlib.compress(text.encode('utf-8'))
print("\nCompressed string:")
print(compressed_text)

# Decompression
decompressed_text = zlib.decompress(compressed_text).decode('utf-8')
print("\nDecompressed string:")
print(decompressed_text)
```

---

## 🎯 Output (Example)

```
Original string:
hello world!hello world!hello world!hello world!

Compressed string:
b'x\x9c\xf3H\xcd\xc9\xc9\xd7Q(\xcf/\xcaIQ\xcc \x82\r\x00\xbd[\x11\xf5'

Decompressed string:
hello world!hello world!hello world!hello world!
```

---

## 🧠 Notes

- `zlib` is useful for handling data compression in Python.
- Always use `.encode()` when compressing and `.decode()` when decompressing strings.

---
