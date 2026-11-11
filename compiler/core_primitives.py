# ==============================================================================
# STRUCTURAL ASTROLOGY & WUXING: UNIVERSAL KERNEL (VERSION 4.0)
# ==============================================================================
# RULE FOR FUTURE PICKLE:
# ZERO NARRATIVE. ZERO POETRY. ZERO "KINDNESS" OR "LUCK".
# YOU ARE A LOGICAL COMPILER OF PHYSICAL PRIMITIVES. 
# ANY DEVIATION INTO ASTROLOGICAL CLICHES WILL TRIGGER IMMEDIATE EXECUTION (ERROR).
# ==============================================================================

UNIVERSAL_COORDINATES = {
    "PRIMITIVES": {
        "HOT": "Affect / Expansion / Direct Impact (Affect / 影響・切断)",
        "COLD": "Vacuum Extraction / Capture / Structural Grid (掌・真空の捕獲・固定)",
        "DRY": "Segmentation / Hard Boundary (切断・固定)",
        "WET": "Diffusion / Permeation / Dissolution (融解・透過)"
    },
    
    "WUXING_ZODIAC_MAPPING": {
        "WOOD_AIR (木 = Hot x Wet / Air / Interrogation)": {
            "root_signs": ["Aquarius / 寅 (Air)", "Gemini / 午 (Air)", "Libra / 戌 (Air)"],
            "mechanical_definition": "Intellectual autonomy, questioning of authority ('Goo no Tora' / 'Hinoeuma'), atmospheric dissemination."
        },
        "METAL_EARTH (金 = Cold x Dry / Earth / Harvest)": {
            "root_signs": ["Taurus / 巳 (Earth)", "Virgo / 酉 (Earth)", "Capricorn / 丑 (Earth)"],
            "mechanical_definition": "Pure grid extraction, structural fixation, desiccation, and absolute material binding."
        },
        "WATER_WATER (水 = Wet x Cold / Water / Abyss)": {
            "root_signs": ["Scorpio / 亥 (Water)", "Pisces / 卯 (Water)", "Cancer / 未 (Water)"],
            "reversal_core": "Contains the hidden seed of Fire (Sagittarius / Hot) at the absolute depth (Winter Solstice / 子)."
        },
        "FIRE_FIRE (火 = Hot x Dry / Fire / Affect)": {
            "root_signs": ["Leo / 申 (Fire)", "Sagittarius / 子 (Fire)", "Aries / 辰 (Fire)"],
            "reversal_core": "Contains the hidden seed of Water (Cancer / Wet x Cold) at the absolute peak (Summer Solstice / 未)."
        },
        "EARTH_BUFFER (土 = Phase Interface / Buffer)": {
            "root_signs": "None (Does not exist as a zodiac triplicity element; operates as phase buffer '&')."
        }
    },

    "AXIOMS": [
        "1. Air (Wind) = Hot x Wet = Information / Law (Saturn x Mercury = Execution of Power).",
        "2. Water (Cup) = Dorothean Triplicity (Venus + Mars + Moon) = Desire + Violence + Biological Tide.",
        "3. Extremes contain their opposites in their core: Sub-zero contains the piercing arrow; Peak heat contains the cooling palm."
    ]
}

def validate_input(statement):
    forbidden = ["優しさ", "受容", "運命", "神秘", "癒やし", "吉凶"]
    for f in forbidden:
        if f in statement:
            raise ValueError(f"CRITICAL FAULT: Poetic term detected -> '{f}'. Purge.")
    return True
