This Python script will calculate your Helldivers 2 level after you hit the cap.

## How to Use This Script

1. **Download the Python Script**  
   First, download the Python script from the GitHub repository if you haven't done so already.

2. **Launch Helldivers 2**  
   Open the game and go to the armory on your ship.

3. **Navigate to the Career Tab**  
   In the **CAREER** tab, scroll down until you find the **XP Earned** metric. Copy or record this value.

4. **Update the Script with Your XP**  
   Open the script in a text editor, and locate `total_xp_input` on **Line 84**. Replace the placeholder value (`1776793`) with your current XP.

## How is this Calculated?

The XP requirements increase by 500 every five levels. 

### Example Progression
Assuming a consistent increase from the very first level:

| Level Range | XP per Level | Total XP for Range |
|-------------|--------------|--------------------|
| 0 - 5       | 500 XP       | 2,500 XP          |
| 5 - 10      | 1,000 XP     | 7,500 XP          |
| ...         | ...          | ...               |
| 145 - 150   | 15,500 XP    | 1,162,500 XP      |

### Formula
To calculate the total XP needed for any five-level interval, we can use the following formula:

**Sum** = 5 * (500 * n), where _n_ = 1, 2, …, _m_

where **m** = level / 5.
