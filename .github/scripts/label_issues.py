import os
import requests

def label_issue(issue_number, labels):
    repo_owner = os.environ['GITHUB_REPOSITORY'].split('/')[0]
    repo_name = os.environ['GITHUB_REPOSITORY'].split('/')[1]
    token = os.environ['GITHUB_TOKEN']
    headers = {'Authorization': f'token {token}'}
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{issue_number}/labels'

    response = requests.post(url, headers=headers, json={'labels': labels})
    if response.status_code == 200:
        print(f"Labels applied successfully: {labels}")
    else:
        print(f"Failed to apply labels. Status code: {response.status_code}, Response: {response.text}")

if __name__ == '__main__':
    issue_number = os.environ['ISSUE_NUMBER']
    issue_body = os.environ['ISSUE_BODY'].lower()

    # Your logic to determine labels based on issue content
    labels_to_apply = []

    if 'bug' in issue_body:
        labels_to_apply.append('bug')

    if 'feature' in issue_body:
        labels_to_apply.append('feature')

    # Apply labels to the issue
    label_issue(issue_number, labels_to_apply)
