# Understanding and Updating Statistics in the FAIR Monte Carlo Tool

This guide explains where incident frequency statistics and risk parameters are stored in the code, how they were derived, and how to update them.

## 📍 Where Statistics Are Stored

### 1. Dashboard Presets (`fair_dashboard.py`)

**Location**: Lines 100-142 in the `load_preset()` function

This is where the **default preset scenarios** live. Each preset contains calibrated parameters based on industry research.

**Example - Ransomware Attack:**
```python
"Ransomware Attack": {
    "tef_min": 100,           # Minimum threat attempts per year
    "tef_mode": 300,          # Most likely threat attempts per year
    "tef_max": 1000,          # Maximum threat attempts per year
    "vuln_contact": 0.25,     # 25% of threats reach the target
    "vuln_action": 0.10,      # 10% result in user action
    "vuln_rate": 0.35,        # 35% succeed when acted upon
    "primary_min": 20000,     # Minimum direct loss (€)
    "primary_mode": 75000,    # Most likely direct loss (€)
    "primary_max": 350000,    # Maximum direct loss (€)
    "secondary_min": 10000,   # Minimum indirect loss (€)
    "secondary_mode": 40000,  # Most likely indirect loss (€)
    "secondary_max": 200000,  # Maximum indirect loss (€)
    "secondary_prob": 0.35    # 35% chance of secondary losses
}
```

### 2. Documentation (`docs/FAIR_Parameter_Reference.md`)

**Location**: Complete file with detailed benchmarks

This contains the **research sources and detailed explanations** for all parameter values:
- Threat Event Frequency by company size
- Vulnerability rates by control maturity
- Loss magnitudes with breakdown by cost component
- Industry-specific modifiers
- Data source citations

### 3. Command-Line Example (`fair_monte_carlo.py`)

**Location**: Lines 360-385 in the `example_ransomware_scenario()` function

Contains a standalone example with inline comments explaining each parameter.

## 📊 How Current Statistics Were Derived

### Threat Event Frequency (TEF)

**Ransomware Example:**
- **Source**: Sophos State of Ransomware 2024 + Verizon DBIR 2024
- **Methodology**: 
  - Small businesses: 100-1,000 ransomware attempts/year
  - Mode (300) represents median from Sophos data
  - Adjusted for EU SMB context (slightly lower than US)

**Data Breach Example:**
- **Source**: Verizon DBIR 2024 (phishing as primary vector)
- **Methodology**:
  - Email gateway logs show 500-4,000 malicious emails/year for SMBs
  - Mode (1,500) based on median across industries

### Vulnerability Rates

**Formula**: `Total Vulnerability = Contact × Action × Vulnerability`

**Ransomware (0.875% total):**
- **Contact (0.25)**: Email filtering blocks 75% (industry standard)
- **Action (0.10)**: 10% of users click suspicious links (training dependent)
- **Vulnerability (0.35)**: 35% of clicks lead to compromise (EDR/AV effectiveness)

**Sources**:
- Verizon DBIR (click rates)
- KnowBe4 phishing benchmarks
- SANS Security Awareness Report

### Loss Magnitudes

**Primary Losses** (Direct Costs):
- **Incident Response**: €10k-50k (based on hourly rates × typical engagement)
- **Downtime**: Revenue/hour × hours down (industry-specific)
- **Recovery**: €5k-100k (system rebuild, data restoration)
- **Legal/PR**: €5k-50k (SMB range)

**Sources**:
- IBM Cost of Data Breach 2024 (€4.88M average, scaled to SMB)
- Ponemon Institute studies
- Coalition Cyber Insurance claims data

**Secondary Losses** (Indirect Costs):
- **GDPR Fines**: €10k-500k (GDPR Enforcement Tracker, actual SMB fines)
- **Customer Churn**: Varies by industry (5-30% post-breach)
- **Reputation**: Lost revenue based on public breach disclosure studies

**Sources**:
- EU GDPR Enforcement Tracker (actual fine data)
- Privacy Affairs GDPR fine database
- Academic studies on breach reputation impact

## 🔄 How to Update Statistics

### Method 1: Update Dashboard Presets (Recommended for Most Users)

**Step 1: Open `fair_dashboard.py`**

**Step 2: Find the `load_preset()` function** (around line 100)

**Step 3: Modify the values you want to update**

**Example - Updating Ransomware TEF based on new data:**

