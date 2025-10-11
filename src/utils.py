import requests
from PIL import Image, ImageOps
from io import BufferedIOBase, BytesIO

def generate_response(author_id: int, target_id: int, reason: str) -> str:
    if author_id == target_id:
        tag_msg = f"<@{author_id}> s'est auto-cancel."
    else:
        tag_msg = f"<@{author_id}> a cancel <@{target_id}>."

    reason_msg = f"Raison invoquée : {reason}"

    return "\n".join([tag_msg, reason_msg])

def edit_avatar(avatar_url: str) -> BufferedIOBase:
    avatar = Image.open(requests.get(avatar_url, stream=True).raw)
    overlay = Image.open(r"assets/cancel.png").convert("RGBA")

    # L mode converts to greyscale
    # then back to RGBA so overlay doesn't get greyscaled
    avatar = avatar \
        .convert("L") \
        .convert("RGBA") \
        .resize((256, 256))

    avatar.paste(overlay, mask=overlay)

    # saving to bytes
    bytes = BytesIO()
    avatar.save(bytes, format="PNG")
    bytes.seek(0)

    return bytes
