def check_url(url):
    if url.startswith("http://www."):
        domain = url[len('http://www.'):]
        print("Converted URL: ", domain)
    else:
        print("URL doesn't start with http://www. Invalid!")

def main():
    url = input("Enter your url (example: http://www.example.com): ")
    check_url(url)
    
main()