```python
# BEFORE (based on 2024 data)
"Ransomware Attack": {
    "tef_min": 100, 
    "tef_mode": 300, 
    "tef_max": 1000,
    ...
}

# AFTER (based on 2025 data showing increased frequency)
"Ransomware Attack": {
    "tef_min": 150,  # ← Updated: 50% increase observed
    "tef_mode": 450, # ← Updated: based on Sophos 2025 report
    "tef_max": 1500, # ← Updated: worst-case scenarios increased
    ...
}
```

**Step 4: Add a comment explaining the change**

```python
"Ransomware Attack": {
    # Updated 2025-01-15: Based on Sophos State of Ransomware 2025
    # TEF increased 50% YoY for EU SMBs (n=2,500 organizations)
    "tef_min": 150,
    "tef_mode": 450,
    "tef_max": 1500,
    ...
}
```

**Step 5: Test the change**

```bash
streamlit run fair_dashboard.py
# Select "Ransomware Attack" preset
# Verify new values load correctly
```

**Step 6: Document in CHANGELOG.md**

```markdown
## [1.1.0] - 2025-01-15

### Changed
- Updated Ransomware TEF parameters based on Sophos 2025 report
  - TEF increased 50% reflecting increased targeting of SMBs
  - Sources: Sophos State of Ransomware 2025, Verizon DBIR 2025
```

### Method 2: Update Documentation Reference

**File**: `docs/FAIR_Parameter_Reference.md`

**What to update**: The detailed benchmark tables

**Example:**

```markdown
## Threat Event Frequency (TEF) - Industry Benchmarks

### Ransomware Attempts
| Company Size | Min/Year | Mode/Year | Max/Year | Source |
|-------------|----------|-----------|----------|--------|
| Small | 150 | 450 | 1,500 | Sophos 2025 ← UPDATED |
```

### Method 3: Add a New Preset Scenario

**Step 1: Choose a name and gather data**

Example: "Supply Chain Attack"

**Step 2: Add to the presets dictionary**

```python
def load_preset(scenario):
    presets = {
        # ... existing presets ...
        
        "Supply Chain Attack": {
            # Based on: ENISA Threat Landscape 2025, Supply Chain section
            # Observation: 15-60 supply chain incidents/year for mid-size orgs
            "tef_min": 15,      # Conservative: quarterly incidents
            "tef_mode": 30,     # Most likely: monthly attempts
            "tef_max": 60,      # Aggressive targeting
            
            # Vulnerability: Depends on vendor management
            "vuln_contact": 0.80,  # High: most orgs have 50+ vendors
            "vuln_action": 0.05,   # Low: vendor compromise is rare
            "vuln_rate": 0.40,     # Medium: if vendor compromised, impact likely
            
            # Primary loss: Extended incident response + vendor coordination
            "primary_min": 30000,
            "primary_mode": 120000,
            "primary_max": 500000,
            
            # Secondary: Reputation + regulatory (NIS2 implications)
            "secondary_min": 20000,
            "secondary_mode": 100000,
            "secondary_max": 600000,
            "secondary_prob": 0.60  # High: supply chain breaches are public
        },
    }
```

**Step 3: Add to the dropdown menu**

Find this line (around line 66):
```python
scenario_preset = st.selectbox(
    "📋 Load Preset Scenario",
    ["Custom", "Ransomware Attack", "Data Breach (GDPR)", 
     "Business Email Compromise", "DDoS Attack", "Insider Threat"]
)
```

Add your new preset:
```python
scenario_preset = st.selectbox(
    "📋 Load Preset Scenario",
    ["Custom", "Ransomware Attack", "Data Breach (GDPR)", 
     "Business Email Compromise", "DDoS Attack", "Insider Threat",
     "Supply Chain Attack"]  # ← Added here
)
```

**Step 4: Document the new preset**

Create a section in `docs/FAIR_Parameter_Reference.md`:

```markdown
### 6. Supply Chain Attack

```python
tef = FAIRDistribution('pert', min_val=15, mode_val=30, max_val=60)
vulnerability = 0.80 * 0.05 * 0.40  # = 0.016 (1.6%)
primary = FAIRDistribution('lognormal', min_val=30000, mode_val=120000, max_val=500000)
secondary = FAIRDistribution('lognormal', min_val=20000, mode_val=100000, max_val=600000)
secondary_prob = 0.60
```

**Data Sources:**
- ENISA Threat Landscape 2025 (Supply Chain section)
- CISA Supply Chain Risk Management guidelines
- IBM X-Force Threat Intelligence Index 2025
```

## 📚 Best Practices for Updates

### 1. Always Cite Sources

