import math

def calculate_level(total_xp):
    """
    Calculate the player's level and progress towards the next level based on the total XP in Helldivers 2.

    Parameters:
    total_xp (int): The total accumulated XP.

    Returns:
    tuple: A tuple containing the player's current level (int), XP into the current level (int),
           and XP required for the next level (int).
    """
    # Constants based on the game's leveling system
    XP_INCREMENT = 500         # Increase in XP per level every 5 levels
    LEVELS_PER_BLOCK = 5       # Levels in each XP increment block
    BASE_XP = 500              # Starting XP per level

    # Solve the quadratic equation: m^2 + m - (total_xp / 1250) = 0
    a = 1
    b = 1
    c = -total_xp / (BASE_XP * LEVELS_PER_BLOCK / 2)
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        # No real solution; return level 0
        return 0, 0, BASE_XP

    sqrt_discriminant = math.sqrt(discriminant)
    m_positive = (-b + sqrt_discriminant) / (2 * a)
    m = m_positive  # We take the positive root since levels are positive

    # Calculate the integer part of m
    m_int = int(m)

    # Calculate total XP up to the last full block
    total_xp_up_to_m_int = (BASE_XP * LEVELS_PER_BLOCK / 2) * m_int * (m_int + 1)

    # Adjust m_int if the calculated total XP exceeds the actual total XP
    while total_xp_up_to_m_int > total_xp and m_int > 0:
        m_int -= 1
        total_xp_up_to_m_int = (BASE_XP * LEVELS_PER_BLOCK / 2) * m_int * (m_int + 1)

    # Remaining XP after full blocks
    remaining_xp = total_xp - total_xp_up_to_m_int

    # XP per level in the current block
    xp_per_level_current_block = BASE_XP + XP_INCREMENT * m_int

    # Levels gained in the current block
    levels_in_current_block = int(remaining_xp / xp_per_level_current_block)

    # XP used in the current block
    xp_used_in_current_block = levels_in_current_block * xp_per_level_current_block

    # XP into the next level
    xp_into_current_level = remaining_xp - xp_used_in_current_block

    # Total level is levels from full blocks plus levels in the current block
    total_level = LEVELS_PER_BLOCK * m_int + levels_in_current_block

    # XP needed to reach the next level
    xp_needed_for_next_level = xp_per_level_current_block

    return total_level, xp_into_current_level, xp_needed_for_next_level

def display_progress_bar(xp_into_current_level, xp_needed_for_next_level, bar_length=20):
    """
    Display a simple text-based progress bar in the terminal.

    Parameters:
    xp_into_current_level (int): The XP accumulated towards the current level.
    xp_needed_for_next_level (int): The total XP required to reach the next level from the current level.
    bar_length (int): The length of the progress bar in characters.
    """
    progress = xp_into_current_level / xp_needed_for_next_level
    filled_length = int(bar_length * progress)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    percentage = progress * 100
    print(f"Progress towards next level: |{bar}| {percentage:.1f}%")

# Example usage:
if __name__ == "__main__":
    total_xp_input = 1776793  # Replace this with your total XP
    level, xp_into_current_level, xp_needed_for_next_level = calculate_level(total_xp_input)
    print(f"With {total_xp_input} XP, you are at level {level}.")
    print(f"XP into current level: {xp_into_current_level}/{xp_needed_for_next_level} XP")
    display_progress_bar(xp_into_current_level, xp_needed_for_next_level)

