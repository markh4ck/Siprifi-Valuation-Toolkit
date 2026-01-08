# Siprifi Valuation Toolkit 🚀

<p align="center">
  <img src="https://github.com/markh4ck/valuation-toolkit/blob/main/banner.png" alt="Valuation Toolkit"/>
</p>

Production-ready valuation methods for **early-stage startups** and **established firms**.

**Author:** [Marc Aliaga](https://markaliaga.com) — Founder & CEO, [Siprifi](https://www.siprifi.com)

---

## 📌 Overview

Each valuation method is self-contained and includes:

* `algorithm.py` — Executable Python implementation
* `paper.pdf` — Academic paper (math + methodology)

---

## 🌟 Featured Method: Siprifi Dynamic DDM (Startup‑First)

> **The only valuation method that works for cash‑flow‑less startups.**

### Why it works

Traditional methods fail without revenues, dividends, or peers. Siprifi models **growth optionality** directly.

### Example Output

```
Siprifi Valuation: $2.34
Going-Concern Value: $1.89 (80%+ from growth!)
Optimal Capital (K*): 0.23
Optimal Labor (L*): 1.45
```

---

## ⚖️ Method Comparison

| Method           | Needs Cash Flows? | Works for Startups? |
| ---------------- | ----------------- | ------------------- |
| DCF              | ✅ Yes             | ❌ No forecasts      |
| Multiples        | ✅ Yes             | ❌ No peers          |
| Classic DDM      | ✅ Yes             | ❌ No dividends      |
| **Siprifi DDDM** | ❌ No              | ✅ Perfect fit       |

---

## 🔢 Model Inputs (Example)

**16 parameters → Instant valuation**

* `g = 0.02` — Growth narrative
* `sigma = 0.40` — Startup risk ⚡
* `c = 1.1` — Technology edge
* `alpha_L = 0.60` — Team scalability

---

## 📁 Repository Structure

```
valuation-toolkit/
├── Dynamic_DDM/             # Startups, early-stage
│   ├── algorithm.py         # Production code
│   ├── paper.pdf            # Academic paper
├── Discounted_Cash_Flow/    # Discounted Cash Flow
├── gordon/                  # Gordon Growth Model
├── multiples/               # Market multiples
├── rimm/                    # Residual Income Model
└── apv/                     # Adjusted Present Value
```

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/markh4ck/valuation-toolkit.git
cd valuation-toolkit/siprifi

# Install dependencies (numpy only)
pip install numpy

# Run valuation
python algorithm.py
```

Read the methodology:

```bash
open paper.pdf
```

---

## 🧮 Siprifi Core Equation

**Total Value = Book Equity + Growth Optionality**

[
V_0 = \max(0, \text{Book Equity} + G_z)
]

[
G_z = M_z \times P^* \quad (\approx 80%+ \text{ of startup value})
]

---

## 🔬 Academic Foundation

**Lazzati & Menichini (2018)**
*A Dynamic Model of Firm Valuation* — The Financial Review

> “Applicable to private firms, IPOs (e.g. Facebook 2012), and new projects.”

---

## 🛠️ Available Valuation Methods

| Method    | Best For           | Main File                |
| --------- | ------------------ | ------------------------ |
| Dyamic DDM| Startups           | `Dynamic_DDM/algorithm.py`   |
| DCF       | Mature firms       | `dcf/algorithm.py`       |
| Gordon    | Stable growth      | `gordon/algorithm.py`    |
| Multiples | Public comparables | `multiples/algorithm.py` |

---

## 📊 Example Valuations

* 🚀 **Dynamic DDM:** $2.34 (80% growth value)
* 💰 **DCF:** $1.87 (cash-flow based)
* 📈 **Gordon:** $2.12 (perpetual growth)

---

## ✅ Key Features

* Copy‑paste executable (no setup)
* Academic rigor (papers included, citeable)
* Startup‑optimized (no cash flows required)
* Fully transparent math → code
* Modular: mix & match methods

---

## 🧑‍💼 Usage Example (Pitch Deck)

```python
params = {'g': 0.05, 'sigma': 0.50, 'c': 1.3}  # Aggressive startup
valuation = calculate_siprifi_valuation(params)

print(f"Pre-money valuation: ${valuation['Total Valuation']:,.0f}M")
# Pre-money valuation: $23M
```

---

## 👨‍💼 About the Author

**Marc Aliaga**
Founder & CEO, [Siprifi](https://www.siprifi.com)
🌐 [https://markaliaga.com](https://markaliaga.com)
🐙 [https://github.com/markh4ck](https://github.com/markh4ck)

---

## 📚 Citation

```bibtex
@misc{aliaga2026siprifi,
  title     = {Siprifi: Dynamic DDM Valuation Toolkit},
  author    = {Aliaga, Marc},
  year      = {2026},
  publisher = {GitHub: markh4ck/valuation-toolkit},
  url       = {https://github.com/markh4ck/valuation-toolkit}
}
```

---

## 💼 Built For

* Founders — Pitch deck valuations
* VCs — Due diligence
* Quants — Research replication
* Academics — Teaching & papers
* Consultants — Client deliverables

---

## ⭐ Support the Project

* ⭐ Star this repoS
* 🐦 [Follow on X](https://x.com/markaliaga_)
* 🌐 [Visit markaliaga.com](https://markaliaga.com)

---

## 📄 License

MIT License — Free for commercial and academic use
© 2026 Marc Aliaga

---

Built with ❤️ for founders worldwide.
