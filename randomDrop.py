import requests
import random
import webbrowser

ACCESS_TOKEN = ''

def fetch_user():
    url = 'https://api.raindrop.io/rest/v1/user/stats'
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_page_drops(page):
    url = f'https://api.raindrop.io/rest/v1/raindrops/0?perpage=50&page={page}'
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
    response = requests.get(url, headers=headers)
    return response.json()

def random_raindrop():
    user_stats = fetch_user()
    print(f"User Stats: {user_stats}")

    user_total_drops = [
        item for item in user_stats['items'] if item['_id'] == 0][0]
    print(f"User Total Drops: {user_total_drops}")

    pages = user_total_drops['count'] // 50 + 1
    print(f"Pages: {pages}")

    random_page = random.randint(1, pages)
    print(f"Random Page: {random_page}")

    page_drops = get_page_drops(random_page)

    random_drop = random.choice(page_drops['items'])
    print(f"Random Drop: {random_drop}")

    return random_drop['link']


if __name__ == "__main__":
    random_drop_link = random_raindrop()
    print(f"Random Drop: {random_drop_link}")
    webbrowser.open(random_drop_link)

    # keep the window open
    input("Press Enter to continue...")
