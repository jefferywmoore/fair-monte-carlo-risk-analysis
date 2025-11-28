# FAIR Risk Analysis Dashboard

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A professional, web-based tool for conducting quantitative cybersecurity risk assessments using the FAIR (Factor Analysis of Information Risk) methodology.

![Dashboard Preview](docs/images/dashboard-preview.png)

## ✨ Key Features

- 🎯 **Interactive Monte Carlo Simulation** - Run 1,000 to 50,000 simulations for statistical rigor
- 🌍 **External vs Internal Factor Grouping** - Clear visual distinction between controllable and uncontrollable risk factors
- 🎚️ **Configurable Risk Tolerance** - Set custom thresholds (Conservative/Moderate/Aggressive/Custom) aligned with your risk appetite
- 💡 **Comprehensive Help System** - 35+ in-context tooltips with FAIR-aligned definitions
- 📊 **Rich Visualizations** - Interactive charts with distribution, exceedance curves, percentiles, and LEF analysis
- 🎨 **Preset Scenarios** - 9 pre-configured risk scenarios for common threats (Ransomware, Data Breach, BEC, DDoS, Insider Threat, Zero-Day, Device Theft, System Outage, Supply Chain)
- 💰 **ROI Calculators** - Built-in ROSI analysis and insurance recommendation tools
- 📥 **Multiple Export Formats** - JSON, CSV, and formatted text reports
- 🎓 **Educational Design** - UI teaches FAIR principles through its structure

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/fair-risk-dashboard.git
cd fair-risk-dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch the dashboard
streamlit run fair_dashboard.py
```

The dashboard will automatically open in your browser at `http://localhost:8501`

### First Use

1. Load a preset scenario (e.g., "Ransomware Attack")
2. Click the (?) help icons to learn FAIR terminology
3. Adjust parameters to match your organization
4. Click "Run Simulation"
5. Explore the four visualization tabs
6. Export your results

## 📊 Understanding the Interface

### External vs Internal Factors

The dashboard clearly distinguishes between factors you can and cannot control:

**🌍 External Factors (Threat Landscape)**
- **Contact Frequency** - Industry-wide threat volume (you can't control)

**🏢 Internal Factors (Your Organization)**
- **Threat Event Frequency & Probability of Action** - Your attractiveness as a target (partially controllable)
- **Vulnerability** - Your security control effectiveness (directly controllable)
- **Loss Magnitudes** - Your specific costs and exposure (partially controllable)

This distinction is fundamental to making smart security investment decisions.

## 📚 Documentation

- **[Getting Started Guide](docs/README_ENHANCED.md)** - Complete user guide with tutorials
- **[FAIR Quick Reference](docs/FAIR_QUICK_REFERENCE.md)** - Essential FAIR terminology and concepts
- **[UI Reorganization Guide](docs/UI_REORGANIZATION_GUIDE.md)** - Understanding external vs internal factors
- **[Help Text Reference](docs/HELP_TEXT_SUMMARY.md)** - Complete catalog of all tooltips
- **[Changelog](CHANGELOG.md)** - Version history and updates

## 🎓 FAIR Methodology

This tool implements the FAIR (Factor Analysis of Information Risk) standard for quantitative risk analysis:

```
Risk = Loss Event Frequency × Loss Magnitude

Where:
  LEF = Threat Event Frequency × Vulnerability
  TEF = Contact Frequency × Probability of Action
  LM = Primary Loss + Secondary Loss (when applicable)
```

**Learn More:**
- [FAIR Institute](https://www.fairinstitute.org/)
- ["Measuring and Managing Information Risk" by Jack A. Jones](https://www.fairinstitute.org/fair-risk-book)

## 💡 Use Cases

### For Security Analysts
- Quantify cyber risk in financial terms
- Compare different risk scenarios
- Justify security investments with ROSI calculations
- Track risk reduction over time

### For Consultants
- Professional client presentations
- Standardized risk assessment methodology
- Clear communication of complex risk concepts
- Generate client-ready reports

### For Executives
- Understand risk in business terms (% of revenue)
- Make informed risk acceptance decisions
- Evaluate security investment proposals
- Set realistic risk appetite thresholds

## 🛠️ Technical Stack

- **Framework:** Streamlit (Python web framework)
- **Simulation:** NumPy (Monte Carlo engine)
- **Visualization:** Plotly (interactive charts)
- **Data Export:** Pandas (CSV/JSON export)
- **Distributions:** PERT, Lognormal, Normal, Uniform

## 📈 Version History

### Version 1.3 (Current) - Risk Tolerance Configuration
- 🎚️ Configurable risk tolerance thresholds
- 📊 Four preset profiles (Conservative/Moderate/Aggressive/Custom)
- 📈 Visual threshold indicators on charts
- 🎯 Industry-aligned risk assessment
- 📋 Four new threat scenarios (Zero-Day, Device Theft, System Outage, Supply Chain)

### Version 1.2 - UI Reorganization
- ✨ Visual grouping of external vs internal factors
- 🎨 Bordered containers for clear section separation
- 📚 Enhanced help text with controllability indicators
- 📖 New UI Reorganization Guide

### Version 1.1 - Complete Help Text
- 💡 35 comprehensive help tooltips (100% coverage)
- 📝 FAIR-aligned definitions with examples
- 🎓 Self-service learning capability

### Version 1.0 - Initial Release
- 🎯 Core FAIR risk assessment functionality
- 📊 Monte Carlo simulation engine
- 📈 Interactive visualizations
- 📥 Export capabilities

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

```bash
# Clone and setup
git clone https://github.com/yourusername/fair-risk-dashboard.git
cd fair-risk-dashboard
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Run with hot reload
streamlit run fair_dashboard.py --logger.level=debug
```

### Guidelines
- Follow PEP 8 style guidelines
- Maintain FAIR methodology alignment
- Update help text for new features
- Add tests for new functionality
- Update documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **FAIR Institute** - For the FAIR methodology and standard definitions
- **Jack A. Jones** - Creator of the FAIR framework
- **BARE Cybersecurity** - Project sponsor and primary use case

## 📞 Support

- **Documentation:** See [docs/](docs/) directory
- **Issues:** [GitHub Issues](https://github.com/yourusername/fair-risk-dashboard/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/fair-risk-dashboard/discussions)
- **FAIR Resources:** [fairinstitute.org](https://www.fairinstitute.org/)

## 🌟 Star History

If you find this tool useful, please consider starring the repository!

---

**Built with ❤️ for the cybersecurity community**

*Making quantitative risk analysis accessible to everyone*
