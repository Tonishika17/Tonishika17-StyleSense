from collections.abc import Mapping
from typing import Any, Dict, List, Union

PEAR_RULES: Dict[str, List[str]] = {
    "recommended": [
        "Boat Neck",
        "Off-Shoulder",
        "Bardot Neck",
        "Square Neck",
        "Cowl Neck",
        "Wide V-Neck",
        "Puff Sleeves",
        "Balloon Sleeves",
        "Cap Sleeves",
        "Bishop Sleeves",
        "Ruffle Sleeves",
        "Structured Shoulders",
        "Embroidery around shoulders",
        "Prints on top",
        "Bright colors on top",
        "Shoulder pads",
        "Horizontal detailing",
        "Straight-Leg Pants",
        "Wide-Leg Pants",
        "Bootcut Jeans",
        "Dark Wash Jeans",
        "A-line Skirts",
        "Structured Trousers",
        "A-line Dresses",
        "Fit-and-Flare Dresses",
        "Princess Dresses",
        "Off-Shoulder Dresses",
    ],
    "avoid": [
        "Very tight plain tops",
        "Narrow spaghetti straps",
        "Shoulder-less silhouettes",
        "Cargo pockets on hips",
        "Heavy embellishment on thighs",
        "Light-colored shiny bottoms",
        "Extremely skinny jeans",
        "Bodycon dresses emphasizing hips",
    ],
}

HOURGLASS_RULES: Dict[str, List[str]] = {
    "recommended": [
        "Sweetheart",
        "Scoop Neck",
        "V-Neck",
        "Wrap Neck",
        "Square Neck",
        "Fitted Sleeves",
        "Three-Quarter Sleeves",
        "Soft Puff Sleeves",
        "Wrap Tops",
        "Peplum Tops",
        "Fitted Shirts",
        "Waist-Cinching Blouses",
        "High-Waisted Jeans",
        "Pencil Skirts",
        "Tailored Trousers",
        "Flared Pants",
        "Wrap Dresses",
        "Mermaid Dresses",
        "Bodycon Dresses",
        "Fit-and-Flare Dresses",
    ],
    "avoid": [
        "Boxy silhouettes",
        "Oversized shapeless dresses",
        "Straight shift dresses",
        "Empire waists that hide waistline",
    ],
}

RECTANGLE_RULES: Dict[str, List[str]] = {
    "recommended": [
        "Sweetheart",
        "Scoop",
        "Deep V",
        "Off-Shoulder",
        "Puff Sleeves",
        "Flutter Sleeves",
        "Bell Sleeves",
        "Peplum Tops",
        "Ruffle Tops",
        "Wrap Tops",
        "Pleated Skirts",
        "Tulip Skirts",
        "Wide-Leg Pants",
        "Flared Jeans",
        "Fit-and-Flare",
        "Wrap Dresses",
        "Ruched Dresses",
        "Corset Dresses",
    ],
    "avoid": [
        "Boxy jackets",
        "Straight dresses",
        "Oversized tunics",
        "Drop-waist silhouettes",
    ],
}

INVERTED_TRIANGLE_RULES: Dict[str, List[str]] = {
    "recommended": [
        "V-Neck",
        "Scoop Neck",
        "Deep U Neck",
        "Simple fitted sleeves",
        "Raglan sleeves",
        "Dark tops",
        "Minimal shoulder detail",
        "Wide-Leg Pants",
        "Palazzo Pants",
        "Cargo Pants",
        "Pleated Skirts",
        "A-Line Skirts",
        "A-Line Dresses",
        "Skater Dresses",
        "Fit-and-Flare Dresses",
    ],
    "avoid": [
        "Puff Sleeves",
        "Boat Neck",
        "Shoulder Pads",
        "Off-Shoulder",
        "Skinny Jeans",
        "Narrow Pencil Skirts",
    ],
}

APPLE_RULES: Dict[str, List[str]] = {
    "recommended": [
        "V-Neck",
        "Deep Scoop",
        "Surplice Neck",
        "Wrap Neck",
        "Three-Quarter Sleeves",
        "Bell Sleeves",
        "Dolman Sleeves",
        "Straight-Leg Pants",
        "Bootcut Jeans",
        "Flared Trousers",
        "Empire Waist Dresses",
        "Wrap Dresses",
        "Shift Dresses",
        "A-Line Dresses",
    ],
    "avoid": [
        "Crop Tops ending at widest point",
        "Tight waist belts",
        "High-neck bulky tops",
        "Clingy fabrics around stomach",
    ],
}

UNKNOWN_BODY_TYPE_RULES: Dict[str, List[str]] = {"recommended": [], "avoid": []}

_BODY_TYPE_RULES: Dict[str, Dict[str, List[str]]] = {
    "pear": PEAR_RULES,
    "hourglass": HOURGLASS_RULES,
    "rectangle": RECTANGLE_RULES,
    "inverted triangle": INVERTED_TRIANGLE_RULES,
    "apple": APPLE_RULES,
}

_BODY_TYPE_ALIASES: Dict[str, str] = {
    "pear": "pear",
    "hourglass": "hourglass",
    "rectangle": "rectangle",
    "inverted triangle": "inverted triangle",
    "inverted": "inverted triangle",
    "inverted_triangle": "inverted triangle",
    "invertedtriangle": "inverted triangle",
    "triangle": "inverted triangle",
    "apple": "apple",
}


def _normalize_body_type(body_type: Any) -> str:
    if not isinstance(body_type, str):
        raise TypeError("body_type must be a string")

    normalized = body_type.strip().lower().replace("_", " ").replace("-", " ")
    return _BODY_TYPE_ALIASES.get(normalized, normalized)


def get_recommendations(
    body_profile: Union[Mapping[str, Any], str]
) -> Dict[str, List[str]]:
    """Return styling recommendations based on a body type profile.

    Args:
        body_profile: A dict with at least a "body_type" key or a string
            containing the body type name.

    Returns:
        A dict with "recommended" and "avoid" lists.
    """
    if isinstance(body_profile, str):
        body_type = body_profile
    elif isinstance(body_profile, Mapping):
        if "body_type" not in body_profile:
            raise ValueError("body_profile must include a 'body_type' entry")
        body_type = body_profile["body_type"]
    else:
        raise TypeError("body_profile must be a mapping or a string")

    normalized_body_type = _normalize_body_type(body_type)
    rules = _BODY_TYPE_RULES.get(normalized_body_type, UNKNOWN_BODY_TYPE_RULES)

    return {
        "recommended": list(rules["recommended"]),
        "avoid": list(rules["avoid"]),
    }
