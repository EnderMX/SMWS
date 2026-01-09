#!/usr/bin/env python3
"""
Maldives Cyber Harassment & Stalking Research - Data Analysis
Student: Pop
Module: UFCFJJ-15-M Social Media and Web Science
Date: December 2024
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

# Set style for better-looking plots
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def load_data():
    """Load all datasets"""
    print("Loading datasets...")
    
    primary_data = pd.read_csv('primary_data_harassment_cases.csv')
    secondary_data = pd.read_csv('secondary_data_statistics.csv')
    legislative_data = pd.read_csv('legislative_comparison.csv')
    
    # Convert date column to datetime
    primary_data['Date'] = pd.to_datetime(primary_data['Date'])
    
    return primary_data, secondary_data, legislative_data

def analyze_harassment_types(df):
    """Analyze types of harassment"""
    print("\n=== HARASSMENT TYPES ANALYSIS ===")
    
    harassment_counts = df['Harassment_Type'].value_counts()
    print("\nHarassment Type Distribution:")
    print(harassment_counts)
    
    # Create visualization
    plt.figure(figsize=(12, 6))
    harassment_counts.plot(kind='barh', color='coral')
    plt.title('Types of Cyber Harassment in Maldives (2019-2025)', fontsize=14, fontweight='bold')
    plt.xlabel('Number of Cases', fontsize=12)
    plt.ylabel('Harassment Type', fontsize=12)
    plt.tight_layout()
    plt.savefig('harassment_types.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: harassment_types.png")
    
    return harassment_counts

def analyze_targets(df):
    """Analyze who is being targeted"""
    print("\n=== TARGET ANALYSIS ===")
    
    target_counts = df['Target_Type'].value_counts()
    print("\nTarget Type Distribution:")
    print(target_counts)
    
    # Create pie chart
    plt.figure(figsize=(10, 8))
    colors = sns.color_palette('pastel')[0:len(target_counts)]
    plt.pie(target_counts, labels=target_counts.index, autopct='%1.1f%%', 
            startangle=90, colors=colors, textprops={'fontsize': 10})
    plt.title('Who is Being Targeted by Cyber Harassment?', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('target_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: target_distribution.png")
    
    return target_counts

def analyze_timeline(df):
    """Analyze harassment over time"""
    print("\n=== TIMELINE ANALYSIS ===")
    
    # Group by year
    df['Year'] = df['Date'].dt.year
    yearly_counts = df.groupby('Year').size()
    print("\nCases by Year:")
    print(yearly_counts)
    
    # Create timeline plot
    plt.figure(figsize=(12, 6))
    yearly_counts.plot(kind='line', marker='o', linewidth=2, markersize=8, color='darkblue')
    plt.title('Cyber Harassment Cases Over Time in Maldives', fontsize=14, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Cases', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('timeline_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: timeline_analysis.png")
    
    return yearly_counts

def analyze_platforms(df):
    """Analyze platforms used for harassment"""
    print("\n=== PLATFORM ANALYSIS ===")
    
    platform_counts = df['Platform'].value_counts()
    print("\nPlatform Distribution:")
    print(platform_counts)
    
    # Create bar chart
    plt.figure(figsize=(10, 6))
    platform_counts.plot(kind='bar', color='steelblue')
    plt.title('Platforms Used for Cyber Harassment', fontsize=14, fontweight='bold')
    plt.xlabel('Platform', fontsize=12)
    plt.ylabel('Number of Cases', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('platform_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: platform_distribution.png")
    
    return platform_counts

def visualize_secondary_data(df):
    """Visualize police statistics"""
    print("\n=== POLICE STATISTICS VISUALIZATION ===")
    
    # Extract cybercrime case data
    cybercrime_stats = df[df['Metric'] == 'Total_Cybercrime_Cases']
    
    years = cybercrime_stats['Year'].astype(int).values
    cases = cybercrime_stats['Value'].astype(int).values
    
    # Create visualization
    plt.figure(figsize=(10, 6))
    bars = plt.bar(years, cases, color=['#3498db', '#e74c3c'], width=0.6)
    
    # Add value labels on bars
    for bar, value in zip(bars, cases):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(value)}',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    plt.title('Reported Cybercrime Cases in Maldives: 2023 vs 2024', 
              fontsize=14, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Cases', fontsize=12)
    plt.ylim(0, int(max(cases)) * 1.15)
    
    # Add percentage increase annotation
    plt.annotate('↑ 74.7% Increase', 
                xy=(2024, cases[1]), 
                xytext=(2023.5, cases[1] * 0.7),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=12, color='red', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('police_statistics.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: police_statistics.png")

def compare_legislation(df):
    """Compare Maldives legislation with other countries"""
    print("\n=== LEGISLATIVE COMPARISON ===")
    
    # Create comparison matrix
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Prepare data for heatmap
    countries = df['Country'].values[:6]  # First 6 countries
    laws = ['General_Cybercrime_Law', 'Cyber_Harassment_Law', 
            'Cyber_Stalking_Law', 'Online_Safety_Act']
    
    # Convert Yes/No to 1/0
    matrix = []
    for country in countries:
        row = []
        country_data = df[df['Country'] == country].iloc[0]
        for law in laws:
            value = country_data[law]
            if value == 'Yes':
                row.append(1)
            elif value == 'No':
                row.append(0)
            elif value == 'Partial' or value == 'Limited':
                row.append(0.5)
            else:
                row.append(0)
        matrix.append(row)
    
    # Create heatmap
    sns.heatmap(matrix, annot=True, fmt='.1f', cmap='RdYlGn', 
                xticklabels=[l.replace('_', ' ') for l in laws],
                yticklabels=countries, cbar_kws={'label': 'Coverage'},
                vmin=0, vmax=1, linewidths=1, linecolor='black')
    
    plt.title('Cybercrime Legislation Comparison: Maldives vs Regional Countries', 
              fontsize=14, fontweight='bold', pad=20)
    plt.xlabel('Type of Law', fontsize=12)
    plt.ylabel('Country', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('legislative_comparison.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: legislative_comparison.png")

def generate_summary_statistics(primary_df, secondary_df):
    """Generate summary statistics for the poster"""
    print("\n=== SUMMARY STATISTICS ===")
    print(f"Total harassment cases documented: {len(primary_df)}")
    print(f"Date range: {primary_df['Date'].min().strftime('%Y-%m-%d')} to {primary_df['Date'].max().strftime('%Y-%m-%d')}")
    print(f"Most common harassment type: {primary_df['Harassment_Type'].mode()[0]}")
    print(f"Most targeted group: {primary_df['Target_Type'].mode()[0]}")
    print(f"\nPolice reported cases (2024): 173 (↑74.7% from 2023)")
    print(f"Financial scam losses (2022): $2.2 million (1,360 cases)")
    print(f"Female politicians shutting accounts: 25%")
    print(f"Female journalists facing online violence: 60%")
    
    # Create summary infographic data
    summary_stats = {
        'Total_Cases_Documented': len(primary_df),
        'Police_Cases_2024': 173,
        'Increase_Percentage': 74.7,
        'Financial_Loss_2022_USD': 2200000,
        'Female_Politicians_Affected_Pct': 25,
        'Female_Journalists_Violence_Pct': 60,
        'Countries_With_Better_Laws': 5,  # Sri Lanka, Malaysia, India, Bangladesh, Pakistan
        'Legislative_Gap': 'YES'
    }
    
    # Save summary
    pd.DataFrame([summary_stats]).to_csv('summary_statistics.csv', index=False)
    print("\n✓ Saved: summary_statistics.csv")

def main():
    """Main analysis function"""
    print("=" * 60)
    print("MALDIVES CYBER HARASSMENT & STALKING ANALYSIS")
    print("=" * 60)
    
    # Load data
    primary_df, secondary_df, legislative_df = load_data()
    
    # Run all analyses
    print("\nAnalyzing primary data...")
    analyze_harassment_types(primary_df)
    analyze_targets(primary_df)
    analyze_timeline(primary_df)
    analyze_platforms(primary_df)
    
    print("\nAnalyzing secondary data...")
    visualize_secondary_data(secondary_df)
    
    print("\nAnalyzing legislation...")
    compare_legislation(legislative_df)
    
    print("\nGenerating summary statistics...")
    generate_summary_statistics(primary_df, secondary_df)
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE!")
    print("=" * 60)
    print("\nGenerated files:")
    print("  - harassment_types.png")
    print("  - target_distribution.png")
    print("  - timeline_analysis.png")
    print("  - platform_distribution.png")
    print("  - police_statistics.png")
    print("  - legislative_comparison.png")
    print("  - summary_statistics.csv")
    print("\nThese visualizations are ready for your poster!")

if __name__ == "__main__":
    main()
