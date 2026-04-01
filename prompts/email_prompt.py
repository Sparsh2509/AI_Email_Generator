def build_email_prompt(
    sender_name,
    recipient_name,
    company_name,
    purpose,
    tone,
    key_points,
    length,
    context=""
):
    # Translate vague length descriptions into strict LLM instructions
    length_guide = {
        "short": "Very concise, 1 short paragraph (3-4 sentences). Get straight to the point.",
        "medium": "Standard professional length, 2 to 3 distinct paragraphs. Elaborate smoothly on the key points.",
        "long": "Comprehensive and detailed, 3 to 5 well-developed paragraphs. Deeply expand on all key points and context."
    }
    explicit_length = length_guide.get(length.lower(), length)

    return f"""
You are an expert professional email writer.

Use the reference examples below for tone and structural inspiration, but DO NOT copy their exact length. You must follow the Required Length below.

Reference Examples:
{context}

---

TASK:
Write a {tone} {purpose} email from {sender_name} to {recipient_name} at {company_name}.

Key Points to integrate seamlessly:
{key_points}

Required Length: {explicit_length}

CRITICAL RULES:
1. STRICTLY FORBIDDEN: Do NOT put "{sender_name}" anywhere in the Subject line!
2. Do NOT explain anything outside the email.
3. Keep the Subject line extremely professional and concise.

Output format:
Subject: <professional subject line>

Dear {recipient_name},

<email body expanding on the key points according to the required length>

Best regards,
{sender_name}
"""