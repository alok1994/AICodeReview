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
    """Analyzes code diff with OpenAI Codex."""
    prompt = f"Review the following code changes and suggest improvements or fixes:\n\n{diff}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=500,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

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

