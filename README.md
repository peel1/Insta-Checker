# Insta-Checker

## Description 
Instagram Account checker that will check username/email:password to see if the account credentials are correct. Then it will write sucessful username:passwords to a file called Accounts.txt. 

# Notes
Proxys are mandatory because instagram will simply block you otherwise so the program would be useless without them.
## Proxys
### Proxys must be formated IP:Port and must be HTTPS. ANY slow results is solely based off proxy speed as multithreading means the program is able to check the response as soon as it arrives.

If the error "requests.exceptions.ProxyError: HTTPSConnectionPool(host='www.instagram.com', port=443): Max retries exceeded with url: /accounts/login/ajax/ (Caused by ProxyError('Cannot connect to proxy.', OSError('Tunnel connection failed: 403 Forbidden')))
" Arrives. This  error means there are not enough proxys and instagram has blacklisted that specific proxy due to overuse or the proxy being public and therfore other people have used it and instagram have blocked it due to their use. The program will pick proxys at complete random. A large proxy list (GBs) will cause the program to run slowly.
### recomended proxys 500-1000 
### max proxys: 10k

### Best cheap proxy provider + free proxys: https://bit.ly/2DPFwHI

## Installation
Linux + Windows:
```
  git clone https://github.com/peel1/Insta-Checker
  
  pip install requests
  
  pip install threading
  
  pip install itertools
  
  cd Insta-Checker
  
  python3 Checker.py
  
 ```

## Donate
Any donations would be very much appricate :)

Zcash : t1gpghwd8upq9ftPgbQSmsamQDdWdhyqGEj

Bitcoin : 37vhDPKUbaB14jKFBUB3bG8gq4dopBCE5C

Ethereum : 0x22f4532d2f6b73e33db1f05df9a55a83b7e7c716 


# Disclamer
THIS SOFTWARE IS FOR EDUCATIONAL USE ONLY THE OWNER TAKES NO RESPONSIBILITY FOR MALICIOUS USE OF THIS SOFTWARE OR MALICIOUS USE OF SOURCE-CODE
