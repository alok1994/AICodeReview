import openai
import os
import requests

# Set up OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

def fetch_pr_diff(pr_url):
    """Fetches the diff for a specific PR URL."""
    headers = {"Accept": "application/vnd.github.v3.diff"}
    response = requests.get(pr_url, headers=headers)
    return response.text if response.status_code == 200 else None

def analyze_code_with_codex(diff):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a code review assistant."},
            {"role": "user", "content": f"Please review the following code:\n{diff}"}
        ],
        max_tokens=150  # Adjust as needed
    )
    return response.choices[0].message['content']

def post_review_comment(repo, pr_number, comment):
    """Posts the Codex review comment to the PR on GitHub."""
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {"body": comment}
    requests.post(url, headers=headers, json=data)

# Main execution
pr_url = os.getenv("PR_URL")
repo = os.getenv("GITHUB_REPOSITORY")
pr_number = os.getenv("PR_NUMBER")

diff = fetch_pr_diff(pr_url)
if diff:
    review_comment = analyze_code_with_codex(diff)
    post_review_comment(repo, pr_number, review_comment)

