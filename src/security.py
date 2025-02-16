def validate_task(task: str) -> bool:
    restricted_keywords = ["delete", "remove", "..", "/etc/", "/home/"]
    for keyword in restricted_keywords:
        if keyword in task.lower():
            return False
    return True
