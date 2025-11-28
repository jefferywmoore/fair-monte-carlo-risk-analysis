# Preset Threat Scenarios Guide

## 📋 Overview

The FAIR Risk Analysis Dashboard includes **9 pre-configured threat scenarios** based on common cybersecurity risks. Each preset contains realistic FAIR parameters derived from industry data and threat intelligence.

---

## 🎯 How to Use Preset Scenarios

### Quick Start
1. Open dashboard sidebar
2. Select "📋 Load Preset Scenario"
3. Choose a threat type
4. Click "🚀 Run Simulation"
5. Review results

### Customization
- Presets provide starting values
- All parameters can be adjusted
- Modify to match your specific environment
- Save custom scenarios for reuse

---

## 💻 Available Threat Scenarios

### 1. 🔐 Ransomware Attack

**Description:**
Malicious software that encrypts files and demands ransom payment. One of the most prevalent and costly cyber threats facing organizations.

**Threat Profile:**
- **Frequency:** Moderate to High (100-1,000 attempts/year)
- **Contact:** 25% (moderate phishing/exploit exposure)
- **Action:** 10% (somewhat targeted)
- **Vulnerability:** 35% (depends on patching, backups, awareness)

**Loss Profile:**
- **Primary Loss:** €20K - €350K (ransom, recovery, downtime)
- **Secondary Loss:** €10K - €200K (reputation, legal, compliance)
- **Secondary Probability:** 35%

**Key Factors:**
- High primary loss from operational disruption
- Moderate secondary loss from PR damage
- Vulnerability heavily depends on backup strategy
- Payment often doesn't guarantee recovery

**Best For:**
- Organizations with limited backup capabilities
- Companies with high ransomware exposure
- Businesses evaluating backup investments

**Typical Industries:**
- Healthcare (high value targets)
- Manufacturing (operational disruption costly)
- Professional services (document-centric)

---

### 2. 🔓 Data Breach (GDPR)

**Description:**
Unauthorized access to personal data with regulatory compliance implications, particularly under GDPR, CCPA, or similar privacy laws.

**Threat Profile:**
- **Frequency:** High (500-4,000 attempts/year)
- **Contact:** 30% (moderate exposure to various attack vectors)
- **Action:** 8% (less targeted than ransomware)
- **Vulnerability:** 25% (depends on access controls, DLP)

**Loss Profile:**
- **Primary Loss:** €15K - €250K (notification, forensics, remediation)
- **Secondary Loss:** €20K - €400K (GDPR fines, lawsuits, churn)
- **Secondary Probability:** 50%

**Key Factors:**
- High secondary loss potential (GDPR fines up to 4% revenue)
- 50% chance of regulatory penalties
- Customer trust damage significant
- Notification costs add up quickly

**Best For:**
- Organizations processing EU personal data
- Companies subject to privacy regulations
- Businesses evaluating DLP/encryption investments

**Typical Industries:**
- E-commerce (customer data)
- Healthcare (PHI/PII)
- Financial services (sensitive data)
- SaaS providers (customer databases)

---

### 3. 📧 Business Email Compromise (BEC)

**Description:**
Social engineering attack where attackers impersonate executives or vendors to trick employees into transferring funds or sensitive data.

**Threat Profile:**
- **Frequency:** Moderate to High (300-2,000 attempts/year)
- **Contact:** 40% (high phishing exposure)
- **Action:** 5% (requires specific targeting)
- **Vulnerability:** 30% (depends on awareness training, controls)

**Loss Profile:**
- **Primary Loss:** €8K - €200K (wire transfers, direct theft)
- **Secondary Loss:** €3K - €75K (reputation, remediation)
- **Secondary Probability:** 25%

**Key Factors:**
- Highly effective social engineering
- Direct financial loss (wire transfers)
- Lower secondary impacts than data breaches
- Prevention relies heavily on training and verification

**Best For:**
- Finance departments with wire transfer authority
- Organizations with weak verification processes
- Companies evaluating awareness training ROI

**Typical Industries:**
- Professional services (frequent invoicing)
- Real estate (large transactions)
- Construction (vendor payments)
- Any business with wire transfer processes

---

### 4. 🌐 DDoS Attack

