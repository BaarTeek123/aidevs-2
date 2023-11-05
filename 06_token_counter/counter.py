import logging
import tiktoken
import Message


TOKEN_VALUES = {
    "gpt-3.5-turbo-0613": (3, 1),
    "gpt-3.5-turbo-16k-0613": (3, 1),
    "gpt-4-0314": (3, 1),
    "gpt-4-32k-0314": (3, 1),
    "gpt-4-0613": (3, 1),
    "gpt-4-32k-0613": (3, 1),
    "gpt-3.5-turbo-0301": (4, -1),
}



# Default encoding for the base case
BASE_ENCODING = tiktoken.get_encoding("cl100k_base")


def count_tokens(messages, model="gpt-3.5-turbo-0613"):
    """Return the number of tokens used by a list of messages."""
    # Retrieve encoding based on model or use base encoding
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        logging.warning("Model not found. Using cl100k_base encoding.")
        encoding = BASE_ENCODING

    # Determine tokens per message/name based on model
    tokens_per_message, tokens_per_name = TOKEN_VALUES.get(
        model,
        (3, 1) if "gpt-3.5-turbo" in model or "gpt-4" in model else (None, None)
    )

    if tokens_per_message is None:
        raise NotImplementedError(
            f"num_tokens_from_messages() is not implemented for model {model}. "
            "See the documentation for information on how messages are converted to tokens."
        )

    if "gpt-3.5-turbo" in model or "gpt-4" in model:
        logging.warning(
            f"{model} may update over time. Assuming default tokens for the latest known configuration."
        )

    # Calculate the total number of tokens
    num_tokens = 3  # Add base tokens for the messages list itself
    for message in messages:
        if not isinstance(message, Message):
            raise ValueError("All items in messages must be instances of Message class.")

        num_tokens += tokens_per_message + len(encoding.encode(message.get_all_text()))
        if message.name:
            num_tokens += tokens_per_name

    return num_tokens


# Example usage within the package
# messages = [Message("user", "Hello, how are you?", "Alice"), Message("bot", "I'm fine, thank you!")]
# total_tokens = num_tokens_from_messages(messages)
# print(total_tokens)