def classify_sign(landmarks):
    # Placeholder: just count finger spread or use a dummy rule
    if not landmarks: return "?"
    spread = landmarks[8]['x'] - landmarks[4]['x']
    if spread > 0.1:
        return "A"
    return "B"
