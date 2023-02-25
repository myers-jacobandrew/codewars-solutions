def format_duration(seconds):
    years = seconds // (365 * 24 * 60 * 60)
    days = (seconds // (24 * 60 * 60)) % 365
    hours = (seconds // (60 * 60)) % 24
    minutes = (seconds // 60) % 60
    seconds = seconds % 60
    components = []

    if (seconds + minutes + hours + days + years) == 0:
        return 'now'

    if years > 0:
        components.append(f"{years} year" + ("s" if years > 1 else ""))

    if days > 0:
        components.append(f"{days} day" + ("s" if days > 1 else ""))

    if hours > 0:
        components.append(f"{hours} hour" + ("s" if hours > 1 else ""))

    if minutes > 0:
        components.append(f"{minutes} minute" + ("s" if minutes > 1 else ""))

    if seconds > 0:
        components.append(f"{seconds} second" + ("s" if seconds > 1 else ""))

    output = ""
    last_index = len(components) - 1
    for i, component in enumerate(components):
        output += component
        if i < last_index - 1:
            output += ", "
        elif i == last_index - 1:
            output += " and "

    return output
