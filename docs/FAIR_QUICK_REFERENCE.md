# FAIR Terminology Quick Reference Card

## 🎯 For Dashboard Users: Essential FAIR Concepts

This quick reference helps you understand the key terms in the FAIR Risk Analysis Dashboard. Each term now has a help icon (?) in the dashboard - click it for detailed explanations.

---

## 📊 The Big Picture: How FAIR Works

```
         RISK = Frequency × Magnitude
              ↙                    ↘
    How Often?                  How Big?
    (LEF)                       (LM)
      ↙                           ↙    ↘
  TEF × Vulnerability      Primary  +  Secondary
    ↙       ↘                Loss         Loss
CF × PoA   Controls
```

### 🌍 External vs 🏢 Internal Factors

**Key Insight:** FAIR factors come from two different sources:

**🌍 External Factors (Threat Landscape):**
- **Contact Frequency (CF)** - Industry-wide threat activity
- Based on threat intelligence, industry reports
- Same for all organizations in your industry
- Example: "Financial services see ~10,000 phishing attempts per employee/year"

**🏢 Internal Factors (Your Organization):**
- **Probability of Action (PoA)** - Your attractiveness as target
- **Vulnerability** - Your control effectiveness  
- **Loss Magnitudes** - Your specific costs and exposure
- Based on your security posture, assets, and environment
- Unique to your organization
- Example: "Our controls block 90% of attacks that get through"

**Why This Matters:**
- External factors you can't control (just measure/estimate)
- Internal factors you CAN control (through security investments)
- ROI calculations focus on improving internal factors

---

## 🔢 The Frequency Side (How Often?)

### 1. Contact Frequency (CF) 🌍 EXTERNAL
**What:** Industry-wide threat volume
**Example:** "Our industry sees ~1,000 phishing emails per employee per year"
**Source:** Industry benchmarks, threat intelligence feeds
**Control:** ❌ You can't control this - it's the threat landscape

### 2. Probability of Action (PoA) 🏢 INTERNAL
**What:** How attractive is YOUR organization as a target?
**Example:** "Of those 1,000 emails, maybe 10% specifically target our company"
**Key:** This converts industry noise to YOUR signal
**Formula:** TEF = CF × PoA
**Control:** ⚠️ Partially controllable - reduce your attractiveness

### 3. Threat Event Frequency (TEF) 🏢 INTERNAL (Calculated)
**What:** Attacks actually targeting YOUR organization
**Example:** "We face ~100 targeted phishing attacks per year"
**Result of:** Contact Frequency × Probability of Action
**Control:** ⚠️ Partially controllable via PoA

### 4. Vulnerability 🏢 INTERNAL
**What:** Probability an attack succeeds
**Example:** "Our controls stop 90% of attacks, so 10% get through"
**Factors:** Control effectiveness, threat capability
**Inverse of:** Your security posture
**Control:** ✅ Directly controllable - invest in better controls

### 5. Loss Event Frequency (LEF) 🏢 INTERNAL (Calculated)
**What:** Successful attacks per year
**Example:** "We expect ~10 successful breaches per year"
**Formula:** LEF = TEF × Vulnerability
**This is the number:** Of actual incidents you'll experience
**Control:** ✅ Controllable via Vulnerability

---

## 💰 The Magnitude Side (How Big?)

### 6. Primary Loss 🏢 INTERNAL
**What:** Direct, immediate costs
**Examples:**
- Hardware replacement
- Ransom payment
- Emergency response team costs
- Incident response contractor fees
**Control:** ⚠️ Partially controllable - reduce asset value, improve recovery

### 7. Secondary Loss 🏢 INTERNAL
**What:** Indirect, consequential costs
**Examples:**
- Regulatory fines (GDPR, etc.)
- Lawsuits and legal costs
- Reputational damage
- Customer churn
- Productivity loss
**Control:** ⚠️ Partially controllable - improve compliance, incident response

**Important:** Not all incidents cause secondary losses!

### 8. Secondary Loss Probability 🏢 INTERNAL
**What:** Chance that secondary losses occur
**Example:** "50% of our data breaches result in regulatory action"
**Control:** ✅ Controllable - improve incident response, regulatory compliance

---

## 📈 The Results (What Does It Mean?)

### 9. Annual Loss Expectancy (ALE)
**What:** Expected loss per year
**Formula:** LEF × Average Loss Magnitude
**Use for:** Budget planning, comparing risks

### 10. Median ALE
**What:** Typical year's losses (50th percentile)
**Better than mean when:** Distribution is skewed
**Use for:** "Normal year" planning

### 11. 95th Percentile
**What:** Worst case with 95% confidence
**Meaning:** Only 5% of years will be worse
**Use for:** Insurance coverage, worst-case budgeting

---

## 🛡️ Making Decisions

### 12. ROSI (Return on Security Investment)
**What:** Percent return on security spending
**Formula:** (Risk Reduction - Control Cost) / Control Cost × 100
**Interpretation:**
- \>100%: Excellent investment
- 0-100%: Positive return
- <0%: Loses money

### 13. Risk Appetite
**What:** How much risk you're willing to accept
**Typical thresholds:**
- Low risk: <0.5% of revenue
- Moderate: 0.5-1% of revenue
- High: >1% of revenue

---

## 🔍 Understanding the PERT Distribution

**The three values you enter:**

1. **Minimum:** Optimistic scenario (10th percentile)
2. **Mode (Most Likely):** Your best single estimate (peak probability)
3. **Maximum:** Pessimistic scenario (90th percentile)

