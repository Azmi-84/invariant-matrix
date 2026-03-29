import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def draw_gear_train_distinguishable(teeth_list):
    """
    Plots a 3-stage compound gear train sketch with high contrast colors and strategic alpha blending.
    teeth_list: list of 6 integers [T1, T2, T3, T4, T5, T6]
    """
    # Configuration
    module = 2.0  # Controls the physical size of the gears
    
    # 1. Distinctive, High-Contrast Colors for each gear box/stage
    # T1(In), T2(Back), T3(Front), T4(Back), T5(Front), T6(Out)
    colors = ['#FF0000', '#0000FF', '#00FF00', '#FF8C00', '#800080', '#00CED1'] # Red, Blue, Green, Orange, Purple, Cyan
    labels = ['T1 (In)', 'T2', 'T3', 'T4', 'T5', 'T6 (Out)']
    
    # 2. Strategic Opacity/Alpha-Blending for Overlaps:
    # We use low opacity for 'Back' gears and high for 'Front' gears.
    # T1: High, T2: Low, T3: High, T4: Low, T5: High, T6: High
    alphas = [0.8, 0.4, 0.8, 0.4, 0.8, 0.8] 

    # Calculate radii (Radius = (m * T) / 2)
    radii = [(module * t) / 2 for t in teeth_list]

    # Define Center Points (x, y)
    # Gear 1 (Input)
    c1 = (0, 0)
    # Gear 2 meshes with G1
    c2 = (radii[0] + radii[1], 0)
    # Gear 3 is on the SAME SHAFT as G2
    c3 = c2
    # Gear 4 meshes with G3
    c4 = (c2[0] + radii[2] + radii[3], 0)
    # Gear 5 is on the SAME SHAFT as G4
    c5 = c4
    # Gear 6 meshes with G5
    c6 = (c4[0] + radii[4] + radii[5], 0)

    centers = [c1, c2, c3, c4, c5, c6]

    # Create Plot
    fig, ax = plt.subplots(figsize=(8, 6))

    for i in range(6):
        # Draw the gear as a circle with specific transparency and edge
        circle = plt.Circle(centers[i], radii[i], 
                            color=colors[i], 
                            alpha=alphas[i], 
                            edgecolor='black',  # 3. Add edges for definition
                            linewidth=1.0,
                            label=f"{labels[i]}: {teeth_list[i]}T")
        ax.add_patch(circle)
        
        # Add center point marker
        ax.plot(centers[i][0], centers[i][1], 'ko', markersize=4)
        
        # Add Text Labels with distinctive color
        y_label_offset = radii[i] + 4
        # ax.text(centers[i][0], centers[i][1] + y_label_offset, 
        #         f"{labels[i]}\n{teeth_list[i]}T", 
        #         ha='center', va='bottom', fontsize=10, fontweight='bold', color=colors[i])

    # Draw Shaft Lines to indicate compound gears more strongly
    shaft_height = max(radii) * 1.5
    ax.plot([c2[0], c2[0]], [-shaft_height, shaft_height], 'k-', linewidth=3, alpha=0.5)
    ax.plot([c4[0], c4[0]], [-shaft_height, shaft_height], 'k-', linewidth=3, alpha=0.5)

    # Compound Gear Markers
    ax.text(c2[0], -shaft_height - 3, 'Common Shaft A', ha='center', fontweight='bold', alpha=0.7)
    ax.text(c4[0], -shaft_height - 3, 'Common Shaft B', ha='center', fontweight='bold', alpha=0.7)

    # Formatting the visual
    ax.set_aspect('equal')
    ax.set_xlim(-radii[0]-20, centers[-1][0] + radii[-1] + 20)
    ax.set_ylim(-max(radii)-20, max(radii)+20)
    plt.title(f"Gear Train Reduction Layout\nTarget Ratio: {round(1830/180, 2)}:1", fontsize=16)
    plt.axis('off')
    
    # Create a clearer legend using color patches
    legend_patches = [mpatches.Patch(color=colors[i], alpha=alphas[i], label=f"{labels[i]} ({teeth_list[i]}T)") for i in range(6)]
    plt.legend(handles=legend_patches, loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)
    
    plt.tight_layout()
    plt.show()

# Example gear set from your solver results
# [T1, T2, T3, T4, T5, T6]
best_fit_gears = [13, 15, 14, 42, 16, 47] 

draw_gear_train_distinguishable(best_fit_gears)