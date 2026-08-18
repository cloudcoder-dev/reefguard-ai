def get_recommendation(predicted_class, confidence):
    """
    Generate a simple conservation recommendation
    based on the coral health classification.
    """

    if predicted_class == "Bleached":
        recommendation = (
            "Possible coral bleaching detected. "
            "The image should be monitored and, where possible, "
            "reviewed by a marine or environmental expert. "
            "Avoid treating this result as a diagnosis."
        )

    elif predicted_class == "Healthy":
        recommendation = (
            "The coral appears healthy according to the AI model. "
            "Continued monitoring is recommended because coral health "
            "can change with environmental conditions."
        )

    else:
        recommendation = (
            "The AI model produced an unexpected classification. "
            "Please review the image and consult an environmental expert."
        )

    return recommendation
# Test the recommendation system
print(get_recommendation("Bleached", 92.4))
print()
print(get_recommendation("Healthy", 88.1))