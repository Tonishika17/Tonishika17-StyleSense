BODY_TYPE_CHARACTERISTICS = {
    "pear": {
        "body_type": "Pear",
        "characteristics": [
            "Hips wider than shoulders",
            "Defined waist",
            "Smaller bust",
            "Weight gain usually in hips, thighs, lower body",
        ],
        "styling_goal": "Create visual width on the upper body and draw attention upward.",
    },
    "hourglass": {
        "body_type": "Hourglass",
                if abs(B - H) <= 0.05 * max(B, H) and W <= 0.75 * min(B, H):
                    body_type = "Hourglass"
            "Defined waist",
            "Balanced proportions",
        ],
                elif H >= B * 1.05 and W < H * 0.85:
                    body_type = "Pear"
    "rectangle": {
        "body_type": "Rectangle",
        "characteristics": [
                elif S > H * 1.05 or B > H * 1.05:
                    body_type = "Inverted Triangle"
            "Athletic frame",
        ],
        "styling_goal": "Create the illusion of curves.",
                elif W >= B * 0.90 or W >= H * 0.90:
                    body_type = "Apple"
        "body_type": "Inverted Triangle",
        "characteristics": [
            "Shoulders wider than hips",
                elif abs(B - H) <= 0.05 * max(B, H) and W > 0.75 * min(B, H):
                    body_type = "Rectangle"
        ],
                else:
                    body_type = "Unknown"

                if verbose:
                    print_body_type_characteristics(body_type)

                return body_type
    },
    "apple": {
        "body_type": "Apple",
        "characteristics": [
            "Fuller midsection",
            "Less defined waist",
            "Slim legs often present",
            "Weight around stomach",
        ],
        "styling_goal": "Create vertical lines and define shape without emphasizing the waist area.",
    },
}


def _normalize_body_type(body_type):
    if not isinstance(body_type, str):
        raise TypeError("body_type must be a string")

    return body_type.strip().lower().replace("_", " ").replace("-", " ")


def get_body_type_characteristics(body_type):
    """Return characteristics and styling goal for a body type."""
    normalized = _normalize_body_type(body_type)
    return BODY_TYPE_CHARACTERISTICS.get(
        normalized,
        {
            "body_type": body_type,
            "characteristics": [],
            "styling_goal": "No styling guidance available for this body type.",
        },
    )


def print_body_type_characteristics(body_type):
    """Print characteristics and styling goal for the given body type."""
    info = get_body_type_characteristics(body_type)
    print(f"Body type: {info['body_type']}")
    print("\nCharacteristics")
    for characteristic in info["characteristics"]:
        print(f"- {characteristic}")
    print("\nStyling Goal")
    print(info["styling_goal"])


def determine_body_type(shoulder, bust, waist, hip, verbose=False):
    """
    Determine body type based on body measurements using classification rules.
    
    All measurements should be in the same unit (inches or cm).
    
    Args:
        shoulder: Shoulder width measurement
        bust: Bust/chest measurement
        waist: Waist measurement
        hip: Hip measurement
        verbose: If True, print body type characteristics with the result.
    
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
        body_type = "Hourglass"
    
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