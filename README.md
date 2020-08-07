# Insta-Checker

## Description 
Instagram Account checker that will check username/email:password to see if the account credentials are correct. Then it will write sucessful username:passwords to a file called Accounts.txt. 

# Notes
## Proxys
Proxys must be formated IP:Port and must be HTTPS. ANY slow results is solely based off proxy speed as multithreading means the program is able to check the response as soon as it arrives. If the error "requests.exceptions.ProxyError: HTTPSConnectionPool(host='www.instagram.com', port=443): Max retries exceeded with url: /accounts/login/ajax/ (Caused by ProxyError('Cannot connect to proxy.', OSError('Tunnel connection failed: 403 Forbidden')))
" Arrives this means there are not enough proxys and instagram has blocked that specific proxy due to overuse the program will pick proxys at complete random. A large proxy list (GBs) will cause the program to run slowly.
### recomended proxys 1000 
### max proxys: 10k

### Installation
Linux:
 '''
  git clone https://github.com/peel1/Insta-Checker
  
  pip install requests
  
  pip install threading
  
  pip install itertools
  
  cd Insta-Checker
  
  python3 Checker.py
  
  '''


# Disclamer
THIS SOFTWARE IS FOR EDUCATIONAL USE ONLY THE OWNER TAKES NO RESPONSIBILITY FOR MALICIOUS USE OF THIS SOFTWARE OR MALICIOUS USE OF SOURCE-CODE
