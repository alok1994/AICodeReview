import requests
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def fetch_pr_diff(pr_url):
    """Fetches the diff for a specific PR URL."""
    headers = {"Accept": "application/vnd.github.v3.diff"}
    response = requests.get(pr_url, headers=headers)
    return response.text if response.status_code == 200 else None

def analyze_code_with_codex(diff):
    """Analyzes code diff with the latest OpenAI model."""
    prompt = f"Review the following code changes and suggest improvements or fixes:\n\n{diff}"
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # Use "gpt-3.5-turbo" if you prefer a less expensive option
        messages=[
            {"role": "system", "content": "You are an expert code reviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=500,
    )
    return response['choices'][0]['message']['content'].strip()
    
# def analyze_code_with_codex(diff):
#     # Mocked response to simulate API call
#     response = {
#         'choices': [{'message': {'content': 'Mocked response: Code review completed successfully.'}}]
#     }
#     return response['choices'][0]['message']['content']

def post_review_comment(pr_number, review_comment):
    github_token = os.getenv("PAT_TOKEN")
    print(github_token)
    repo = os.getenv("GITHUB_REPOSITORY")  # e.g., "username/repo-name"
    print(repo)
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"body": review_comment}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Review comment posted successfully.")
    else:
        print("Failed to post review comment:", response.json())

if __name__ == "__main__":
    diff = "Example diff text here"  # Replace this with actual diff text if applicable
    review_comment = analyze_code_with_codex(diff)
    pr_number = os.getenv("PR_NUMBER")  
    post_review_comment(pr_number, review_comment)
