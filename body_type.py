def determine_body_type(shoulder, bust, waist, hip):
    """
    Determine body type based on body measurements using classification rules.
    
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
    S = shoulder
    
    # HOURGLASS: Bust ≈ Hip with significantly smaller waist
    # Rule: abs(bust - hip) <= 0.05 * max(bust, hip) AND waist <= 0.75 * min(bust, hip)
    if abs(B - H) <= 0.05 * max(B, H) and W <= 0.75 * min(B, H):
        return "Hourglass"
    
    # PEAR: Hip noticeably larger than Bust
    # Rule: hip >= bust * 1.05 AND waist < hip * 0.85
    if H >= B * 1.05 and W < H * 0.85:
        return "Pear"
    
    # INVERTED TRIANGLE: Shoulders/Bust wider than Hip
    # Rule: (shoulder > hip * 1.05) OR (bust > hip * 1.05)
    if S > H * 1.05 or B > H * 1.05:
        return "Inverted Triangle"
    
    # APPLE: Waist dominant
    # Rule: waist >= bust * 0.90 OR waist >= hip * 0.90
    if W >= B * 0.90 or W >= H * 0.90:
        return "Apple"
    
    # RECTANGLE: Bust ≈ Waist ≈ Hip
    # Rule: abs(bust-hip) <= 0.05*max(bust,hip) AND waist > 0.75*min(bust,hip)
    if abs(B - H) <= 0.05 * max(B, H) and W > 0.75 * min(B, H):
        return "Rectangle"
    
    return "Unknown"