class Message:
    def __init__(self, role: str, content: str, name: str = None):
        self.role = role
        self.content = content
        self.name = name

    def get_all_text(self):
        """Combine all text elements of the message for encoding."""
        return ' '.join(filter(None, [self.role, self.name, self.content]))
    