```python
"Ransomware Attack": {
    # Source: Sophos State of Ransomware 2025 (pp. 23-25)
    # Sample: 3,000 EU SMBs, surveyed Q4 2024
    # Context: 50% YoY increase in targeting
    "tef_min": 150,
    ...
}
```

### 2. Explain Your Reasoning

```python
# Vulnerability reduced from 0.35 to 0.20 because:
# - MFA adoption increased to 85% (Microsoft Digital Defense Report 2025)
# - EDR deployment increased to 60% in EU SMBs (ENISA survey 2025)
# - Resulted in 43% reduction in successful compromises
"vuln_rate": 0.20,  # Updated 2025-01-15
```

### 3. Keep Old Values Commented

```python
# Historical values for reference:
# "tef_mode": 300,  # 2024 baseline (Sophos 2024)
# "tef_mode": 450,  # 2025 update (Sophos 2025) ← current
```

### 4. Version Your Updates

Add to `CHANGELOG.md`:
```markdown
## [1.1.0] - 2025-01-15
### Changed
- Ransomware TEF: 300 → 450 events/year (Sophos 2025)
- Data Breach vulnerability: 0.60% → 0.45% (improved MFA adoption)
- GDPR fine estimates: Updated based on 2024 enforcement data
```

### 5. Regional Adjustments

If you're adapting for different regions:

```python
def load_preset(scenario, region="EU"):
    if region == "EU":
        # EU-specific parameters (GDPR context)
        gdpr_fine_max = 400000
    elif region == "US":
        # US-specific parameters (state breach laws)
        gdpr_fine_max = 0  # Not applicable
        # But add state breach notification costs
    
    presets = {
        "Data Breach (GDPR)": {
            ...
            "secondary_max": gdpr_fine_max,
        }
    }
```

## 🔍 Verifying Your Updates

### Sanity Check Questions

Before committing changes, ask:

1. **Is the TEF reasonable?**
   - 1,000+ events/year for small org? Probably too high
   - 10 events/year for a common threat? Probably too low

2. **Is the vulnerability in range?**
   - Total vulnerability >10%? Very risky (or poor controls)
   - Total vulnerability <0.01%? Extremely well-protected (rare)

3. **Are loss magnitudes realistic?**
   - Primary loss > annual revenue? Unrealistic for SMB
   - Mode between min and max? Should be closer to min (lognormal)

4. **Do sources support the values?**
   - Can you point to the page number in the report?
   - Is the sample size adequate?
   - Is the data recent (within 2 years)?

### Test Process

```bash
# 1. Update the code
nano fair_dashboard.py

# 2. Launch dashboard
streamlit run fair_dashboard.py

# 3. Select your updated preset
# 4. Run simulation
# 5. Check results are reasonable:
#    - Mean ALE: 0.3-0.6% of revenue (typical SMB)
#    - LEF: Reasonable number of events
#    - No negative values
#    - Percentiles make sense
```

## 📊 Data Sources to Monitor

### Annual Updates Recommended

**General Threat Landscape:**
- Verizon DBIR (published March/April each year)
- ENISA Threat Landscape (published annually)
- Cyentia Institute IRIS (periodic updates)

**Cyber Insurance Claims:**
- Coalition Cyber Claims Report (annual)
- Allianz Commercial Cyber Report (annual)
- Munich Re Cyber Risk publications

**Regional Enforcement:**
- EU GDPR Enforcement Tracker (updated continuously)
- National DPA annual reports

**Industry-Specific:**
- ISACs for your sector
- Sector-specific breach reports

### Where to Find Data

**Free Sources:**
- Verizon DBIR: https://www.verizon.com/business/resources/reports/dbir/
- ENISA Reports: https://www.enisa.europa.eu/publications
- CISA Advisories: https://www.cisa.gov/news-events/cybersecurity-advisories
- GDPR Tracker: https://www.enforcementtracker.com/

**Paid/Research Access:**
- Gartner research (if you have access)
- Forrester reports
- Ponemon Institute studies
- Academic databases (IEEE, ACM)

## 🤝 Contributing Updates

If you update parameters based on new research:

1. **Fork the repository** (if open source)
2. **Make your changes** with proper documentation
3. **Create a pull request** with:
   - Clear description of what changed
   - Citation of data sources
   - Explanation of methodology
   - Test results showing reasonableness
4. **Engage in discussion** about the changes

## 📝 Template for Update Documentation

When updating, use this template in your commit message:

