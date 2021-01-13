import os
for top, dirs, files in os.walk('/Users/mrrobot/PycharmProjects/pythonProject1'):
    for nm in files:
        if os.path.getsize(os.path.join(top, nm)) < 1e+6:
            print(os.path.join(top, nm))
            
# /Users/mrrobot/PycharmProjects/pythonProject1/.DS_Store
# /Users/mrrobot/PycharmProjects/pythonProject1/1/extra.py
# /Users/mrrobot/PycharmProjects/pythonProject1/1/2.py
# /Users/mrrobot/PycharmProjects/pythonProject1/1/3.py
# /Users/mrrobot/PycharmProjects/pythonProject1/1/1.py
# /Users/mrrobot/PycharmProjects/pythonProject1/2/2.2-output.txt
# /Users/mrrobot/PycharmProjects/pythonProject1/2/2.py
# /Users/mrrobot/PycharmProjects/pythonProject1/2/2.1-input.txt
# /Users/mrrobot/PycharmProjects/pythonProject1/2/3.py
# /Users/mrrobot/PycharmProjects/pythonProject1/2/2.2-input.txt
# /Users/mrrobot/PycharmProjects/pythonProject1/2/1.py
# /Users/mrrobot/PycharmProjects/pythonProject1/2/2.1-output.txt
# /Users/mrrobot/PycharmProjects/pythonProject1/.idea/pythonProject1.iml
# /Users/mrrobot/PycharmProjects/pythonProject1/.idea/other.xml
# /Users/mrrobot/PycharmProjects/pythonProject1/.idea/.gitignore
# /Users/mrrobot/PycharmProjects/pythonProject1/.idea/workspace.xml
# /Users/mrrobot/PycharmProjects/pythonProject1/.idea/modules.xml
# /Users/mrrobot/PycharmProjects/pythonProject1/.idea/.name
# /Users/mrrobot/PycharmProjects/pythonProject1/.idea/misc.xml
# /Users/mrrobot/PycharmProjects/pythonProject1/.idea/inspectionProfiles/profiles_settings.xml
# /Users/mrrobot/PycharmProjects/pythonProject1/.idea/inspectionProfiles/Project_Default.xml