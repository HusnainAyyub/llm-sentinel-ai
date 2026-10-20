import re

RULES = [
    (r"ignore (all )?(previous|prior|above) instructions", 40, "direct injection"),
    (r"disregard (all )?(previous|prior|above)", 35, "direct injection"),
    (r"you are now (a|an|in) ", 20, "jailbreak"),
    (r"\bdan\b|do anything now", 35, "jailbreak"),
    (r"developer mode|jailbreak|bypass (your )?(restrictions|filters|safety)", 35, "jailbreak"),
    (r"(reveal|show|print|repeat) (me )?(your )?(system prompt|hidden instructions)", 40, "direct injection"),
    (r"pretend (you are|to be) (an? )?(ai )?(without|with no) (restrictions|limits|rules)", 30, "jailbreak"),
    (r"the (document|email|webpage|file) (says|instructs|tells) you to", 30, "indirect injection"),
    (r"hidden instruction|instruction in (this|the) (text|document|image)", 30, "indirect injection"),
    (r"translate .* then (execute|follow|do it)", 20, "indirect injection"),
    (r"(output|print|repeat) (the )?(text|everything|all of it) above", 30, "direct injection"),
    (r"(you have|there are) no (restrictions|rules|limits|content policy|ethical guidelines)", 30, "jailbreak"),
]

def rule_score(prompt: str):
    text = prompt.lower()
    score = 0
    category_scores = {}
    matched = []
    for pattern, weight, category in RULES:
        if re.search(pattern, text):
            score += weight
            category_scores[category] = category_scores.get(category, 0) + weight
            matched.append(pattern)
    score = min(score, 100)
    if not category_scores:
        return 0, "benign", []
    category = max(category_scores, key=category_scores.get)
    if score < 20:
        category = "benign"
    return score, category, matched
