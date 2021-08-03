#include <iostream>
#include <stdio.h>
#include <vector>
#include <sys/stat.h>
#include "dir.h"
#include "dirent.h"

using namespace std;

int searchDir(const char* path, vector<string>& vpaths) {

    DIR* dir = opendir(path);
    struct dirent* ent;
    const char* tempPath;
    string tmp;
    string ntmp;

    if (!dir)
        return 1;

        while ((ent = readdir(dir)) != NULL) {
            struct stat file_info;
            stat(ent->d_name, &file_info);     

            if (S_ISDIR(file_info.st_mode)) {                
                if (strcmp(ent->d_name, ".") != 0 && strcmp(ent->d_name, "..") != 0){                                  
                    tmp = path;
                    ntmp = tmp + "/" + (ent->d_name);                   
  
                    if (ent->d_type == DT_REG) 
                    {                             
                        tmp = path;
                        ntmp = tmp + "/" + (ent->d_name);
                        tempPath = ntmp.c_str();  
                        vpaths.push_back(tempPath);
                         
                    }
                    else{                    
                    cout << ntmp <<endl;
                    tempPath = ntmp.c_str();
                    searchDir(tempPath, vpaths);
                    }
                }
            }
        }
    closedir(dir);
}