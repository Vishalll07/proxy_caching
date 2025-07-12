# 🔄 Proxy Caching Server CLI

A lightweight Python-based HTTP proxy server that caches GET requests using an in-memory store with optional TTL (time-to-live) and persistent file caching.

👉 Listed on [roadmap.sh/projects/caching-server](https://roadmap.sh/projects/caching-server)

---

## 🚀 Features

- 🔁 **Proxy Server**: Forwards requests to any origin URL
- 🧠 **In-Memory Caching**: Stores response data to serve repeated requests faster
- ⏳ **TTL Support**: Automatically expires cache after a fixed time (default: 60 seconds)
- 💾 **Persistent Disk Caching**: Stores cache in `cache.json` file for reuse on restart
- 🧼 **Clear Cache Command**: CLI command to clear the cache anytime
- 🧪 **Custom Headers**: Returns `X-Cache: HIT` or `X-Cache: MISS` for debugging

---

## 📦 Usage

### 🔹 Start the Proxy Server

```bash
python proxy.py start --port 3000 --origin http://dummyjson.com


## 📁 Project Structure

```
proxy_caching/
├── proxy.py          # Main script
├── cache.json        # Stores cached responses
├── README.md         # Documentation
```
---

## 🛠 Install Dependencies
```bash
pip install flask click requests httpie
```
---
## 🧪 Usage
### ➤ Start the server
```bash
python proxy.py start --port 3000 --origin http://dummyjson.com
```
Then test it:
```bash
http http://localhost:3000/products
```
### ➤ Clear cache
```bash
python proxy.py clear-cache
```
---
## 📌 Example Headers
For cache hits:
```
X-Cache: HIT
```
For cache misses:
```
X-Cache: MISS
## 🧹 Future Plans

- [ ] Add support for more HTTP methods
- [ ] Add LRU eviction
- [ ] Add Docker support
- [ ] Add logging & test cases