**Why PERT?** It creates a realistic curve that weights toward your best estimate while accounting for uncertainty.

---

## 💡 Pro Tips for Using the Dashboard

### For Threat Event Frequency (TEF):
1. Start with industry data (Contact Frequency)
2. Adjust for your organization's attractiveness (PoA)
3. Don't confuse general threats with targeted threats

### For Vulnerability:
1. Think about your control effectiveness
2. 100% = no controls at all
3. 0% = perfect security (unrealistic!)
4. Most organizations: 5-30% vulnerability

### For Loss Magnitude:
1. Separate direct costs (primary) from indirect (secondary)
2. Remember: not all incidents have secondary losses
3. Use real cost data when possible (forensics reports, insurance claims)

### For Results Interpretation:
1. Mean ALE: Use for budgeting
2. Median: More realistic "typical year"
3. 95th percentile: Use for insurance and reserves
4. Compare to revenue: Is this acceptable?

---

## 🎓 Common Mistakes to Avoid

### ❌ Mistake #1: Confusing CF with TEF
**Wrong:** "We see 10,000 scans per day, so TEF = 10,000"
**Right:** "10,000 scans (CF) × 0.01 (PoA) = 100 TEF"
**Why:** Most scans aren't targeting YOU specifically

### ❌ Mistake #2: Using Mean When You Should Use Median
**Wrong:** Using mean with highly skewed distributions
**Right:** Use median for typical scenarios, mean for budgeting
**Why:** Extreme outliers can skew the mean

### ❌ Mistake #3: Confusing Vulnerability with Risk
**Wrong:** "We have 5 critical vulnerabilities, so risk is high"
**Right:** "Vulnerability is 20%, but TEF is low, so risk is moderate"
**Why:** Risk = Frequency AND Magnitude, not just one factor

### ❌ Mistake #4: All-or-Nothing Secondary Losses
**Wrong:** Secondary probability = 100% or 0%
**Right:** Realistic probability based on history (e.g., 40%)
**Why:** Not all incidents trigger fines/lawsuits

---

## 📋 Quick Calculation Cheat Sheet

```
TEF = Contact Frequency × Probability of Action

Vulnerability = Contact × Action × Vuln Rate
             (or use single Vulnerability slider)

LEF = TEF × Vulnerability

ALE = LEF × Average Loss Magnitude

ROSI = (Risk Reduction - Control Cost) / Control Cost × 100

Risk as % of Revenue = ALE / Annual Revenue × 100
```

---

## 🎯 Decision Frameworks

### Should We Implement This Control?
1. Calculate current ALE
2. Estimate risk reduction (%)
3. Calculate new ALE
4. Compare reduction to control cost
5. Calculate ROSI
6. Decision: Implement if ROSI > 0% (or your threshold)

### How Much Insurance Should We Buy?
1. Run simulation
2. Note 95th percentile (recommended coverage)
3. Set deductible at median ALE
4. Compare premium (3-5% of coverage) to risk reduction
5. Decision: Buy if premium < (95th % - median)

### Is This Risk Acceptable?
1. Calculate ALE as % of revenue
2. Compare to risk appetite:
   - <0.5%: Generally acceptable
   - 0.5-1%: Moderate, consider controls
   - \>1%: High, take action
3. Consider non-financial impacts
4. Decision: Accept, mitigate, transfer, or avoid

---

## 📚 Where to Learn More

**In the Dashboard:**
- Every field has a (?) help icon - click for details
- Results tabs show different views of the same data
- Export reports for deeper analysis

**FAIR Institute Resources:**
- www.fairinstitute.org
- "Measuring and Managing Information Risk" book
- FAIR-CAM certification

**Best Practices:**
- Use real historical data when available
- Calibrate estimates with experts
- Update regularly (quarterly reviews)
- Document your assumptions

---

## 🚀 Getting Started Checklist

### First Time Using the Dashboard?

1. ☐ Load a preset scenario (e.g., "Ransomware Attack")
2. ☐ Click the (?) help icons to understand each term
3. ☐ Run the simulation with default values
4. ☐ Explore all four result tabs
5. ☐ Try adjusting one parameter at a time
6. ☐ Use the ROSI calculator
7. ☐ Export results in all three formats

### Ready for Real Analysis?

1. ☐ Gather historical incident data
2. ☐ Research industry threat intelligence (CF)
3. ☐ Assess your organization's target profile (PoA)
4. ☐ Evaluate control effectiveness (Vulnerability)
5. ☐ Estimate realistic cost ranges (Primary/Secondary Loss)
6. ☐ Run multiple scenarios (best/worst/likely case)
7. ☐ Document assumptions and sources
8. ☐ Present to stakeholders with confidence

---

## 🎨 Visual Legend

When you see these colors in results:

- **🟢 Green**: Acceptable risk (<0.5% revenue)
- **🟡 Orange**: Moderate risk (0.5-1% revenue)
- **🔴 Red**: High risk (>1% revenue)

---

## 💬 Questions?

**Every field in the dashboard now has help text!**

Just hover over or click the (?) icon next to any term for:
- Precise FAIR definition
- Practical examples
- Calculation formulas
- Interpretation guidance

---

**Remember:** Risk quantification is part art, part science. Use ranges to express uncertainty, document your reasoning, and update regularly as you learn more.

**Happy Risk Quantifying! 🛡️**

---

*This quick reference card complements the enhanced FAIR Risk Analysis Dashboard v1.1*
*All definitions align with FAIR Institute standards*
