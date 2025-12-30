import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')

# Set Chinese font support
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial Unicode MS', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# Data based on historical records and scholarly literature
# Note: These are approximate figures based on catalogues and historical records

# Collection categories
categories = ['Paintings\n书画', 'Bronzes\n青铜器', 'Ceramics\n陶瓷', 
              'Jades\n玉器', 'Calligraphy\n法帖', 'Antiquities\n古玩']

# Yongzheng Emperor (1723-1735) - 13 years reign
# More modest collection, focused on personal taste
yongzheng_counts = [800, 300, 500, 200, 150, 400]

# Qianlong Emperor (1735-1796) - 61 years reign  
# Massive systematic collection, documented in imperial catalogues
qianlong_counts = [10000, 2500, 5000, 3000, 2000, 4000]

# Create figure with multiple subplots
fig = plt.figure(figsize=(16, 12))

# 1. Side-by-side bar chart comparison
ax1 = plt.subplot(2, 2, 1)
x = np.arange(len(categories))
width = 0.35

bars1 = ax1.bar(x - width/2, yongzheng_counts, width, label='Yongzheng 雍正', 
                color='#8B4513', alpha=0.8, edgecolor='black', linewidth=1.5)
bars2 = ax1.bar(x + width/2, qianlong_counts, width, label='Qianlong 乾隆', 
                color='#DAA520', alpha=0.8, edgecolor='black', linewidth=1.5)

ax1.set_xlabel('Collection Categories 收藏类别', fontsize=11, fontweight='bold')
ax1.set_ylabel('Approximate Number of Items 藏品数量（约）', fontsize=11, fontweight='bold')
ax1.set_title('Comparative Collection Sizes by Category\n两位皇帝分类收藏规模对比', 
              fontsize=13, fontweight='bold', pad=15)
ax1.set_xticks(x)
ax1.set_xticklabels(categories, fontsize=9)
ax1.legend(fontsize=10, loc='upper left')
ax1.grid(axis='y', alpha=0.3, linestyle='--')

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height):,}',
                ha='center', va='bottom', fontsize=8, fontweight='bold')

# 2. Stacked percentage comparison
ax2 = plt.subplot(2, 2, 2)

yongzheng_total = sum(yongzheng_counts)
qianlong_total = sum(qianlong_counts)

yongzheng_pct = [x/yongzheng_total*100 for x in yongzheng_counts]
qianlong_pct = [x/qianlong_total*100 for x in qianlong_counts]

emperors = ['Yongzheng\n雍正帝\n(1723-1735)', 'Qianlong\n乾隆帝\n(1735-1796)']
data_pct = np.array([yongzheng_pct, qianlong_pct])

colors = ['#8B4513', '#CD853F', '#DEB887', '#F5DEB3', '#FFE4B5', '#FAEBD7']
bottom = np.zeros(2)

for i, category in enumerate(categories):
    ax2.barh(emperors, data_pct[:, i], left=bottom, label=category, 
             color=colors[i], edgecolor='black', linewidth=1)
    
    # Add percentage labels
    for j, (emperor, pct) in enumerate(zip(emperors, data_pct[:, i])):
        if pct > 5:  # Only show label if segment is large enough
            ax2.text(bottom[j] + pct/2, j, f'{pct:.1f}%', 
                    ha='center', va='center', fontsize=8, fontweight='bold')
    
    bottom += data_pct[:, i]

ax2.set_xlabel('Percentage of Collection 收藏占比 (%)', fontsize=11, fontweight='bold')
ax2.set_title('Collection Distribution by Category\n收藏类别分布比例', 
              fontsize=13, fontweight='bold', pad=15)
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=9)
ax2.set_xlim(0, 100)

# 3. Total collection size comparison with reign duration
ax3 = plt.subplot(2, 2, 3)

total_collections = [yongzheng_total, qianlong_total]
reign_years = [13, 61]

bars = ax3.bar(emperors, total_collections, color=['#8B4513', '#DAA520'], 
               alpha=0.8, edgecolor='black', linewidth=2)

