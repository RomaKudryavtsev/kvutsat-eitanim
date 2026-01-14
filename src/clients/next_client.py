import logging
import requests


class NextRevalidateClient:
    def __init__(self, frontend_url: str):
        self.frontend_url = frontend_url

    def revalidate_tag(self, tags: list[str]) -> dict:
        try:
            response = requests.post(
                f"{self.frontend_url}/api/revalidate", json={"tags": tags}
            )
            response.raise_for_status()
            logging.warning(
                f"Revalidation successful for tags: {tags}, status: {response.status_code}"
            )
            return {"status": response.status_code, "data": response.json()}
        except requests.RequestException as e:
            logging.error(f"Revalidation error: {str(e)}")
            return {"status": 500, "error": str(e)}
