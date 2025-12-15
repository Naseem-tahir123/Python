"""
Your junior developer wrote this code to back up user settings, but the backup keeps getting corrupted. Fix it. 
The Buggy Code: 
import copy 
# User settings with nested preferences 
default_settings = { 
"theme": "Dark", 
"notifications": {"email": True, "sms": False} 
} 
# The Junior Dev tries to make a backup 
user_1_settings = copy.copy(default_settings) 
# User 1 changes their SMS setting 
user_1_settings["notifications"]["sms"] = True 
# CHECK: Did default_settings change?  
print(default_settings["notifications"]["sms"])  
# It prints True! The default is ruined for everyone else! 
Your Task: 
Rewrite the line user_1_settings = ... using the correct copying method so that default_settings remains False.
"""

import copy

default_settings ={
    "theme":"Dark",
    "notifications":{'email':True, 'sms': False}
}

user1_settings = copy.deepcopy(default_settings)
user1_settings["notifications"]["sms"] = True
print(user1_settings["notifications"]["sms"])  # This should print True
print(default_settings["notifications"]['sms'])  # This should print False now 
# Now the default_settings remains unchanged