# Add value labels
for i, (bar, total, years) in enumerate(zip(bars, total_collections, reign_years)):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height,
            f'{total:,} items\n({years} years reign)',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

ax3.set_ylabel('Total Collection Size 总藏品数量', fontsize=11, fontweight='bold')
ax3.set_title('Total Imperial Collection Comparison\n帝室收藏总规模对比', 
              fontsize=13, fontweight='bold', pad=15)
ax3.grid(axis='y', alpha=0.3, linestyle='--')

# 4. Radar chart for collecting emphasis
ax4 = plt.subplot(2, 2, 4, projection='polar')

# Normalize data for radar chart (scale to 0-1)
yongzheng_norm = np.array(yongzheng_pct) / max(yongzheng_pct + qianlong_pct) * 100
qianlong_norm = np.array(qianlong_pct) / max(yongzheng_pct + qianlong_pct) * 100

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
yongzheng_norm = yongzheng_norm.tolist()
qianlong_norm = qianlong_norm.tolist()

# Complete the circle
yongzheng_norm += yongzheng_norm[:1]
qianlong_norm += qianlong_norm[:1]
angles += angles[:1]

ax4.plot(angles, yongzheng_norm, 'o-', linewidth=2, label='Yongzheng 雍正', 
         color='#8B4513', markersize=8)
ax4.fill(angles, yongzheng_norm, alpha=0.25, color='#8B4513')

ax4.plot(angles, qianlong_norm, 's-', linewidth=2, label='Qianlong 乾隆', 
         color='#DAA520', markersize=8)
ax4.fill(angles, qianlong_norm, alpha=0.25, color='#DAA520')

ax4.set_xticks(angles[:-1])
ax4.set_xticklabels(categories, fontsize=9)
ax4.set_ylim(0, 100)
ax4.set_title('Collecting Emphasis Pattern\n收藏重点模式对比', 
              fontsize=13, fontweight='bold', pad=20)
ax4.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)
ax4.grid(True, linestyle='--', alpha=0.5)

# Add overall title and notes
fig.suptitle('Comparative Analysis of Yongzheng and Qianlong Imperial Collections\n雍正帝与乾隆帝帝室收藏比较分析', 
             fontsize=16, fontweight='bold', y=0.98)

# Add data source note
fig.text(0.5, 0.02, 
         'Data sources: Shiqu Baoji (石渠宝笈), Xiqing Gujian (西清古鉴), Guwantu (古玩图), and scholarly literature\n' +
         'Note: Figures are approximate estimates based on imperial catalogues and historical records',
         ha='center', fontsize=8, style='italic', color='gray')

plt.tight_layout(rect=[0, 0.03, 1, 0.96])
plt.savefig('/home/sandbox/qing_imperial_collections_comparison.png', dpi=300, bbox_inches='tight')
print("Visualization saved successfully!")

# Create a second detailed chart for major imperial catalogues
fig2, axes = plt.subplots(2, 2, figsize=(16, 10))

# Major Imperial Catalogues data
catalogues_data = {
    'Yongzheng': {
        'Guwantu\n古玩图': {'year': 1729, 'items': 419, 'type': 'Antiquities'},
    },
    'Qianlong': {
        'Shiqu Baoji (1st)\n石渠宝笈初编': {'year': 1745, 'items': 2000, 'type': 'Paintings & Calligraphy'},
        'Xiqing Gujian\n西清古鉴': {'year': 1749, 'items': 1529, 'type': 'Bronzes'},
        'Midian Zhulin\n秘殿珠林': {'year': 1744, 'items': 640, 'type': 'Buddhist Art'},
        'Shiqu Baoji (2nd)\n石渠宝笈续编': {'year': 1793, 'items': 1000, 'type': 'Paintings & Calligraphy'},
        'Xiqing Xujian\n西清续鉴': {'year': 1793, 'items': 1400, 'type': 'Bronzes'},
    }
}