**Description:**
Distributed Denial of Service attack that floods systems with traffic, causing service unavailability and revenue loss.

**Threat Profile:**
- **Frequency:** Low to Moderate (15-120 attempts/year)
- **Contact:** 50% (publicly accessible services)
- **Action:** 35% (commodity attack, less targeting)
- **Vulnerability:** 100% (always exposed if online)

**Loss Profile:**
- **Primary Loss:** €5K - €120K (downtime, mitigation costs)
- **Secondary Loss:** €3K - €80K (SLA penalties, customer churn)
- **Secondary Probability:** 50%

**Key Factors:**
- Vulnerability is 100% (cannot prevent exposure)
- Success depends on mitigation capabilities
- Revenue loss from downtime
- Reputational damage if prolonged

**Best For:**
- E-commerce platforms
- SaaS providers with SLAs
- Organizations with high availability requirements

**Typical Industries:**
- E-commerce (revenue per hour critical)
- Gaming (uptime essential)
- Financial services (trading platforms)
- SaaS (service level agreements)

---

### 5. 🕵️ Insider Threat

**Description:**
Malicious or negligent actions by employees, contractors, or partners with legitimate access to systems and data.

**Threat Profile:**
- **Frequency:** Low (3-30 attempts/year)
- **Contact:** 60% (employees always have access)
- **Action:** 15% (most employees trustworthy)
- **Vulnerability:** 100% (insiders have legitimate access)

**Loss Profile:**
- **Primary Loss:** €15K - €400K (data theft, sabotage, fraud)
- **Secondary Loss:** €20K - €600K (investigation, legal, reputation)
- **Secondary Probability:** 60%

**Key Factors:**
- Low frequency but high impact
- 100% vulnerability (authorized access)
- High secondary impacts (legal, regulatory)
- Detection often delayed

**Best For:**
- Organizations with privileged access concerns
- Companies with sensitive IP or data
- Businesses evaluating UBA/SIEM investments

**Typical Industries:**
- Financial services (fraud risk)
- Technology (IP theft)
- Healthcare (privacy violations)
- Government (espionage concerns)

---

### 6. 💣 Zero-Day Exploit

**Description:**
Attack leveraging previously unknown software vulnerabilities before patches are available. High impact but lower frequency.

**Threat Profile:**
- **Frequency:** Very Low (5-75 attempts/year)
- **Contact:** 20% (limited availability of exploits)
- **Action:** 50% (highly valuable, actively targeted)
- **Vulnerability:** 50% (depends on compensating controls)

**Loss Profile:**
- **Primary Loss:** €30K - €500K (breach, remediation, emergency response)
- **Secondary Loss:** €50K - €800K (significant reputation damage)
- **Secondary Probability:** 60%

**Key Factors:**
- Low frequency but very high impact
- Cannot patch (vulnerability unknown)
- Requires defense-in-depth strategy
- Often used in APT campaigns

**Best For:**
- High-value targets (government, critical infrastructure)
- Organizations evaluating EDR/XDR investments
- Companies with nation-state threat concerns

**Typical Industries:**
- Critical infrastructure
- Defense contractors
- Financial institutions (nation-state targets)
- Technology companies (IP targets)

---

### 7. 💼 Physical Theft of Device

**Description:**
Theft or loss of laptops, mobile devices, or removable media containing sensitive data. Often opportunistic rather than targeted.

**Threat Profile:**
- **Frequency:** Low to Moderate (10-200 incidents/year)
- **Contact:** 80% (physical access opportunities common)
- **Action:** 10% (mostly opportunistic, not targeted)
- **Vulnerability:** 15% (depends on encryption, remote wipe)

**Loss Profile:**
- **Primary Loss:** €1K - €15K (device replacement, data recovery)
- **Secondary Loss:** €5K - €150K (data breach if unencrypted)
- **Secondary Probability:** 30%

**Key Factors:**
- Low primary loss (device cost)
- Secondary loss only if data exposed
- Encryption dramatically reduces risk
- Mobile workforce increases exposure

**Best For:**
- Organizations with mobile workforce
- Companies with unencrypted devices
- Businesses evaluating MDM/encryption investments

