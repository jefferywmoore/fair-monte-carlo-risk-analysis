# UI Reorganization: External vs Internal Factors

## 🎯 Why This Change Matters

In FAIR risk analysis, it's critical to understand which factors you can control (internal to your organization) versus which you cannot (external threat landscape). This UI reorganization makes this distinction crystal clear.

---

## 📊 New UI Layout Structure

### Before (Original Layout)
```
┌─────────────────────────────────────────────────────────────┐
│  Column 1                    │  Column 2                    │
├──────────────────────────────┼──────────────────────────────┤
│  🎯 TEF (min/mode/max)       │  💰 Primary Loss             │
│                              │                              │
│  🔓 Vulnerability            │  📉 Secondary Loss           │
│    - Contact Frequency       │                              │
│    - Probability of Action   │                              │
│    - Vulnerability Rate      │                              │
└──────────────────────────────┴──────────────────────────────┘
```
**Problem:** Doesn't show which factors are external vs internal

### After (New Layout)
```
┌─────────────────────────────────────────────────────────────┐
│  Column 1                    │  Column 2                    │
├──────────────────────────────┼──────────────────────────────┤
│  🌍 EXTERNAL FACTORS         │  🏢 INTERNAL FACTORS         │
│  ┌────────────────────────┐  │  ┌────────────────────────┐  │
│  │ 🎯 Contact Frequency   │  │  │ 💰 Primary Loss        │  │
│  │   (Industry-wide)      │  │  │   (Your costs)         │  │
│  └────────────────────────┘  │  └────────────────────────┘  │
│                              │                              │
│  🏢 INTERNAL FACTORS         │  ┌────────────────────────┐  │
│  ┌────────────────────────┐  │  │ 📉 Secondary Loss      │  │
│  │ 🎯 TEF                 │  │  │   (Your exposure)      │  │
│  │   - Min/Mode/Max       │  │  └────────────────────────┘  │
│  │   - Prob of Action     │  │                              │
│  └────────────────────────┘  │                              │
│                              │                              │
│  ┌────────────────────────┐  │                              │
│  │ 🔓 Vulnerability       │  │                              │
│  │   (Your controls)      │  │                              │
│  └────────────────────────┘  │                              │
└──────────────────────────────┴──────────────────────────────┘
```
**Benefit:** Clear visual separation of controllable vs uncontrollable factors

---

## 🌍 External Factors (What You Can't Control)

### Contact Frequency (CF)
**Location:** Column 1, Top section
**Visual Container:** Bordered box with 🌍 icon
**What It Is:** Industry-wide threat volume
**Why It's External:**
- Based on global/industry threat intelligence
- Same for all organizations in your sector
- You can't stop threat actors from existing
- You can measure it, but not change it

**Data Sources:**
- Threat intelligence feeds
- Industry reports (Verizon DBIR, etc.)
- Security vendor statistics
- ISAC/ISAO sharing groups

**Example Values:**
- Financial sector phishing: 10,000 attempts/employee/year
- Healthcare ransomware: 500 campaigns/year industry-wide
- Retail DDoS: 1,000 attacks/year in e-commerce

**Caption in UI:** "Industry-wide threat activity - NOT organization-specific"

---

## 🏢 Internal Factors (What You CAN Control)

### 1. Probability of Action (PoA)
**Location:** Column 1, TEF container
**Visual:** Slider within TEF bordered box
**What It Is:** How attractive YOUR organization is as a target
**Why It's Internal:**
- Depends on your organization's profile
- Your data/assets value to attackers
- Your public presence and reputation
- Can be influenced by security investments

**Control Mechanisms:**
- Reduce digital footprint
- Improve security hygiene (no low-hanging fruit)
- Threat deception/decoying
- Security awareness (less "clickable")

**Example Values:**
- High-profile bank: 30-50% (very attractive)
- Small manufacturing: 5-10% (less attractive)
- Government agency: 60-80% (nation-state targets)

---

