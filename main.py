from __future__ import annotations

import sys
from typing import Any, Dict, List, Optional

from body_analysis.body_type import determine_body_type
from body_analysis.proportions import (
    classify_leg_length,
    classify_shoulders,
    classify_torso,
)
from recommendations import get_recommendations


def prompt_float(prompt: str, *, default: Optional[float] = None) -> float:
    while True:
        try:
            raw_value = input(prompt).strip()
        except EOFError:
            if default is not None:
                print("No input detected. Using the default value.")
                return default
            print("No input detected. Using 0.0.")
            return 0.0

        if not raw_value and default is not None:
            return default

        try:
            value = float(raw_value)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if value < 0:
            print("Please enter a non-negative value.")
            continue
        return value


def collect_user_profile() -> Dict[str, Any]:
    print("\nWelcome to the AI Fashion Stylist")
    print("Please enter your measurements in the same unit (cm or inches).\n")

    profile = {
        "height": prompt_float("Height: ", default=165.0),
        "shoulder_width": prompt_float("Shoulder width: ", default=40.0),
        "bust": prompt_float("Bust/chest: ", default=90.0),
        "waist": prompt_float("Waist: ", default=70.0),
        "hip": prompt_float("Hip: ", default=95.0),
        "leg_length": prompt_float("Leg length: ", default=85.0),
    }
    return profile


def build_report(
    profile: Dict[str, Any],
    body_type: str,
    leg_analysis: Dict[str, Any],
    torso_analysis: Dict[str, Any],
    shoulder_analysis: Dict[str, Any],
    recommendations: Dict[str, List[str]],
) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("AI FASHION STYLIST REPORT")
    lines.append("=" * 60)
    lines.append(f"Height: {profile['height']:.1f}")
    lines.append(f"Shoulder Width: {profile['shoulder_width']:.1f}")
    lines.append(f"Bust: {profile['bust']:.1f}")
    lines.append(f"Waist: {profile['waist']:.1f}")
    lines.append(f"Hip: {profile['hip']:.1f}")
    lines.append(f"Leg Length: {profile['leg_length']:.1f}")
    lines.append("")
    lines.append("Body Type")
    lines.append("-" * 60)
    lines.append(f"Detected Body Type: {body_type}")
    lines.append("")
    lines.append("Proportions")
    lines.append("-" * 60)
    lines.append(f"Legs: {leg_analysis['classification']} (ratio {leg_analysis['leg_ratio']:.2f})")
    lines.append(f"Torso: {torso_analysis['classification']} (ratio {torso_analysis['torso_ratio']:.2f})")
    lines.append(f"Shoulders: {shoulder_analysis['classification']}")
    lines.append("")
    lines.append("Style Recommendations")
    lines.append("-" * 60)
    if recommendations["recommended"]:
        lines.append("Recommended:")
        for item in recommendations["recommended"]:
            lines.append(f"- {item}")
    else:
        lines.append("Recommended: None")

    if recommendations["avoid"]:
        lines.append("")
        lines.append("Avoid:")
        for item in recommendations["avoid"]:
            lines.append(f"- {item}")
    else:
        lines.append("Avoid: None")

    lines.append("")
    lines.append("=" * 60)
    return "\n".join(lines)


def main() -> None:
    profile = collect_user_profile()

    body_type = determine_body_type(
        shoulder=profile["shoulder_width"],
        bust=profile["bust"],
        waist=profile["waist"],
        hip=profile["hip"],
    )

    leg_analysis = classify_leg_length(profile["leg_length"], profile["height"])
    torso_analysis = classify_torso(profile["leg_length"], profile["height"])
    shoulder_analysis = classify_shoulders(profile["shoulder_width"], profile["height"])
    recommendations = get_recommendations({"body_type": body_type})

    report = build_report(
        profile=profile,
        body_type=body_type,
        leg_analysis=leg_analysis,
        torso_analysis=torso_analysis,
        shoulder_analysis=shoulder_analysis,
        recommendations=recommendations,
    )

    print(report)


if __name__ == "__main__":
    main()
