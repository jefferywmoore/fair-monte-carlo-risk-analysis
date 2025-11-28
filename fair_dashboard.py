# -*- coding: utf-8 -*-
"""
FAIR Monte Carlo - Interactive Risk Analysis Dashboard

A web-based interactive tool for running FAIR risk assessments with real-time visualization.
Perfect for client presentations and scenario modeling.

To run: streamlit run fair_dashboard.py
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from fair_monte_carlo import FAIRMonteCarloSimulation, FAIRDistribution
import json

# Page configuration
st.set_page_config(
    page_title="FAIR Risk Analysis Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .metric-container {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    .stAlert {
        background-color: #d4edda;
        border-color: #c3e6cb;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'simulation_run' not in st.session_state:
    st.session_state.simulation_run = False
if 'stats' not in st.session_state:
    st.session_state.stats = None
if 'sim' not in st.session_state:
    st.session_state.sim = None

# Header
st.markdown('<div class="main-header">🛡️ FAIR Risk Analysis Dashboard</div>', unsafe_allow_html=True)
st.markdown("**Interactive Monte Carlo Simulation for Cybersecurity Risk Quantification**")
st.markdown("---")

# Sidebar - Scenario Selection
with st.sidebar:
    # Display logo if it exists
    import os
    if os.path.exists("bare_logo.png"):
        st.image("bare_logo.png", width=150)
    st.header("⚙️ Configuration")
    
    # Preset scenarios
    scenario_preset = st.selectbox(
        "📋 Load Preset Scenario",
        ["Custom", "Ransomware Attack", "Data Breach (GDPR)", "Business Email Compromise", 
         "DDoS Attack", "Insider Threat", "Zero-Day Exploit", "Physical Theft of Device",
         "Critical System Outage", "Supply Chain Compromise"],
        help="Load pre-configured risk scenarios based on common cybersecurity threats. Select 'Custom' to define your own parameters."
    )
    
    st.markdown("---")
    
    # Client information
    st.subheader("👤 Client Information")
    client_name = st.text_input(
        "Client Name", 
        value="Example Company",
        help="The name of the organization being assessed. Used for report generation and documentation."
    )
    annual_revenue = st.number_input(
        "Annual Revenue (€)", 
        min_value=100000, 
        max_value=1000000000, 
        value=5000000, 
        step=100000, 
        format="%d",
        help="Total annual revenue of the organization. Used to calculate risk as a percentage of revenue and determine risk appetite thresholds."
    )
    industry = st.selectbox(
        "Industry", 
        ["Professional Services", "Financial Services", "Healthcare", 
         "E-commerce", "Manufacturing", "Technology", "Other"],
        help="Industry sector of the organization. Helps contextualize risk tolerance and provides industry-specific risk benchmarking."
    )
    
    st.markdown("---")
    
    # Simulation settings
    st.subheader("🔧 Simulation Settings")
    n_simulations = st.select_slider(
        "Number of Simulations",
        options=[1000, 5000, 10000, 20000, 50000],
        value=10000,
        help="Number of Monte Carlo iterations to run. Higher values provide more accurate results but take longer to compute. 10,000 simulations typically provide a good balance of accuracy and speed."
    )
    
    currency = st.selectbox(
        "Currency", 
        ["€", "$", "£", "CHF"], 
        index=0,
        help="Currency symbol for displaying financial values in reports and visualizations."
    )
    
    st.markdown("---")
    
    # Risk Appetite / Tolerance Configuration
    st.subheader("🎚️ Risk Tolerance Settings")
    
    # Preset risk appetite profiles
    risk_profile = st.selectbox(
        "Risk Appetite Profile",
        ["Conservative", "Moderate", "Aggressive", "Custom"],
        index=1,
        help="Pre-configured risk tolerance levels based on industry best practices. Conservative is typical for financial services, Moderate for most organizations, Aggressive for startups. Select 'Custom' to define your own thresholds."
    )
    
    # Set default thresholds based on profile
    if risk_profile == "Conservative":
        default_low = 0.2
        default_moderate = 0.5
    elif risk_profile == "Moderate":
        default_low = 0.5
        default_moderate = 1.0
    elif risk_profile == "Aggressive":
        default_low = 1.0
        default_moderate = 2.0
    else:  # Custom
        default_low = 0.5
        default_moderate = 1.0
    
    # Allow customization
    col_risk1, col_risk2 = st.columns(2)
    with col_risk1:
        low_threshold = st.number_input(
            "Low Risk Threshold (%)",
            min_value=0.01,
            max_value=10.0,
            value=default_low,
            step=0.1,
            disabled=(risk_profile != "Custom"),
            help="ALE as % of annual revenue below this threshold is considered LOW RISK (acceptable). Typical values: 0.2% (conservative), 0.5% (moderate), 1.0% (aggressive)."
        )
    
    with col_risk2:
        moderate_threshold = st.number_input(
            "Moderate Risk Threshold (%)",
            min_value=0.01,
            max_value=10.0,
            value=default_moderate,
            step=0.1,
            disabled=(risk_profile != "Custom"),
            help="ALE as % of annual revenue above this threshold is considered HIGH RISK (requires treatment). Between low and moderate thresholds is MODERATE RISK. Typical values: 0.5% (conservative), 1.0% (moderate), 2.0% (aggressive)."
        )
    
    # Store in session state for use in results
    st.session_state.risk_thresholds = {
        'low': low_threshold,
        'moderate': moderate_threshold,
        'profile': risk_profile
    }
    
    # Show risk tolerance summary
    with st.expander("📊 Your Risk Tolerance Summary"):
        st.markdown(f"""
        **Profile:** {risk_profile}
        
        **Risk Levels (as % of annual revenue):**
        - 🟢 **Low Risk (Acceptable):** < {low_threshold}%
        - 🟡 **Moderate Risk:** {low_threshold}% - {moderate_threshold}%
        - 🔴 **High Risk:** > {moderate_threshold}%
        
        **For your organization (Revenue: {currency}{annual_revenue:,}):**
        - 🟢 Low Risk: < {currency}{annual_revenue * low_threshold / 100:,.0f}
        - 🟡 Moderate Risk: {currency}{annual_revenue * low_threshold / 100:,.0f} - {currency}{annual_revenue * moderate_threshold / 100:,.0f}
        - 🔴 High Risk: > {currency}{annual_revenue * moderate_threshold / 100:,.0f}
        """)


# Load preset values
def load_preset(scenario):
    """
    Load pre-configured risk scenario parameters for common cybersecurity threats.
    
    Args:
        scenario (str): Name of the threat scenario
        
    Returns:
        dict: Dictionary containing TEF, vulnerability, and loss magnitude parameters
    """
    presets = {
        "Ransomware Attack": {
            "tef_min": 100, "tef_mode": 300, "tef_max": 1000,
            "vuln_contact": 0.25, "vuln_action": 0.10, "vuln_rate": 0.35,
            "primary_min": 20000, "primary_mode": 75000, "primary_max": 350000,
            "secondary_min": 10000, "secondary_mode": 40000, "secondary_max": 200000,
            "secondary_prob": 0.35
        },
        "Data Breach (GDPR)": {
            "tef_min": 500, "tef_mode": 1500, "tef_max": 4000,
            "vuln_contact": 0.30, "vuln_action": 0.08, "vuln_rate": 0.25,
            "primary_min": 15000, "primary_mode": 65000, "primary_max": 250000,
            "secondary_min": 20000, "secondary_mode": 80000, "secondary_max": 400000,
            "secondary_prob": 0.50
        },
        "Business Email Compromise": {
            "tef_min": 300, "tef_mode": 800, "tef_max": 2000,
            "vuln_contact": 0.40, "vuln_action": 0.05, "vuln_rate": 0.30,
            "primary_min": 8000, "primary_mode": 40000, "primary_max": 200000,
            "secondary_min": 3000, "secondary_mode": 15000, "secondary_max": 75000,
            "secondary_prob": 0.25
        },
        "DDoS Attack": {
            "tef_min": 15, "tef_mode": 40, "tef_max": 120,
            "vuln_contact": 0.50, "vuln_action": 0.35, "vuln_rate": 1.0,
            "primary_min": 5000, "primary_mode": 25000, "primary_max": 120000,
            "secondary_min": 3000, "secondary_mode": 18000, "secondary_max": 80000,
            "secondary_prob": 0.50
        },
        "Insider Threat": {
            "tef_min": 3, "tef_mode": 10, "tef_max": 30,
            "vuln_contact": 0.60, "vuln_action": 0.15, "vuln_rate": 1.0,
            "primary_min": 15000, "primary_mode": 80000, "primary_max": 400000,
            "secondary_min": 20000, "secondary_mode": 100000, "secondary_max": 600000,
            "secondary_prob": 0.60
        },
        "Zero-Day Exploit": {
            "tef_min": 5, "tef_mode": 20, "tef_max": 75,
            "vuln_contact": 0.20, "vuln_action": 0.50, "vuln_rate": 0.50,
            "primary_min": 30000, "primary_mode": 100000, "primary_max": 500000,
            "secondary_min": 50000, "secondary_mode": 150000, "secondary_max": 800000,
            "secondary_prob": 0.60
        },
        "Physical Theft of Device": {
            "tef_min": 10, "tef_mode": 50, "tef_max": 200,
            "vuln_contact": 0.80, "vuln_action": 0.10, "vuln_rate": 0.15,
            "primary_min": 1000, "primary_mode": 4000, "primary_max": 15000,
            "secondary_min": 5000, "secondary_mode": 25000, "secondary_max": 150000,
            "secondary_prob": 0.30
        },
        "Critical System Outage": {
            "tef_min": 1, "tef_mode": 3, "tef_max": 10,
            "vuln_contact": 1.0, "vuln_action": 1.0, "vuln_rate": 0.80,
            "primary_min": 15000, "primary_mode": 60000, "primary_max": 300000,
            "secondary_min": 10000, "secondary_mode": 50000, "secondary_max": 250000,
            "secondary_prob": 0.50
        },
        "Supply Chain Compromise": {
            "tef_min": 2, "tef_mode": 8, "tef_max": 30,
            "vuln_contact": 0.70, "vuln_action": 0.20, "vuln_rate": 0.25,
            "primary_min": 25000, "primary_mode": 120000, "primary_max": 600000,
            "secondary_min": 50000, "secondary_mode": 200000, "secondary_max": 1000000,
            "secondary_prob": 0.75
        }
    }
    return presets.get(scenario, {
        "tef_min": 100, "tef_mode": 500, "tef_max": 2000,
        "vuln_contact": 0.30, "vuln_action": 0.10, "vuln_rate": 0.30,
        "primary_min": 20000, "primary_mode": 80000, "primary_max": 300000,
        "secondary_min": 10000, "secondary_mode": 50000, "secondary_max": 200000,
        "secondary_prob": 0.40
    })

preset_values = load_preset(scenario_preset if scenario_preset != "Custom" else None)

# Main content area - Parameters
st.header("📊 Risk Scenario Parameters")

# Add informational box explaining the grouping
st.info("💡 **FAIR factors are grouped by source:** 🌍 **External factors** depend on the threat landscape. 🏢 **Internal factors** depend on your organization's posture and costs.")

col1, col2 = st.columns(2)

with col1:
    # EXTERNAL FACTORS (THREAT LANDSCAPE)
    st.markdown("### 🌍 External Factors (Threat Landscape)")
    with st.container(border=True):
        st.markdown("**🎯 Contact Frequency**")
        st.caption("Industry-wide threat activity - NOT organization-specific")
        
        vuln_contact = st.slider(
            "Contact Frequency (%)",
            min_value=0.0, 
            max_value=100.0, 
            value=preset_values["vuln_contact"]*100, 
            step=1.0,
            help="Contact Frequency (CF): The probable frequency that a threat agent will come into contact with your asset or organization's perimeter. This is typically based on industry-wide data (e.g., volume of phishing emails, automated scans). This is EXTERNAL - based on threat actor activity, not your organization."
        ) / 100
        
        st.caption(f"📊 Industry benchmark: {vuln_contact*100:.1f}% contact rate")
    
    st.markdown("---")
    
    # INTERNAL FACTORS (YOUR ORGANIZATION)
    st.markdown("### 🏢 Internal Factors (Your Organization)")
    
    with st.container(border=True):
        st.markdown("**🎯 Threat Event Frequency (TEF)**")
        st.caption("How many times per year are YOU specifically targeted?")
        
        col_tef1, col_tef2 = st.columns(2)
        with col_tef1:
            tef_min = st.number_input(
                "Minimum attempts/year",
                min_value=1, 
                max_value=100000, 
                value=preset_values["tef_min"], 
                step=10,
                help="The minimum probable frequency that this asset will be subjected to threat agent actions (attempted attacks) per year. TEF represents organization-specific threat events, not general threat activity."
            )
            tef_mode = st.number_input(
                "Most likely attempts/year",
                min_value=1, 
                max_value=100000, 
                value=preset_values["tef_mode"], 
                step=10,
                help="The most likely (mode) frequency of threat events per year. This is the peak of your probability distribution and represents your best estimate of typical threat frequency."
            )
        with col_tef2:
            tef_max = st.number_input(
                "Maximum attempts/year",
                min_value=1, 
                max_value=100000, 
                value=preset_values["tef_max"], 
                step=10,
                help="The maximum probable frequency of threat events per year in a worst-case scenario. This represents the upper bound of your uncertainty range."
            )
            st.markdown("")  # Spacing
            vuln_action = st.slider(
                "Probability of Action (%)",
                min_value=0.0, 
                max_value=100.0, 
                value=preset_values["vuln_action"]*100, 
                step=1.0,
                help="Probability of Action (PoA): The probable frequency that, once contact occurs, the threat agent will act upon the asset to cause a threat event. This is organization-specific and reflects the asset's value and the threat agent's motivation. PoA is the crucial factor that scales industry data (CF) to your specific threat events (TEF).",
                key="poa_slider"
            ) / 100
        
        st.caption(f"📈 TEF = CF × PoA = {vuln_contact*100:.1f}% × {vuln_action*100:.1f}% (Your specific threat level)")
    
    with st.container(border=True):
        st.markdown("**🔓 Vulnerability (Your Controls)**")
        st.caption("How effective are YOUR security controls?")
        
        vuln_rate = st.slider(
            "Vulnerability Rate (%)",
            min_value=0.0, 
            max_value=100.0, 
            value=preset_values["vuln_rate"]*100, 
            step=1.0,
            help="Vulnerability: The probability that a threat event will result in a loss event. This is the ratio of Threat Capability to Resistance Strength (control effectiveness). Essentially the inverse of your security controls' effectiveness. This is INTERNAL - depends on YOUR security posture."
        ) / 100
        
        total_vulnerability = vuln_contact * vuln_action * vuln_rate
        
        col_v1, col_v2 = st.columns(2)
        with col_v1:
            st.metric(
                "Total Vulnerability",
                f"{total_vulnerability*100:.3f}%",
                help="The combined probability that a threat event will result in a loss event, calculated as Contact × Action × Vulnerability. This represents the overall likelihood of successful attacks."
            )
        with col_v2:
            expected_lef = tef_mode * total_vulnerability
            st.metric(
                "Expected Loss Events/Year",
                f"{expected_lef:.2f}",
                help="Loss Event Frequency (LEF): The probable frequency that loss events of this type will occur per year. Calculated as TEF × Vulnerability. This is the number of successful attacks you can expect annually."
            )

with col2:
    st.markdown("### 🏢 Internal Factors (Your Organization)")

    with st.container(border=True):
        st.markdown("**💰 Primary Loss Magnitude**")
        st.caption("Direct costs when incident occurs - YOUR organization's costs")
        
        primary_min = st.number_input(
            "Minimum primary loss",
            min_value=100, 
            max_value=10000000, 
            value=preset_values["primary_min"], 
            step=1000,
            help="Primary Loss: The minimum direct loss associated with the initial impact of the loss event (e.g., cost to replace hardware, direct ransom payment, immediate response costs). This is INTERNAL - based on YOUR organization's costs and assets."
        )
        primary_mode = st.number_input(
            "Most likely primary loss",
            min_value=100, 
            max_value=10000000, 
            value=preset_values["primary_mode"], 
            step=1000,
            help="The most likely (mode) value for primary losses. This represents your best estimate of typical direct costs when an incident occurs."
        )
        primary_max = st.number_input(
            "Maximum primary loss",
            min_value=100, 
            max_value=10000000, 
            value=preset_values["primary_max"], 
            step=1000,
            help="The maximum probable primary loss in a worst-case scenario. This represents the upper bound of direct costs you could face from a single incident."
        )
    
    with st.container(border=True):
        st.markdown("**📉 Secondary Loss Magnitude**")
        st.caption("Indirect costs (fines, reputation, etc.) - YOUR organization's exposure")
        
        secondary_min = st.number_input(
            "Minimum secondary loss",
            min_value=0, 
            max_value=10000000, 
            value=preset_values["secondary_min"], 
            step=1000,
            help="Secondary Loss: The minimum indirect losses that occur after the primary event, typically from organizational response and external pressures (e.g., regulatory fines, lawsuits, reputational damage, remediation costs). This is INTERNAL - based on YOUR regulatory environment and reputation value."
        )
        secondary_mode = st.number_input(
            "Most likely secondary loss",
            min_value=0, 
            max_value=10000000, 
            value=preset_values["secondary_mode"], 
            step=1000,
            help="The most likely (mode) value for secondary losses. This represents your best estimate of typical indirect costs following an incident."
        )
        secondary_max = st.number_input(
            "Maximum secondary loss",
            min_value=0, 
            max_value=10000000, 
            value=preset_values["secondary_max"], 
            step=1000,
            help="The maximum probable secondary loss in a worst-case scenario. This represents the upper bound of indirect costs, including worst-case regulatory penalties and reputational damage."
        )
        
        secondary_prob = st.slider(
            "Probability of Secondary Losses (%)",
            min_value=0.0, 
            max_value=100.0, 
            value=preset_values["secondary_prob"]*100, 
            step=5.0,
            help="Secondary Loss Event Frequency: The probable frequency that the primary event will lead to a specific secondary loss event. For example, the probability that a data breach will result in regulatory fines or lawsuits. This is INTERNAL - depends on YOUR regulatory environment and incident response capabilities."
        ) / 100

# Run Simulation Button
st.markdown("---")
col_button1, col_button2, col_button3 = st.columns([1, 1, 1])
with col_button2:
    run_button = st.button("🚀 Run Simulation", type="primary")

if run_button:
    with st.spinner('Running Monte Carlo simulation... This may take a few seconds...'):
        try:
            # Create distributions
            tef = FAIRDistribution(
                dist_type='pert',
                min_val=tef_min,
                mode_val=tef_mode,
                max_val=tef_max
            )

            primary_loss = FAIRDistribution(
                dist_type='lognormal',
                min_val=primary_min,
                mode_val=primary_mode,
                max_val=primary_max
            )

            secondary_loss = FAIRDistribution(
                dist_type='lognormal',
                min_val=secondary_min,
                mode_val=secondary_mode,
                max_val=secondary_max
            )

            # Run simulation
            sim = FAIRMonteCarloSimulation(n_simulations=n_simulations)
            stats = sim.run_simulation(
                tef_dist=tef,
                vuln_prob=total_vulnerability,
                primary_loss_dist=primary_loss,
                secondary_loss_dist=secondary_loss,
                secondary_loss_prob=secondary_prob
            )

            # Store in session state
            st.session_state.simulation_run = True
            st.session_state.stats = stats
            st.session_state.sim = sim

            st.success("✅ Simulation complete!")

        except ValueError as e:
            st.error(f"❌ **Simulation Error**: {str(e)}")
            st.info("Please check your input parameters and ensure they are valid.")
        except Exception as e:
            st.error(f"❌ **Unexpected Error**: {str(e)}")
            st.info("An unexpected error occurred. Please try again or contact support.")

# Display results if simulation has been run
if st.session_state.simulation_run and st.session_state.stats:
    stats = st.session_state.stats
    sim = st.session_state.sim
    
    st.markdown("---")
    st.header("📈 Simulation Results")
    
    # Key metrics
    st.subheader("🎯 Key Risk Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Mean ALE",
            f"{currency}{stats['ale_mean']:,.0f}",
            delta=f"{(stats['ale_mean']/annual_revenue)*100:.2f}% of revenue",
            help="Annual Loss Expectancy (ALE): The mean (average) expected loss per year from this risk scenario. This is calculated as the frequency of loss events multiplied by the magnitude of losses."
        )
    
    with col2:
        st.metric(
            "Median ALE",
            f"{currency}{stats['ale_median']:,.0f}",
            help="The median (middle value) of the annual loss distribution. This represents a typical loss year and is often more representative than the mean for skewed distributions."
        )
    
    with col3:
        st.metric(
            "95th Percentile",
            f"{currency}{stats['percentiles']['95th']:,.0f}",
            help="The loss value that will be exceeded only 5% of the time. This represents a worst-case scenario with 95% confidence and is commonly used for insurance coverage decisions."
        )
    
    with col4:
        st.metric(
            "Loss Event Frequency",
            f"{stats['lef_mean']:.2f}/year",
            help="Loss Event Frequency (LEF): The expected number of successful loss events per year. This is calculated from Threat Event Frequency multiplied by Vulnerability."
        )
    
    # Risk appetite indicator - using configurable thresholds
    ale_pct_revenue = (stats['ale_mean'] / annual_revenue) * 100
    
    # Get thresholds from session state (with defaults if not set)
    thresholds = st.session_state.get('risk_thresholds', {'low': 0.5, 'moderate': 1.0, 'profile': 'Moderate'})
    low_threshold = thresholds['low']
    moderate_threshold = thresholds['moderate']
    
    if ale_pct_revenue > moderate_threshold:
        st.error(f"🔴 **HIGH RISK**: Mean ALE is {ale_pct_revenue:.2f}% of annual revenue (>{moderate_threshold}%). Immediate risk treatment recommended.")
    elif ale_pct_revenue > low_threshold:
        st.warning(f"🟡 **MODERATE RISK**: Mean ALE is {ale_pct_revenue:.2f}% of annual revenue ({low_threshold}%-{moderate_threshold}%). Consider cost-effective controls.")
    else:
        st.success(f"🟢 **LOW RISK (ACCEPTABLE)**: Mean ALE is {ale_pct_revenue:.2f}% of annual revenue (<{low_threshold}%). May accept or implement low-cost controls.")
    
    st.markdown("---")
    
    # Visualizations
    st.subheader("📊 Interactive Visualizations")
    
    # Create tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Distribution", "📈 Exceedance Curve", "🎲 Percentiles", "📉 LEF Analysis"])
    
    with tab1:
        # Annual Loss Distribution
        fig_dist = go.Figure()
        
        annual_losses = sim.results['annual_losses']
        
        fig_dist.add_trace(go.Histogram(
            x=annual_losses,
            nbinsx=50,
            name='Annual Loss',
            marker_color='#2E86AB',
            opacity=0.7
        ))
        
        fig_dist.add_vline(
            x=stats['ale_mean'],
            line_dash="dash",
            line_color="red",
            annotation_text=f"Mean: {currency}{stats['ale_mean']:,.0f}",
            annotation_position="top right"
        )
        
        fig_dist.add_vline(
            x=stats['ale_median'],
            line_dash="dash",
            line_color="orange",
            annotation_text=f"Median: {currency}{stats['ale_median']:,.0f}",
            annotation_position="top left"
        )
        
        # Add risk tolerance threshold lines
        low_threshold_value = annual_revenue * low_threshold / 100
        moderate_threshold_value = annual_revenue * moderate_threshold / 100
        
        fig_dist.add_vline(
            x=low_threshold_value,
            line_dash="dot",
            line_color="green",
            annotation_text=f"Low Risk: {currency}{low_threshold_value:,.0f}",
            annotation_position="bottom left",
            opacity=0.7
        )
        
        fig_dist.add_vline(
            x=moderate_threshold_value,
            line_dash="dot",
            line_color="red",
            annotation_text=f"High Risk: {currency}{moderate_threshold_value:,.0f}",
            annotation_position="bottom right",
            opacity=0.7
        )
        
        fig_dist.update_layout(
            title="Distribution of Annual Losses (with Risk Tolerance Thresholds)",
            xaxis_title=f"Annual Loss ({currency})",
            yaxis_title="Frequency",
            hovermode='x unified',
            height=500
        )
        
        st.plotly_chart(fig_dist)
        
        st.caption(f"🟢 Green line: Low risk threshold ({low_threshold}% of revenue) | 🔴 Red line: High risk threshold ({moderate_threshold}% of revenue)")
    
    with tab2:
        # Exceedance Curve
        sorted_losses = np.sort(annual_losses)
        exceedance_prob = 1 - np.arange(1, len(sorted_losses) + 1) / len(sorted_losses)
        
        fig_exceed = go.Figure()
        
        fig_exceed.add_trace(go.Scatter(
            x=sorted_losses,
            y=exceedance_prob * 100,
            mode='lines',
            name='Exceedance Probability',
            line=dict(color='#A23B72', width=3),
            fill='tozeroy',
            fillcolor='rgba(162, 59, 114, 0.1)'
        ))
        
        # Add percentile markers
        for pct in [95, 99]:
            pct_val = stats['percentiles'][f'{pct}th']
            fig_exceed.add_vline(
                x=pct_val,
                line_dash="dot",
                line_color="red",
                opacity=0.5,
                annotation_text=f"{pct}th: {currency}{pct_val:,.0f}",
                annotation_position="top"
            )
        
        fig_exceed.update_layout(
            title="Loss Exceedance Curve",
            xaxis_title=f"Annual Loss ({currency})",
            yaxis_title="Probability of Exceedance (%)",
            hovermode='x unified',
            height=500
        )
        
        st.plotly_chart(fig_exceed)
        
        st.info("💡 **Interpretation**: This curve shows the probability that annual losses will exceed a given amount. Use the 95th percentile for insurance coverage decisions.")
    
    with tab3:
        # Percentiles Bar Chart
        percentiles_df = pd.DataFrame({
            'Percentile': ['10th', '25th', '50th', '75th', '90th', '95th', '99th'],
            'Value': [stats['percentiles'][p] for p in ['10th', '25th', '50th', '75th', '90th', '95th', '99th']]
        })
        
        fig_pct = go.Figure()
        
        fig_pct.add_trace(go.Bar(
            x=percentiles_df['Percentile'],
            y=percentiles_df['Value'],
            marker_color=['#06A77D', '#06A77D', '#2E86AB', '#2E86AB', '#F18F01', '#A23B72', '#DC143C'],
            text=[f"{currency}{v:,.0f}" for v in percentiles_df['Value']],
            textposition='outside'
        ))
        
        fig_pct.update_layout(
            title="Loss Distribution by Percentile",
            xaxis_title="Percentile",
            yaxis_title=f"Annual Loss ({currency})",
            height=500,
            showlegend=False
        )
        
        st.plotly_chart(fig_pct)

        # Percentile table
        st.subheader("📋 Detailed Percentiles")
        pct_table = pd.DataFrame({
            'Percentile': ['10th', '25th', '50th (Median)', '75th', '90th', '95th', '99th'],
            'Annual Loss': [f"{currency}{stats['percentiles'][p]:,.2f}" for p in ['10th', '25th', '50th', '75th', '90th', '95th', '99th']],
            '% of Revenue': [f"{(stats['percentiles'][p]/annual_revenue)*100:.2f}%" for p in ['10th', '25th', '50th', '75th', '90th', '95th', '99th']]
        })
        st.dataframe(pct_table, hide_index=True)
    
    with tab4:
        # Loss Event Frequency
        lef_samples = sim.results['lef_samples']
        
        fig_lef = go.Figure()
        
        fig_lef.add_trace(go.Histogram(
            x=lef_samples,
            nbinsx=50,
            name='Loss Event Frequency',
            marker_color='#F18F01',
            opacity=0.7
        ))
        
        fig_lef.add_vline(
            x=stats['lef_mean'],
            line_dash="dash",
            line_color="red",
            annotation_text=f"Mean: {stats['lef_mean']:.3f}",
            annotation_position="top right"
        )
        
        fig_lef.update_layout(
            title="Distribution of Loss Event Frequency",
            xaxis_title="Loss Events per Year",
            yaxis_title="Frequency",
            hovermode='x unified',
            height=500
        )
        
        st.plotly_chart(fig_lef)
        
        st.metric(
            "Probability of at least one loss event",
            f"{stats['probability_of_loss']*100:.1f}%",
            help="The probability that at least one successful loss event will occur during the year."
        )
    
    st.markdown("---")
    
    # Recommendations
    st.header("💡 Risk Treatment Recommendations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🛡️ Control Investment Analysis")
        
        # Control scenarios
        control_reduction = st.slider(
            "Estimated Risk Reduction from Controls (%)",
            min_value=0, 
            max_value=95, 
            value=70, 
            step=5,
            help="The expected percentage reduction in Annual Loss Expectancy from implementing security controls. This should be based on the control's effectiveness in reducing either Threat Event Frequency or Vulnerability."
        )
        
        control_cost = st.number_input(
            f"Annual Control Cost ({currency})",
            min_value=0, 
            max_value=1000000, 
            value=25000, 
            step=1000,
            help="The total annual cost of implementing and maintaining the security control, including licensing, personnel, and operational costs."
        )
        
        ale_reduction = stats['ale_mean'] * (control_reduction / 100)
        net_benefit = ale_reduction - control_cost
        rosi = (net_benefit / control_cost * 100) if control_cost > 0 else 0
        
        st.metric(
            "ALE Reduction", 
            f"{currency}{ale_reduction:,.0f}",
            help="The expected annual reduction in losses from implementing this control."
        )
        st.metric(
            "Net Benefit", 
            f"{currency}{net_benefit:,.0f}",
            help="The net annual benefit after subtracting control costs from the ALE reduction (ALE Reduction - Control Cost)."
        )
        st.metric(
            "ROSI", 
            f"{rosi:.0f}%",
            help="Return on Security Investment: The percentage return on the control investment. Calculated as (Net Benefit / Control Cost) × 100. Values >100% indicate strong financial justification."
        )
        
        if rosi > 100:
            st.success(f"✅ **Excellent Investment**: ROSI of {rosi:.0f}% indicates strong value.")
        elif rosi > 0:
            st.info(f"💡 **Positive ROI**: ROSI of {rosi:.0f}% - consider implementation.")
        else:
            st.warning(f"⚠️ **Negative ROI**: ROSI of {rosi:.0f}% - may not be cost-effective.")
    
    with col2:
        st.subheader("🏥 Insurance Recommendation")
        
        st.write("**Recommended Coverage Limits:**")
        st.write(f"- Minimum Coverage: {currency}{stats['percentiles']['90th']:,.0f} (90th percentile)")
        st.write(f"- Recommended Coverage: {currency}{stats['percentiles']['95th']:,.0f} (95th percentile)")
        st.write(f"- Conservative Coverage: {currency}{stats['percentiles']['99th']:,.0f} (99th percentile)")
        
        st.write(f"\n**Suggested Deductible:** {currency}{stats['ale_median']:,.0f} (median ALE)")
        
        # Estimated premium (3-5% of coverage)
        coverage_95 = stats['percentiles']['95th']
        premium_low = coverage_95 * 0.03
        premium_high = coverage_95 * 0.05
        
        st.write(f"\n**Estimated Annual Premium:** {currency}{premium_low:,.0f} - {currency}{premium_high:,.0f}")
        st.caption("(Typically 3-5% of coverage amount for SMBs)")
        
        st.info("💡 **Tip**: Coverage should be set at the 95th percentile to protect against worst-case scenarios while keeping premiums reasonable. The deductible should align with your risk appetite and the median expected loss.")
    
    st.markdown("---")
    
    # Export options
    st.header("💾 Export Results")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Export summary as JSON
        export_data = {
            "client_name": client_name,
            "scenario": scenario_preset,
            "annual_revenue": annual_revenue,
            "industry": industry,
            "simulation_parameters": {
                "n_simulations": n_simulations,
                "tef": {"min": tef_min, "mode": tef_mode, "max": tef_max},
                "vulnerability": total_vulnerability,
                "primary_loss": {"min": primary_min, "mode": primary_mode, "max": primary_max},
                "secondary_loss": {"min": secondary_min, "mode": secondary_mode, "max": secondary_max},
                "secondary_probability": secondary_prob
            },
            "results": stats
        }
        
        json_str = json.dumps(export_data, indent=2, default=str)
        st.download_button(
            label="📄 Download JSON",
            data=json_str,
            file_name=f"{client_name.replace(' ', '_')}_fair_analysis.json",
            mime="application/json",
            help="Export complete analysis results in JSON format for further processing or integration with other tools."
        )
    
    with col2:
        # Export raw data as CSV
        raw_data_df = pd.DataFrame({
            'annual_loss': sim.results['annual_losses'],
            'loss_event_frequency': sim.results['lef_samples'],
            'threat_event_frequency': sim.results['tef_samples'],
            'actual_events': sim.results['actual_events']
        })
        
        csv = raw_data_df.to_csv(index=False)
        st.download_button(
            label="📊 Download CSV",
            data=csv,
            file_name=f"{client_name.replace(' ', '_')}_simulation_data.csv",
            mime="text/csv",
            help="Export raw simulation data (all Monte Carlo iterations) for detailed statistical analysis in Excel or other tools."
        )
    
    with col3:
        # Export summary report
        report = f"""
