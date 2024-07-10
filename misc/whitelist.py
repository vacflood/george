import datetime

class Whitelist():
    def __init__(self) -> None:
        self.users = open('shittydb/users.txt').read().splitlines()
        self.admins = open('shittydb/admins.txt').read().splitlines()

    @staticmethod
    def check(username: str, checktype: str) -> None:
        whitelisted = False
        users = Whitelist().users
        admins = Whitelist().admins

        if checktype == 'user':
            for user in users:
                u = user.split(':')[0]
                if username == u:
                    whitelisted = True
        elif checktype == 'admin':
            for admin in admins:
                a = str(admin)
                if username == a:
                    whitelisted = True
        elif checktype == 'expiry':
            for user in users:
                u = user.split(':')[0]
                if username == u:
                    e = user.split(':')[1]
                    ed = datetime.datetime.strptime(e, "%Y-%m-%d").date()
                    if ed <= datetime.date.today():
                        return 'expired'
                    else:
                        return ed
        elif checktype == 'maxlfg':
            for user in users:
                u = user.split(':')[0]
                if username == u:
                    maxlfg = user.split(':')[2]
                    return maxlfg
        elif checktype == 'followers':
            for user in users:
                u = user.split(':')[0]
                if username == u:
                    followers = user.split(':')[3]
                    return followers
        else:
            return f'{checktype} is not a valid check-type'
        
        return whitelisted
        
    @staticmethod
    def adduser(adminuser: str, username: str, addtype: str, expiry: None, maxlfg: None, followers: None) -> None:
        if Whitelist.check(adminuser, 'admin') == True:
            if addtype == 'admin':
                open('shittydb/admins.txt','a+').write(f'{username}\n')
                return True
            elif addtype == 'user':
                open('shittydb/users.txt','a+').write(f'{username}:{expiry}:{maxlfg}:{followers}\n')
                return True
            else:
                return f'{addtype} is not a valid add-type'
        else:
            return False