```
Update [Scenario] parameters based on [Source]

Changes:
- TEF: [old] → [new] ([reason])
- Vulnerability: [old] → [new] ([reason])
- Loss magnitudes: [old] → [new] ([reason])

Data Source:
- [Full citation]
- Sample size: [n]
- Region: [EU/US/Global]
- Date: [when data was collected]

Justification:
[Explain why this update improves accuracy]

Testing:
- Ran simulation with new parameters
- Mean ALE: €[amount] ([%] of €5M revenue)
- Results within expected range
```

## 🎓 Example: Complete Update Process

Let's walk through updating ransomware statistics based on new 2025 data:

### Step 1: New Data Available

**Source**: Sophos State of Ransomware 2025 (hypothetical)
**Finding**: Ransomware attempts increased 50% YoY for EU SMBs

### Step 2: Calculate New Parameters

**Old values** (2024):
- TEF: 100-300-1000
- Vulnerability: 0.875%

**New values** (2025):
- TEF: 150-450-1500 (50% increase)
- Vulnerability: 0.60% (MFA adoption reduced successful compromise)

### Step 3: Update Code

```python
"Ransomware Attack": {
    # === UPDATED 2025-01-15 ===
    # Source: Sophos State of Ransomware 2025, pp. 23-28
    # Sample: 3,000 EU organizations (500-5,000 employees)
    # Key findings:
    # - 50% increase in targeting (TEF ↑)
    # - MFA adoption (78% → 89%) reduced success rate (Vuln ↓)
    
    # Threat Event Frequency (ransomware attempts/year)
    "tef_min": 150,    # Was: 100 (2024)
    "tef_mode": 450,   # Was: 300 (2024)
    "tef_max": 1500,   # Was: 1000 (2024)
    
    # Vulnerability components
    "vuln_contact": 0.20,  # Was: 0.25 (better email filtering)
    "vuln_action": 0.10,   # Unchanged (user behavior stable)
    "vuln_rate": 0.30,     # Was: 0.35 (MFA + EDR improvements)
    # Total vuln: 0.20 × 0.10 × 0.30 = 0.006 (0.6%)
    
    # Loss magnitudes unchanged (no new cost data)
    "primary_min": 20000,
    "primary_mode": 75000,
    "primary_max": 350000,
    "secondary_min": 10000,
    "secondary_mode": 40000,
    "secondary_max": 200000,
    "secondary_prob": 0.35
},
```

### Step 4: Test

```bash
streamlit run fair_dashboard.py
# Select "Ransomware Attack"
# Run simulation
# Verify: Mean ALE changed from ~€460k to ~€540k
# Reason: More attempts (TEF ↑) offset by better defenses (Vuln ↓)
```

### Step 5: Document

**In CHANGELOG.md:**
```markdown
## [1.1.0] - 2025-01-15

### Changed
- **Ransomware Attack preset** - Updated parameters based on 2025 threat landscape
  - TEF increased 50% (150-450-1500, was 100-300-1000)
  - Vulnerability decreased 31% (0.6%, was 0.875%)
  - Net effect: ~18% increase in expected annual loss
  - Sources: Sophos State of Ransomware 2025, Microsoft Digital Defense Report 2025
```

### Step 6: Communicate

**In README.md or blog post:**
```markdown
## Recent Updates (January 2025)

We've updated the ransomware parameters based on the latest threat intelligence:

📈 **Threat frequency increased**: Organizations now face 50% more ransomware 
attempts compared to 2024, reflecting intensified targeting of EU SMBs.

🛡️ **But defenses improved**: Widespread MFA adoption (now 89% of SMBs) and 
better EDR deployment have reduced the success rate by 31%.

💶 **Net impact**: Expected annual loss increased ~18% despite better defenses, 
due to the significant increase in attack volume.

**Sources**: Sophos State of Ransomware 2025, Microsoft Digital Defense Report 2025
```

## 🎯 Summary

**Where statistics live:**
1. `fair_dashboard.py` - lines 100-142 (dashboard presets)
2. `docs/FAIR_Parameter_Reference.md` - detailed benchmarks
3. `fair_monte_carlo.py` - line 360+ (example code)

**How to update:**
1. Modify the dictionary values in `load_preset()`
2. Add comments citing sources
3. Test the changes
4. Document in CHANGELOG.md
5. Update parameter reference docs

**Best practices:**
- Always cite sources with page numbers
- Explain your reasoning
- Keep historical values commented
- Version your updates
- Verify results are reasonable

**For major updates:**
- Consider a new minor version (1.0 → 1.1)
- Write a blog post explaining the changes
- Notify users via GitHub release notes

---

**Questions?** The statistics are designed to be transparent and updatable as new research emerges. This is a living tool that should evolve with the threat landscape!
