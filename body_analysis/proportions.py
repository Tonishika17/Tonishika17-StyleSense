def classify_leg_length(leg_length, height):
    """Classify leg length proportion using leg_ratio = leg_length / height."""
    if height <= 0:
        raise ValueError("Height must be positive")
    if leg_length < 0:
        raise ValueError("Leg length must be non-negative")

    leg_ratio = leg_length / height

    if leg_ratio >= 0.58:
        classification = "Long Legs"
    elif leg_ratio >= 0.46:
        classification = "Balanced Legs"
    else:
        classification = "Short Legs"

    return {
        "leg_ratio": leg_ratio,
        "classification": classification,
    }


def classify_shoulders(shoulder_width, height=None):
    """Classify shoulder width relative to height or absolute thresholds."""
    if shoulder_width < 0:
        raise ValueError("Shoulder width must be non-negative")

    if height is not None:
        if height <= 0:
            raise ValueError("Height must be positive when provided")
        ratio = shoulder_width / height
        if ratio >= 0.31:
            classification = "Broad Shoulders"
        elif ratio >= 0.24:
            classification = "Balanced Shoulders"
        else:
            classification = "Narrow Shoulders"
    else:
        if shoulder_width >= 50:
            classification = "Broad Shoulders"
        elif shoulder_width >= 44:
            classification = "Balanced Shoulders"
        else:
            classification = "Narrow Shoulders"

    return {
        "shoulder_width": shoulder_width,
        "height": height,
        "classification": classification,
    }


def classify_torso(leg_length, height):
    """Classify torso length using torso_length = height - leg_length."""
    if height <= 0:
        raise ValueError("Height must be positive")
    if leg_length < 0:
        raise ValueError("Leg length must be non-negative")
    if leg_length > height:
        raise ValueError("Leg length cannot exceed height")

    torso_length = height - leg_length
    torso_ratio = torso_length / height

    if torso_ratio >= 0.53:
        classification = "Long Torso"
    elif torso_ratio >= 0.46:
        classification = "Balanced Torso"
    else:
        classification = "Short Torso"

    return {
        "torso_length": torso_length,
        "torso_ratio": torso_ratio,
        "classification": classification,
    }


def classify_arm_length(arm_length, height):
    """Classify arm length using arm_length / height.

    Thresholds are derived from the dataset averages and quantiles:
    - median arm ratio ≈ 0.37
    - 75th percentile ≈ 0.42
    - 25th percentile ≈ 0.33
    """
    if height <= 0:
        raise ValueError("Height must be positive")
    if arm_length < 0:
        raise ValueError("Arm length must be non-negative")
    if arm_length > height:
        raise ValueError("Arm length cannot exceed height")

    arm_ratio = arm_length / height
    if arm_ratio >= 0.42:
        classification = "Long Arms"
    elif arm_ratio >= 0.33:
        classification = "Balanced Arms"
    else:
        classification = "Short Arms"

    return {
        "arm_length": arm_length,
        "arm_ratio": arm_ratio,
        "classification": classification,
    }


if __name__ == "__main__":
    sample = {
        "height": 170,
        "leg_length": 95,
        "shoulder_width": 44,
        "arm_length": 65,
    }
    print("Sample proportions output:")
    print(classify_leg_length(sample["leg_length"], sample["height"]))
    print(classify_shoulders(sample["shoulder_width"], sample["height"]))
    print(classify_torso(sample["leg_length"], sample["height"]))
    print(classify_arm_length(sample["arm_length"], sample["height"]))