FAIR RISK ANALYSIS REPORT
{'='*60}

Client: {client_name}
Industry: {industry}
Annual Revenue: {currency}{annual_revenue:,}
Scenario: {scenario_preset}
Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}

RISK METRICS
{'='*60}
Mean ALE: {currency}{stats['ale_mean']:,.2f}
Median ALE: {currency}{stats['ale_median']:,.2f}
Standard Deviation: {currency}{stats['ale_std']:,.2f}

ALE as % of Revenue: {ale_pct_revenue:.2f}%

PERCENTILES
{'='*60}
10th Percentile: {currency}{stats['percentiles']['10th']:,.2f}
25th Percentile: {currency}{stats['percentiles']['25th']:,.2f}
50th Percentile: {currency}{stats['percentiles']['50th']:,.2f}
75th Percentile: {currency}{stats['percentiles']['75th']:,.2f}
90th Percentile: {currency}{stats['percentiles']['90th']:,.2f}
95th Percentile: {currency}{stats['percentiles']['95th']:,.2f}
99th Percentile: {currency}{stats['percentiles']['99th']:,.2f}

LOSS EVENT FREQUENCY
{'='*60}
Mean LEF: {stats['lef_mean']:.4f} events/year
Median LEF: {stats['lef_median']:.4f} events/year
Probability of Loss: {stats['probability_of_loss']*100:.1f}%

SIMULATION PARAMETERS
{'='*60}
Number of Simulations: {n_simulations:,}
Threat Event Frequency: {tef_min}-{tef_mode}-{tef_max}
Vulnerability: {total_vulnerability*100:.3f}%
Primary Loss Range: {currency}{primary_min:,} - {currency}{primary_max:,}
Secondary Loss Range: {currency}{secondary_min:,} - {currency}{secondary_max:,}
Secondary Loss Probability: {secondary_prob*100:.1f}%

Generated by BARE Cybersecurity FAIR Analysis Tool
"""
        
        st.download_button(
            label="📝 Download Report",
            data=report,
            file_name=f"{client_name.replace(' ', '_')}_fair_report.txt",
            mime="text/plain",
            help="Export a formatted text report summarizing key risk metrics and simulation parameters for documentation and presentation."
        )

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem 0;'>
        <p><strong>FAIR Monte Carlo Risk Analysis Dashboard</strong></p>
        <p>Created for BARE Cybersecurity | Version 1.0</p>
        <p>Based on Factor Analysis of Information Risk (FAIR) methodology</p>
    </div>
    """, unsafe_allow_html=True)
