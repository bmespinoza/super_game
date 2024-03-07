from requests import HTTPError, post
import os
from dotenv import load_dotenv

load_dotenv()

api_url = os.getenv("MAIL_API_URL")
api_key = os.getenv("MAIL_API_KEY")
mail_from = os.getenv("MAIL_FROM")


def create_html_email(html_body: str) -> str:
    html = f"""
        <html>
            <body>
                {html_body}
            </body>
        </html>
        """
    return html


def send_simple_message(recipient_email: str, html: str) -> None:
    try:
        response = post(
            f"{api_url}/messages",
            auth=("api", api_key),
            data={
                "from": mail_from,
                "to": recipient_email,
                "subject": "Fighting game",
                "html": html,
            },
        )
        response.raise_for_status()
        print("Mail enviado, podría tardar unos segundos")
    except HTTPError as error:
        print("Error enviando email", error)