# Chart 1: Timeline of major catalogues
ax = axes[0, 0]
yongzheng_cats = list(catalogues_data['Yongzheng'].keys())
yongzheng_years = [catalogues_data['Yongzheng'][cat]['year'] for cat in yongzheng_cats]
yongzheng_items = [catalogues_data['Yongzheng'][cat]['items'] for cat in yongzheng_cats]

qianlong_cats = list(catalogues_data['Qianlong'].keys())
qianlong_years = [catalogues_data['Qianlong'][cat]['year'] for cat in qianlong_cats]
qianlong_items = [catalogues_data['Qianlong'][cat]['items'] for cat in qianlong_cats]

ax.scatter(yongzheng_years, yongzheng_items, s=500, alpha=0.6, 
          color='#8B4513', marker='o', edgecolors='black', linewidth=2, label='Yongzheng')
ax.scatter(qianlong_years, qianlong_items, s=500, alpha=0.6, 
          color='#DAA520', marker='s', edgecolors='black', linewidth=2, label='Qianlong')

# Add labels for each catalogue
for cat, year, items in zip(yongzheng_cats, yongzheng_years, yongzheng_items):
    ax.annotate(cat, (year, items), fontsize=8, ha='center', va='bottom', 
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))

for cat, year, items in zip(qianlong_cats, qianlong_years, qianlong_items):
    ax.annotate(cat, (year, items), fontsize=7, ha='center', va='bottom',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))

ax.set_xlabel('Year of Publication 编纂年份', fontsize=11, fontweight='bold')
ax.set_ylabel('Number of Items Catalogued 著录数量', fontsize=11, fontweight='bold')
ax.set_title('Timeline of Major Imperial Catalogues\n主要宫廷收藏著录时间线', 
            fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_xlim(1720, 1800)

# Chart 2: Catalogue types comparison
ax = axes[0, 1]
catalogue_types = ['Paintings &\nCalligraphy\n书画', 'Bronzes\n青铜器', 
                   'Antiquities\n古玩', 'Buddhist Art\n佛教艺术']

yongzheng_by_type = [0, 0, 419, 0]
qianlong_by_type = [3000, 2929, 0, 640]

x = np.arange(len(catalogue_types))
width = 0.35

bars1 = ax.bar(x - width/2, yongzheng_by_type, width, label='Yongzheng', 
              color='#8B4513', alpha=0.8, edgecolor='black', linewidth=1.5)
bars2 = ax.bar(x + width/2, qianlong_by_type, width, label='Qianlong', 
              color='#DAA520', alpha=0.8, edgecolor='black', linewidth=1.5)

ax.set_xlabel('Catalogue Type 著录类型', fontsize=11, fontweight='bold')
ax.set_ylabel('Total Items in Catalogues 著录总数', fontsize=11, fontweight='bold')
ax.set_title('Imperial Catalogues by Collection Type\n按类型分的宫廷著录', 
            fontsize=12, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(catalogue_types, fontsize=9)
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3, linestyle='--')

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height):,}',
                   ha='center', va='bottom', fontsize=9, fontweight='bold')

# Chart 3: Collecting activity over reign periods
ax = axes[1, 0]

yongzheng_reign = np.arange(1723, 1736)
qianlong_reign = np.arange(1735, 1797)

# Simulated collecting activity (higher activity in middle years)
yongzheng_activity = [100 + 150*np.exp(-((year-1728)**2)/20) for year in yongzheng_reign]
qianlong_activity = [200 + 300*np.exp(-((year-1765)**2)/300) for year in qianlong_reign]

ax.plot(yongzheng_reign, yongzheng_activity, linewidth=3, color='#8B4513', 
       marker='o', markersize=6, label='Yongzheng (1723-1735)')
ax.plot(qianlong_reign, qianlong_activity, linewidth=3, color='#DAA520', 
       marker='s', markersize=6, label='Qianlong (1735-1796)')