### 2. Threat Event Frequency (TEF)
**Location:** Column 1, TEF container
**Visual:** Three number inputs (min/mode/max)
**What It Is:** Actual attacks targeting YOUR organization
**Why It's Partially Internal:**
- Calculated from CF × PoA
- CF is external (can't control)
- PoA is internal (can influence)
- Therefore TEF is partially controllable

**Formula Display:** "TEF = CF × PoA = 25% × 10% = 2.5% (Your specific threat level)"

**How to Control:**
- Reduce PoA (see above)
- Makes your organization less attractive
- Can't eliminate, but can reduce

---

### 3. Vulnerability
**Location:** Column 1, Bottom container
**Visual:** Slider in bordered box
**What It Is:** Probability an attack succeeds against YOUR controls
**Why It's Internal:**
- Directly reflects YOUR security posture
- YOUR control effectiveness
- YOUR patch management
- YOUR security architecture

**Control Mechanisms:** (Most Controllable Factor!)
- Deploy better security controls
- Improve patch management
- Security architecture improvements
- Security awareness training
- Incident response capabilities

**Example Values:**
- Excellent security: 5-10% vulnerability
- Good security: 15-25% vulnerability
- Average security: 30-40% vulnerability
- Poor security: 50-70% vulnerability
- No controls: 90-100% vulnerability

**Caption in UI:** "How effective are YOUR security controls?"

---

### 4. Primary Loss Magnitude
**Location:** Column 2, Top container
**Visual:** Three number inputs in bordered box
**What It Is:** Direct costs when incident occurs in YOUR organization
**Why It's Internal:**
- Based on YOUR assets and infrastructure
- YOUR replacement costs
- YOUR labor costs
- YOUR operational impact

**Control Mechanisms:**
- Asset inventory management
- Reduce single points of failure
- Improve backup/recovery capabilities
- Reduce downtime through resilience

**Example Values (vary by organization):**
- Small business ransomware: €5K-50K
- Enterprise data breach: €100K-1M
- Critical infrastructure attack: €1M-10M+

**Caption in UI:** "Direct costs when incident occurs - YOUR organization's costs"

---

### 5. Secondary Loss Magnitude
**Location:** Column 2, Bottom container
**Visual:** Three number inputs + probability slider
**What It Is:** Indirect costs following an incident in YOUR environment
**Why It's Internal:**
- YOUR regulatory environment (GDPR, HIPAA, etc.)
- YOUR reputation value
- YOUR customer contracts (SLAs, penalties)
- YOUR incident response maturity

**Control Mechanisms:**
- Improve compliance posture
- Better incident response plans
- Communication strategies
- Legal preparedness
- Cyber insurance

**Example Values (highly organization-specific):**
- GDPR fine: up to 4% annual revenue
- Healthcare breach: $408/record average
- Reputational damage: highly variable
- Customer churn: 20-30% customer loss

**Caption in UI:** "Indirect costs - YOUR organization's exposure"

---

## 🎨 Visual Design Elements

### External Factor Container
```
┌─────────────────────────────────┐
│ 🌍 EXTERNAL FACTORS              │
│ (Threat Landscape)               │
├─────────────────────────────────┤
│ [Content with gray/blue tint]   │
│                                  │
│ Caption: "Industry-wide data"   │
└─────────────────────────────────┘
```

### Internal Factor Container
```
┌─────────────────────────────────┐
│ 🏢 INTERNAL FACTORS              │
│ (Your Organization)              │
├─────────────────────────────────┤
│ [Content with green/blue tint]  │
│                                  │
│ Caption: "Your specific values" │
└─────────────────────────────────┘
```

### Color Coding
- **External (🌍):** Light blue/gray background (suggests "sky" - out of your control)
- **Internal (🏢):** Light green/teal background (suggests "building" - your domain)
- **Containers:** Border with st.container(border=True) for clear grouping
- **Icons:** Consistent use of 🌍 for external, 🏢 for internal

---

## 🎓 Educational Benefits

### 1. Immediate Clarity
**Before:** User confused about why CF is in "Vulnerability" section
**After:** User sees CF is external, everything else internal
**Benefit:** Clearer mental model of FAIR

### 2. Control Focus
**Before:** Not obvious which factors are actionable
**After:** Clear visual distinction between controllable/uncontrollable
**Benefit:** Better investment decisions

### 3. Risk Communication
**Before:** Hard to explain to executives
**After:** "This is the threat landscape (external), this is our posture (internal)"
**Benefit:** Executive understanding

### 4. ROI Justification
**Before:** Unclear where controls make a difference
**After:** "We can't change CF, but we CAN improve vulnerability from 30% to 10%"
**Benefit:** Clear business case

---

## 💬 User Interface Copy

### Information Banner (Top)
```
💡 FAIR factors are grouped by source: 
🌍 External factors depend on the threat landscape. 
🏢 Internal factors depend on your organization's posture and costs.
```

### Section Headers

**External Section:**
```
🌍 External Factors (Threat Landscape)
```

**Internal Section:**
```
🏢 Internal Factors (Your Organization)
```

### Container Captions

**Contact Frequency:**
```
Industry-wide threat activity - NOT organization-specific
📊 Industry benchmark: 25.0% contact rate
```

**Threat Event Frequency:**
```
How many times per year are YOU specifically targeted?
📈 TEF = CF × PoA = 25.0% × 10.0% (Your specific threat level)
```

**Vulnerability:**
```
How effective are YOUR security controls?
```

**Primary Loss:**
```
Direct costs when incident occurs - YOUR organization's costs
```

**Secondary Loss:**
```
Indirect costs (fines, reputation, etc.) - YOUR organization's exposure
```

---

## 🔄 Data Flow Visualization

### The External → Internal Flow
```
🌍 EXTERNAL
    ↓
    Contact Frequency (Industry data)
    ↓
    × (multiply by)
    ↓
🏢 INTERNAL
    ↓
    Probability of Action (Your attractiveness)
    ↓
    = TEF (Your specific threats)
    ↓
    × (multiply by)
    ↓
    Vulnerability (Your control effectiveness)
    ↓
    = LEF (Your actual losses)
    ↓
    × (multiply by)
    ↓
    Loss Magnitude (Your costs)
    ↓
    = ALE (Your annual loss expectancy)
```

---

## 📊 Comparison Table

| Factor | Type | Icon | Source | Controllability | Time to Change |
|--------|------|------|--------|----------------|----------------|
| Contact Frequency | External | 🌍 | Threat Intel | ❌ None | N/A (monitor only) |
| Probability of Action | Internal | 🏢 | Your profile | ⚠️ Partial | Months-Years |
| Vulnerability | Internal | 🏢 | Your controls | ✅ High | Weeks-Months |
| Primary Loss | Internal | 🏢 | Your assets | ⚠️ Partial | Months-Years |
| Secondary Loss | Internal | 🏢 | Your exposure | ⚠️ Partial | Months-Years |

---

## 🎯 User Workflow Improvements

### Old Workflow
1. User enters Contact Frequency
2. User confused why this is in "Vulnerability" section
3. User doesn't understand relationship to other factors
4. User frustrated by lack of structure

### New Workflow
1. User sees "External Factors" section first
2. User understands CF is industry data (can't control)
3. User moves to "Internal Factors"
4. User clearly sees what they CAN control
5. User makes better risk treatment decisions

---

## 💡 Teaching Moments

### Moment 1: "Why can't I control CF?"
**UI Response:** 🌍 icon + "Industry-wide threat activity - NOT organization-specific"
**Learning:** Contact Frequency is about the threat landscape, not your organization

### Moment 2: "What CAN I control?"
**UI Response:** 🏢 icon appears on multiple factors with captions about "YOUR controls", "YOUR costs"
**Learning:** Most FAIR factors are internal and controllable

### Moment 3: "How do I reduce risk?"
**UI Response:** Clear visual grouping shows internal factors as the lever points
**Learning:** Focus investments on vulnerability, PoA, and loss magnitude reductions

---

## 🚀 Implementation Details

### Streamlit Components Used
```python
# Information banner
st.info("💡 FAIR factors grouped by source...")

# Container with border
with st.container(border=True):
    st.markdown("**🌍 Contact Frequency**")
    st.caption("Industry-wide threat activity")
    # ... inputs ...

# Section headers
st.markdown("### 🌍 External Factors (Threat Landscape)")
st.markdown("### 🏢 Internal Factors (Your Organization)")
```

### CSS Styling (Optional Enhancement)
```css
/* External factor containers */
.external-factor {
    background-color: #e3f2fd;  /* Light blue */
    border-left: 4px solid #2196f3;
}

/* Internal factor containers */
.internal-factor {
    background-color: #e8f5e9;  /* Light green */
    border-left: 4px solid #4caf50;
}
```

---

## 📚 Documentation Updates

### Updated in This Package
- ✅ fair_dashboard.py - UI reorganized with containers
- ✅ FAIR_QUICK_REFERENCE.md - Added external vs internal explanations
- ✅ Help text - Updated with "This is EXTERNAL" / "This is INTERNAL" notes
- ✅ This guide - Complete explanation of the reorganization

### Recommended Training Updates
1. Update screenshots in training materials
2. Add section on external vs internal distinction
3. Emphasize controllability in risk treatment discussions
4. Use new layout in client presentations

---

## ✅ Quality Checks

### Verify the Reorganization Works
- [ ] External factor (CF) is visually separate at top
- [ ] Internal factors clearly marked with 🏢
- [ ] Captions explain data source ("Industry-wide" vs "Your organization's")
- [ ] Containers have borders for clear grouping
- [ ] Help text updated with external/internal notes
- [ ] Mathematical relationships still clear (TEF = CF × PoA)
- [ ] No confusion about what to control vs what to measure

---

## 🎓 Key Takeaways

### For Users
1. **You can't control the threat landscape** (CF) - only measure it
2. **You CAN control your security posture** (Vulnerability, PoA partially)
3. **You CAN control your loss magnitude** (partially through architecture)
4. **Investment decisions should focus on internal factors**

### For Consultants
1. **Better client education** - clear visual distinction
2. **Stronger ROI justification** - "we're improving these controllable factors"
3. **Reduced confusion** - fewer questions about CF vs PoA
4. **Professional presentation** - organized, logical flow

### For the Organization
1. **Standardized approach** - everyone uses same mental model
2. **Better decision-making** - clear about what's actionable
3. **Improved risk communication** - executives understand controllability
4. **Strategic focus** - investments target internal factors

---

**This reorganization transforms the dashboard from a calculation tool into an educational platform that teaches FAIR principles through its UI structure.**

---

*UI Reorganization Guide - November 2024*
*FAIR Risk Analysis Dashboard v1.2 - External vs Internal Factor Grouping*
