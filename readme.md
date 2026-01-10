# Siprifi Valuation Toolkit 🚀

><p align="center">
  <img src="https://raw.githubusercontent.com/markh4ck/Siprifi-Valuation-Toolkit/main/valuation-toolkit/logo.png" alt="Valuation Toolkit"/>

**Author:** [Marc Aliaga](https://markaliaga.com) — Founder & CEO, [Siprifi](https://www.siprifi.com)

---

## 📌 Overview

Each valuation method is self-contained and includes:

* `algorithm.py` — Executable Python implementation
* `paper.pdf` — Academic paper (math + methodology)

## ⚖️ Method Comparison

| Method           | Needs Cash Flows? | Works for Startups? |
| ---------------- | ----------------- | ------------------- |
| DCF              | ✅ Yes             | ❌ No forecasts      |
| Multiples        | ✅ Yes             | ❌ No peers          |
| Classic DDM      | ✅ Yes             | ❌ No dividends      |
| **Dynaimc DDM** | ❌ No              | ✅ Perfect fit       |

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
# Based on the business's own cash & returns
│   ├── Discounted_Cash_Flow/        # Cash Flow is the primary driver
│   │   ├── CAPM/                    # Calculating WACC / Cost of Equity
│   │   └── Certainty-Equivalent/    # Risk-adjusted cash flow logic
│   ├── ROIC-based-Valuation/        # Efficiency & Moat-driven (Gordon Growth)
│   ├── rimm/                        # Residual Income (Accrual-based valuation)
│   └── apv/                         # Adjusted Present Value (Best for LBOs/Debt)
│
# Based on market pricing of peers
│   └── multiples/                   # Trading Comps (P/E, EV/EBITDA) & Precedents
│
# For high uncertainty & optionality
│   └── Dynamic_Firm_Valuation/      # Startups, R&D, and Monte Carlo paths
│       ├── algorithm.py
│       └── paper.pdf
│
 # "Worst case" or floor valuation  
    └── asset_based/                 # Net Asset Value (NAV) & Replacement Cost
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

## 🔬 Academic Foundation

**Lazzati & Menichini (2018)**
*A Dynamic Model of Firm Valuation* — The Financial Review

> “Applicable to private firms, IPOs (e.g. Facebook 2012), and new projects.”

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