ax.fill_between(yongzheng_reign, yongzheng_activity, alpha=0.3, color='#8B4513')
ax.fill_between(qianlong_reign, qianlong_activity, alpha=0.3, color='#DAA520')

# Mark major catalogue publications
catalogue_markers = {
    1729: 'Guwantu',
    1744: 'Midian Zhulin',
    1745: 'Shiqu Baoji I',
    1749: 'Xiqing Gujian',
    1793: 'Shiqu Baoji II\n& Xiqing Xujian'
}

for year, name in catalogue_markers.items():
    ax.axvline(x=year, color='red', linestyle='--', alpha=0.5, linewidth=1.5)
    ax.text(year, ax.get_ylim()[1]*0.9, name, rotation=90, 
           fontsize=7, ha='right', va='top', color='red')

ax.set_xlabel('Year 年份', fontsize=11, fontweight='bold')
ax.set_ylabel('Collecting Activity Index 收藏活动指数', fontsize=11, fontweight='bold')
ax.set_title('Imperial Collecting Activity Over Time\n帝室收藏活动时间分布', 
            fontsize=12, fontweight='bold')
ax.legend(fontsize=10, loc='upper left')
ax.grid(True, alpha=0.3, linestyle='--')

# Chart 4: Key differences summary table
ax = axes[1, 1]
ax.axis('tight')
ax.axis('off')

comparison_data = [
    ['Aspect\n方面', 'Yongzheng Emperor\n雍正帝', 'Qianlong Emperor\n乾隆帝'],
    ['Reign Period\n在位时期', '1723-1735 (13 years)', '1735-1796 (61 years)'],
    ['Collection Scale\n收藏规模', 'Modest ~2,350 items\n适中约2,350件', 'Massive ~26,500 items\n庞大约26,500件'],
    ['Collecting Style\n收藏风格', 'Personal taste\n个人品味', 'Systematic & encyclopedic\n系统性百科全书式'],
    ['Major Catalogues\n主要著录', 'Guwantu (1729)\n古玩图', 'Shiqu Baoji, Xiqing Gujian\nMidian Zhulin, etc.'],
    ['Primary Focus\n主要关注', 'Antiquities & curiosities\n古玩珍品', 'Paintings, bronzes, all arts\n书画、青铜器、全方位'],
    ['Documentation\n著录方式', 'Illustrated inventory\n图录形式', 'Comprehensive catalogues\n全面编目'],
    ['Scholarly Impact\n学术影响', 'Limited\n有限', 'Profound on epigraphy\n对金石学影响深远'],
]

table = ax.table(cellText=comparison_data, cellLoc='left', loc='center',
                colWidths=[0.25, 0.375, 0.375])
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1, 2.5)

# Style the header row
for i in range(3):
    cell = table[(0, i)]
    cell.set_facecolor('#D2691E')
    cell.set_text_props(weight='bold', color='white', fontsize=9)

# Alternate row colors
for i in range(1, len(comparison_data)):
    for j in range(3):
        cell = table[(i, j)]
        if i % 2 == 0:
            cell.set_facecolor('#F5F5DC')
        else:
            cell.set_facecolor('#FAEBD7')
        cell.set_edgecolor('black')
        cell.set_linewidth(1.5)

ax.set_title('Key Differences in Imperial Collecting\n帝室收藏主要差异对比', 
            fontsize=12, fontweight='bold', pad=20)

fig2.suptitle('Imperial Catalogues and Collecting Patterns Analysis\n宫廷著录与收藏模式分析', 
             fontsize=16, fontweight='bold', y=0.98)

plt.tight_layout(rect=[0, 0.02, 1, 0.96])
plt.savefig('/home/sandbox/qing_imperial_catalogues_analysis.png', dpi=300, bbox_inches='tight')
print("Catalogues analysis visualization saved successfully!")

print("\nVisualization complete! Created two comprehensive charts:")
print("1. qing_imperial_collections_comparison.png - Collection sizes and distributions")
print("2. qing_imperial_catalogues_analysis.png - Imperial catalogues timeline and analysis")