**Typical Industries:**
- Professional services (travel frequent)
- Healthcare (mobile devices common)
- Sales organizations (laptops in cars)
- Field services (tablets, phones)

---

### 8. ⚠️ Critical System Outage

**Description:**
Failure of critical infrastructure (servers, network, cloud services) causing business disruption. May be technical failure or cyber-induced.

**Threat Profile:**
- **Frequency:** Very Low (1-10 incidents/year)
- **Contact:** 100% (all systems can fail)
- **Action:** 100% (not an attack, system failure)
- **Vulnerability:** 80% (depends on redundancy, DR)

**Loss Profile:**
- **Primary Loss:** €15K - €300K (downtime, recovery, lost revenue)
- **Secondary Loss:** €10K - €250K (SLA penalties, customer impact)
- **Secondary Probability:** 50%

**Key Factors:**
- Low frequency but guaranteed to happen eventually
- High vulnerability without redundancy
- Revenue loss per hour critical
- Recovery time objective (RTO) determines impact

**Best For:**
- Organizations evaluating HA/DR investments
- Companies with single points of failure
- Businesses calculating acceptable downtime costs

**Typical Industries:**
- E-commerce (revenue per hour)
- Manufacturing (production lines)
- Financial services (trading systems)
- Healthcare (patient care systems)

---

### 9. 🔗 Supply Chain Compromise

**Description:**
Attack targeting suppliers, vendors, or software providers to gain access to customer networks. Growing threat vector with cascading impacts.

**Threat Profile:**
- **Frequency:** Very Low (2-30 attempts/year)
- **Contact:** 70% (most organizations have suppliers)
- **Action:** 20% (requires significant attacker investment)
- **Vulnerability:** 25% (depends on vendor security requirements)

**Loss Profile:**
- **Primary Loss:** €25K - €600K (breach via vendor, remediation)
- **Secondary Loss:** €50K - €1M (massive reputation damage, legal)
- **Secondary Probability:** 75%

**Key Factors:**
- Low frequency but extreme impact potential
- Very high secondary loss probability (75%)
- Cascading effects across customer base
- Difficult to detect and attribute

**Best For:**
- Organizations with critical suppliers/vendors
- Companies evaluating vendor risk programs
- Businesses with software supply chain exposure

**Typical Industries:**
- Technology (software supply chain)
- Financial services (outsourced services)
- Healthcare (medical device suppliers)
- Government (contractor relationships)

---

## 📊 Scenario Comparison Matrix

| Scenario | Frequency | Primary Loss | Secondary Loss | Vulnerability | Best Defense |
|----------|-----------|--------------|----------------|---------------|--------------|
| **Ransomware** | High | High | Moderate | 35% | Backups, patching |
| **Data Breach** | Very High | Moderate | High | 25% | Encryption, access controls |
| **BEC** | High | Moderate | Low | 30% | Awareness, verification |
| **DDoS** | Moderate | Moderate | Moderate | 100% | DDoS mitigation service |
| **Insider Threat** | Low | High | High | 100% | UBA, least privilege |
| **Zero-Day** | Very Low | Very High | Very High | 50% | EDR, defense-in-depth |
| **Device Theft** | Moderate | Very Low | Moderate | 15% | Encryption, MDM |
| **System Outage** | Very Low | High | Moderate | 80% | HA/DR, redundancy |
| **Supply Chain** | Very Low | Very High | Extreme | 25% | Vendor assessment |

---

## 🎯 Selecting the Right Scenario

### By Industry

**Financial Services:**
- Primary: Data Breach, Ransomware, DDoS
- Secondary: Insider Threat, Zero-Day

**Healthcare:**
- Primary: Ransomware, Data Breach, Insider Threat
- Secondary: Device Theft, System Outage

**Technology/SaaS:**
- Primary: DDoS, Data Breach, Supply Chain
- Secondary: Zero-Day, System Outage

**Retail/E-commerce:**
- Primary: Data Breach, DDoS, BEC
- Secondary: System Outage, Ransomware

**Manufacturing:**
- Primary: Ransomware, System Outage, Supply Chain
- Secondary: Insider Threat, Device Theft

**Professional Services:**
- Primary: BEC, Data Breach, Device Theft
- Secondary: Ransomware, Insider Threat

