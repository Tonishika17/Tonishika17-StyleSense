def determine_body_type(
    shoulder,
    bust,
    waist,
    hip
):
    # The classification rules currently rely on bust, waist, and hip only.
    B = bust
    H = hip
    W = waist
    bust_hip = B - H
    hip_bust = H - B
    bust_waist = B - W
    hip_waist = H - W

    # Hourglass
    # Condition 1: (B-H) <= 1" AND (H-B) < 3.6"
    # Condition 2: (B-W) >= 9" OR (H-W) >= 10"
    if bust_hip <= 1 and hip_bust < 3.6 and (bust_waist >= 9 or hip_waist >= 10):
        return "Hourglass"

    # Pear
    if hip_bust >= 3.6 and hip_waist < 9:
        return "Pear"

    # Inverted Triangle
    if bust_hip >= 3.6 and bust_waist < 9:
        return "Inverted Triangle"

    # Apple
    if H > 0:
        waist_hip_ratio = W / H
        if 0.80 <= waist_hip_ratio <= 0.85:
            return "Apple"

    # Rectangle
    if abs(bust_hip) < 3.6 and bust_waist < 9 and hip_waist < 10:
        return "Rectangle"

    return "Unknown"