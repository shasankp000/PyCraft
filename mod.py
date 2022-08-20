import requests
import os
import platform
import json
import wget



def downloadjar(url, path, filename):
    if platform.platform().startswith("Windows"):
        os.chdir(path)

        print(f"Downloading {filename}.....")

        remote_url = url
        local_file_name = filename

        data = requests.get(remote_url)

        # Save file data to local copy
        with open(local_file_name, 'wb')as file:
            file.write(data.content)
            print("Download complete")



    elif platform.platform().startswith("Linux"):
        os.chdir(path)
        os.system(f"wget {url}")





def downloadfromModrinth(modname, modloader, gameVersion):

    print(f"Searching Modrinth database for mod: {modname}, with loader {modloader} and game version {gameVersion}")


    search_url = f'https://api.modrinth.com/v2/project/{modname}/version?loaders=["{modloader}"]&game_versions=["{gameVersion}"]' #slug=modname
    #base_url = f'https://api.modrinth.com/v2/search?query={modname}&limit=20&index=downloads&facets=[["categories:{modloader}"],["versions:{gameVersion}"],["project_type:mod"]]'
    print(search_url)
    r = requests.get(search_url)

    if r.status_code == 200:

        print("OK [200], mod found, downloading.....")
        data = r.json()
        
        if data == []:
            print("Mod exists, but stable version not found")

        else:

            with open("mod_details.json", "w") as f:
                json.dump(data, f, indent=4)
                f.close()

            with open("mod_details.json", "r") as js_read:
                s1 = js_read.read()
                s1 = s1.replace('\t','')  #Trailing commas in dict cause file read problems, these lines will fix it.
                s1 = s1.replace('\n','')  #Found this on stackoverflow.
                s1 = s1.replace(',}','}')
                s1 = s1.replace(',]',']')
                data1 = json.loads(s1)

            fileurl = data1[0]["files"][0]["url"]
            print(fileurl)

            curn_dir = os.getcwd()

            filename = wget.detect_filename(fileurl)
            downloadjar(fileurl, curn_dir, filename=filename)

    else:
        print("Mod not found")



#downloadfromModrinth("hydrogen", "fabric", "1.19.2")
