import requests

def check_header(url):
    response = requests.get(url)
    issues = []

    if 'X-XSS-Protection' not in response.headers:
        issues.append(f"Missing X-XSS-Protection header on {url}")
    if 'Content-Security-Policy' not in response.headers:
        issues.append(f"Missing Content-Security-Policy header on {url}")
    if 'Strict-Transport-Security' not in response.headers:
        issues.append(f"Missing Strict-Transport-Security header on {url}")
    
    if issues:
        return f"Vulnerabilities found on {url}:\n" + "\n".join(issues)
    else:
        return f"No basic vulnerabilities found on {url}"

def run(url):
    result = check_header(url)
    return result

