def determine_body_type(shoulder, bust, waist, hip):
    """
    Determine body type based on body measurements using optimized classification rules.
    
    All measurements should be in the same unit (inches or cm).
    
    Args:
        shoulder: Shoulder width measurement
        bust: Bust/chest measurement
        waist: Waist measurement
        hip: Hip measurement
    
    Returns:
        str: Body type classification - Hourglass, Pear, Inverted Triangle, 
             Rectangle, Apple, or Unknown
    """
    B = bust
    H = hip
    W = waist
    
    # Pre-calculate key measurement differences for efficiency
    bust_hip_diff = B - H          # (B-H)
    hip_bust_diff = H - B          # (H-B)
    bust_waist_diff = B - W        # (B-W)
    hip_waist_diff = H - W         # (H-W)
    
    # Hourglass: (B-H) ≤ 1 AND (H-B) < 3.6 AND ((B-W) ≥ 9 OR (H-W) ≥ 10)
    # Balanced bust and hips with pronounced waist definition
    if bust_hip_diff <= 1 and hip_bust_diff < 3.6 and (bust_waist_diff >= 9 or hip_waist_diff >= 10):
        return "Hourglass"
    
    # Pear: (H-B) ≥ 3.6 AND (H-W) < 9
    # Hips significantly larger than bust, waist only slightly smaller than hips
    if hip_bust_diff >= 3.6 and hip_waist_diff < 9:
        return "Pear"
    
    # Inverted Triangle: (B-H) ≥ 3.6 AND (B-W) < 9
    # Bust significantly larger than hips, waist only slightly smaller than bust
    if bust_hip_diff >= 3.6 and bust_waist_diff < 9:
        return "Inverted Triangle"
    
    # Rectangle: (H-B) < 3.6 AND (B-H) < 3.6 AND (B-W) < 9 AND (H-W) < 10
    # Bust and hips nearly equal with minimal waist definition
    if abs(bust_hip_diff) < 3.6 and bust_waist_diff < 9 and hip_waist_diff < 10:
        return "Rectangle"
    
    # Apple: 0.80 ≤ (W/H) ≤ 0.85
    # Waist to hip ratio within the defined range
    if H > 0:  # Prevent division by zero
        waist_hip_ratio = W / H
        if 0.80 <= waist_hip_ratio <= 0.85:
            return "Apple"
    
    return "Unknown"