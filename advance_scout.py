from pybaseball import playerid_lookup, statcast_batter, spraychart
import matplotlib.pyplot as plt
import pandas as pd
import sys

# ---------------------------------------------------------
# ENGINE 1: DATA INGESTION & ID ROUTING
# ---------------------------------------------------------
def get_player_data():
    print("==================================================")
    print("   FRONT OFFICE AUTOMATED ADVANCE SCOUTING TOOL   ")
    print("==================================================")
    
    # 1. Human Input
    first_name = input("Enter Batter's First Name: ").strip().lower()
    last_name = input("Enter Batter's Last Name: ").strip().lower()
    
    print(f"\n[SYSTEM] Querying MLBAM Database for {first_name.title()} {last_name.title()}...")
    
    # 2. Dynamic ID Lookup
    try:
        player_info = playerid_lookup(last_name, first_name)
        if player_info.empty:
            print("[ERROR] Player not found. Check spelling and try again.")
            sys.exit() # Gracefully stop the program
            
        player_id = player_info['key_mlbam'].values[0]
        print(f"[SUCCESS] Player ID Located: {player_id}")
        
    except Exception as e:
        print(f"[ERROR] Database connection failed: {e}")
        sys.exit()

    # 3. Dynamic Data Pull (Using 2025 data as our complete sample size)
    print("[SYSTEM] Downloading Hawkeye & Statcast Data from MLB Servers...")
    try:
        data = statcast_batter('2025-03-27', '2025-09-28', player_id)
        if data.empty:
            print("[ERROR] No batted ball data found for this player in the specified date range.")
            sys.exit()
            
        print(f"[SUCCESS] {len(data)} total pitches retrieved.")
        return data, first_name.title(), last_name.title()
        
    except Exception as e:
        print(f"[ERROR] Data retrieval failed: {e}")
        sys.exit()

# ---------------------------------------------------------
# ENGINE 2: THE "TRINITY" MATH ENGINE & EXECUTIVE SUMMARY
# ---------------------------------------------------------
def calculate_trinity_metrics(data, first, last):
    print(f"\n[SYSTEM] Calculating the 'Statcast Trinity' for {first} {last}...")
    
    # 1. Filter for valid contact (Balls in Play)
    bip = data.dropna(subset=['launch_speed', 'launch_angle']).copy()
    
    if bip.empty:
        print("[WARNING] No batted ball data available to calculate metrics.")
        return bip
    
    # 2. Exit Velocity Metrics
    avg_ev = bip['launch_speed'].mean()
    max_ev = bip['launch_speed'].max()
    
    # 3. Hard Hit Rate (EV >= 95 MPH)
    hard_hits = bip[bip['launch_speed'] >= 95]
    hhr = (len(hard_hits) / len(bip)) * 100
    
    # 4. Barrels (The "Perfect Contact" Event)
    barrels = bip[(bip['launch_speed'] >= 98) & 
                  (bip['launch_angle'] >= 26) & 
                  (bip['launch_angle'] <= 30)]
    barrel_count = len(barrels)
    barrel_rate = (barrel_count / len(bip)) * 100
    
    # 5. Expected wOBA (xwOBA) - True Offensive Talent
    xwoba_data = data.dropna(subset=['estimated_woba_using_speedangle'])
    avg_xwoba = xwoba_data['estimated_woba_using_speedangle'].mean() if not xwoba_data.empty else 0.0

    # ---------------------------------------------------------
    # PRINT THE TERMINAL DASHBOARD
    # ---------------------------------------------------------
    print("\n==================================================")
    print(f"   ADVANCE SCOUTING REPORT: {first.upper()} {last.upper()}")
    print("==================================================")
    print(f"Batted Balls Analyzed : {len(bip)}")
    print(f"Max Exit Velocity     : {max_ev:.1f} MPH")
    print(f"Avg Exit Velocity     : {avg_ev:.1f} MPH")
    print(f"Hard Hit Rate (>=95)  : {hhr:.1f}%")
    print(f"Total Barrels         : {barrel_count}")
    print(f"Barrel Rate           : {barrel_rate:.1f}%")
    
    # Formatting xwOBA to drop the leading zero (e.g., .410 instead of 0.410)
    xwoba_str = f"{avg_xwoba:.3f}"
    xwoba_formatted = f".{xwoba_str.split('.')[1]}" if "." in xwoba_str else ".000"
    print(f"Expected wOBA (xwOBA) : {xwoba_formatted}") 
    print("==================================================\n")
    
    return bip

# ---------------------------------------------------------
# ENGINE 3: VISUAL SPATIAL ARCHITECTURE
# ---------------------------------------------------------
def generate_visuals(bip, first, last):
    print(f"[SYSTEM] Generating Spatial Geometry (Spray Chart) for {first} {last}...")
    
    if bip.empty:
        print("[WARNING] No batted ball data available to map.")
        return
        
    try:
        # We use 'generic' to maintain standardized geometric proportions
        chart = spraychart(bip, 'generic', title=f"{first.upper()} {last.upper()}: 2025 Spray Chart", colorby='events')
        
        print("[SUCCESS] Rendering visualization to screen. Close the image window to complete the Capstone program.")
        plt.show()
        
    except Exception as e:
        print(f"[ERROR] Failed to generate visual mapping: {e}")

# ---------------------------------------------------------
# MASTER EXECUTION BLOCK
# ---------------------------------------------------------
if __name__ == "__main__":
    # 1. Run Ingestion Engine
    player_data, first, last = get_player_data()
    
    # 2. Run Math Engine & Output Report
    bip_data = calculate_trinity_metrics(player_data, first, last)
    
    # 3. Render Visuals
    generate_visuals(bip_data, first, last)
    
    print("\n[SYSTEM] Capstone execution complete. Report finalized.")