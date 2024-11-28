import requests
import os

def analyze_code_with_codex(diff):
    # Mocked response to simulate API call
    response = {
        'choices': [{'message': {'content': 'Mocked response: Code review completed successfully. with AI'}}]
    }
    return response['choices'][0]['message']['content']


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