### By Risk Priority

**Highest Frequency:**
1. Data Breach (500-4,000/year)
2. BEC (300-2,000/year)
3. Ransomware (100-1,000/year)

**Highest Impact:**
1. Supply Chain (€75K-€1.6M total)
2. Zero-Day (€80K-€1.3M total)
3. Insider Threat (€35K-€1M total)

**Highest Secondary Probability:**
1. Supply Chain (75%)
2. Insider Threat (60%)
3. Zero-Day (60%)

---

## 💡 Customization Tips

### Adjust for Your Environment

**Increase TEF if:**
- High-profile organization
- Publicly known security incidents
- Industry under active attack
- Valuable data/systems

**Decrease TEF if:**
- Low profile organization
- Strong deterrence in place
- Not in targeted industry
- Limited attack surface

**Increase Vulnerability if:**
- Legacy systems
- Limited patching
- Weak controls
- High user privileges

**Decrease Vulnerability if:**
- Modern security architecture
- Strong controls
- Good security hygiene
- Defense-in-depth

**Adjust Loss Magnitudes for:**
- Organization size
- Industry specifics
- Regulatory environment
- Revenue models

---

## 🔄 Combining Scenarios

### Multi-Threat Analysis

Run multiple scenarios to understand cumulative risk:

**Example: Technology Company**
1. Run Data Breach scenario → €150K ALE
2. Run DDoS scenario → €75K ALE
3. Run Supply Chain scenario → €200K ALE
4. **Total portfolio risk:** €425K ALE

**Portfolio View:**
- Prioritize highest risks first
- Look for common controls
- Optimize security spend
- Balance prevention vs. insurance

---

## 📚 Using Scenarios for Decision Making

### Control Investment Justification

**Example: Ransomware Prevention**

**Current State (No Backup):**
- Scenario: Ransomware Attack
- Vulnerability: 50%
- ALE: €120K

**With Investment (Immutable Backups):**
- Vulnerability: 10% (can restore)
- New ALE: €24K
- Risk Reduction: €96K

**Control Cost:** €30K/year
**Net Benefit:** €66K/year
**ROSI:** 220%

**Decision:** Strong business case for investment

---

## ✅ Best Practices

### Do:
- ✅ Start with preset, then customize
- ✅ Run multiple scenarios
- ✅ Compare before/after control investments
- ✅ Document assumptions
- ✅ Update with actual incident data
- ✅ Use for executive communication

### Don't:
- ❌ Use presets without considering your environment
- ❌ Ignore industry-specific factors
- ❌ Forget to adjust for organization size
- ❌ Run only one scenario
- ❌ Use outdated threat intelligence
- ❌ Present without context

---

## 🎓 Learning from Scenarios

### Key Insights

**From Frequency Analysis:**
- Data breaches happen most often
- System outages are rare but inevitable
- Supply chain attacks are increasing

**From Impact Analysis:**
- Secondary losses often exceed primary
- Regulatory fines can be massive
- Reputation damage is hard to quantify

**From Vulnerability Analysis:**
- DDoS and insider threats have 100% vulnerability
- Device theft has lowest vulnerability (with encryption)
- Zero-days require defense-in-depth

**From Probability Analysis:**
- Supply chain has highest secondary probability
- BEC has lowest secondary impact
- Ransomware secondary impact is moderate

---

## 📖 Additional Resources

### Threat Intelligence Sources
- Verizon DBIR (Data Breach Investigations Report)
- IBM X-Force Threat Intelligence Index
- CrowdStrike Global Threat Report
- Mandiant M-Trends Report

### Industry Benchmarks
- Ponemon Cost of Data Breach Report
- Gartner Security & Risk Management
- SANS Threat Landscape Surveys
- FAIR Institute Case Studies

### Regulatory Guidance
- GDPR (EU data protection)
- CCPA (California privacy)
- HIPAA (healthcare)
- PCI-DSS (payment cards)

---

**These preset scenarios provide realistic starting points for FAIR risk assessments. Customize them based on your specific environment, threat intelligence, and risk tolerance.**

---

*Preset Threat Scenarios Guide - FAIR Risk Analysis Dashboard v1.3*
*Last Updated: November 2024*
