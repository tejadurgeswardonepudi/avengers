def marketing_prompt(product, audience, platform):
    return f"""
    Create a marketing campaign for:
    Product: {product}
    Target Audience: {audience}
    Platform: {platform}

    Include:
    - Campaign objective
    - 5 content ideas
    - 3 ad copy variations
    - CTA suggestions
    """


def sales_pitch_prompt(product, customer):
    return f"""
    Create a sales pitch for:
    Product: {product}
    Customer: {customer}

    Include:
    - 30-second elevator pitch
    - Clear value proposition
    - Key differentiators
    - Call-to-action
    """


def lead_scoring_prompt(budget, urgency, requirement):
    return f"""
    Analyze this sales lead and assign a score (0–100):

    Budget: {budget}
    Urgency: {urgency}
    Requirement: {requirement}

    Provide:
    - Lead score
    - Reasoning
    - Probability of conversion
    """