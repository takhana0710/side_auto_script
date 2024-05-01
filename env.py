
"""
邏輯註解：
攥寫目的：為了多情況而做的多參數設定+未來多不同作業系統的參數設定
常見的三種命令：
python runAll.py dev
python main.py
2023/03/01 註解:
  1.因為接了智販機業務，將自動化系統給簡單專一化
  2.未來會做一個工作相關工具前後端網站去使用
2023/07/31 註解:
  1.因應方向改寫參數變成多站進行
  2.趁這次拔除redis
  3.分兩次進行
  4. env代號如下
    tw_prod : gpg正式
    tw_dev ： gpg測試
    ph ： xpg 菲律賓
    sp ： xpg 新加坡
    qa ssh 遠端
"""


def sys_parameter(check_env):  # 系統參數 for 防止循環引用
    if check_env == 'tw_prod':
        env = {'font_url': '', 'font_api': '',
                   'member_account': '',
                   'site_send':'',
                   'env': '',
                   'agent_account':'',
                   'agent_password':'',
                   'back_url': '',
                   'back_api': '',
                   'back_account': '', 'back_password': '', 'play_api': '',
                   'play_api_ids': '', 'retail_url': ''
                   }
    elif check_env=='ph':
        env = {'font_url': '', 'font_api': '',
                   'member_account': '','site_send':'',
                   'agent_account':'',
                   'agent_password':'',
                   'env': 'ph', 
                   'back_url': '',
                   'back_api': '',
                   'back_account': '',
                   'back_password': '',
                   'play_api': '',
                   'play_api_ids': '',
                     'retail_url': ''
                   }
    elif check_env == 'sp':
        env = {'font_url': '', 'font_api': '',
               'site_send':'',
                   'member_account': '',
                   'agent_account':'',
                   'agent_password':'',
                   'env': 'sp', 'back_url': '',
                   'back_api': '',
                   'back_account': '',
                   'back_password': '',
                   'play_api': '',
                   'play_api_ids': '',
                   'retail_url': ''
                   }
    else:
        env = {'font_url': '', 'font_api': '',
                'member_account': '',
                'env': 'tw_dev', 'site_send':'',
                'agent_account':'',
                'agent_password':'',
                'back_url': '',
               'back_api': '',
               'back_account': '', 'back_password': '', 'play_api': '',
               'play_api_ids': '', 'retail_url': ''
               }
    return  env
