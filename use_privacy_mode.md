### Files related to privacy mode

#### Sandboxie\core\drv\file.c

```c
    if (ok && proc->use_privacy_mode) { // in privacy mode all drive paths are set to "write"
        for (i = 0; drive_devices[i] && ok; ++i) {
            ok = Process_AddPath(proc, write_file_paths, NULL, 
                                    TRUE, drive_devices[i], FALSE);
        }
    }
```
#### Sandboxie\core\dll\file_dir.c
```c
//
    // in privacy mode we need to pre create some folders or else programs may fail
    //

    //File_CreateBoxedPath(File_SysVolume);
    // 
    //if (SbieApi_QueryConfBool(NULL, L"SeparateUserFolders", TRUE)) {
    //    File_CreateBoxedPath(File_AllUsers);
    //    File_CreateBoxedPath(File_CurrentUser);
    //}

    WCHAR* Folders[] = { L"SystemRoot", L"TEMP", L"USERPROFILE", //L"windir",
                        L"PUBLIC", L"ProgramData", L"LOCALAPPDATA", L"ALLUSERSPROFILE", L"APPDATA",
                        L"ProgramFiles", L"ProgramFiles(x86)", L"ProgramW6432",
                        //L"CommonProgramFiles", L"CommonProgramFiles(x86)", L"CommonProgramW6432", 
                        NULL };
```

#### Sandboxie\core\dll\key.c
```c
    WCHAR* base_keys[] = {
        L"\\machine\\system", L"\\machine\\software",
        L"\\user\\current\\software", L"\\user\\current_Classes",
        L"\\machine\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer",
        L"\\user\\current\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer",
        NULL};

    //
    // in privacy mode we need to pre create some keys or else the box initialization will fail
    //
```

#### Sandboxie\core\drv\process.c

```c
//
    // privacy mode requirers Rule Specificity
    //

    proc->use_security_mode = Conf_Get_Boolean(proc->box->name, L"UseSecurityMode", 0, FALSE);
    proc->is_locked_down = proc->use_security_mode || Conf_Get_Boolean(proc->box->name, L"SysCallLockDown", 0, FALSE);
#ifdef USE_MATCH_PATH_EX
    proc->restrict_devices = proc->use_security_mode || Conf_Get_Boolean(proc->box->name, L"RestrictDevices", 0, FALSE);

    proc->use_privacy_mode = Conf_Get_Boolean(proc->box->name, L"UsePrivacyMode", 0, FALSE); 
    proc->use_rule_specificity = proc->restrict_devices || proc->use_privacy_mode || Conf_Get_Boolean(proc->box->name, L"UseRuleSpecificity", 0, FALSE); 
#endif
    proc->confidential_box = Conf_Get_Boolean(proc->box->name, L"ConfidentialBox", 0, FALSE); 

```

#### Sandboxie\install\Templates.ini

```ini
#
# Access rules for privacy enhanced boxes
#

[TemplatePModPaths]
#NormalKeyPath=HKEY_LOCAL_MACHINE\*
#NormalKeyPath=HKEY_CURRENT_USER\software\Microsoft\*
#NormalKeyPath=HKEY_CURRENT_USER\software\WOW6432Node\Microsoft\*
#NormalKeyPath=\REGISTRY\USER\*_Classes\*
WriteKeyPath=\REGISTRY\USER\*
#
NormalFilePath=%SystemRoot%\*
NormalFilePath=%SbieHome%\*
NormalFilePath=%ProgramFiles%\*
NormalFilePath=%ProgramFiles% (x86)\*
NormalFilePath=%ProgramData%\Microsoft\*
# recycle bin
NormalFilePath=?:\$Recycle.Bin\*
WriteFilePath=?:\$Recycle.Bin\**\*
# shell & ui
NormalKeyPath=HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize\*
NormalKeyPath=HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders\*
NormalKeyPath=HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders\*
NormalKeyPath=HKEY_CURRENT_USER\SOFTWARE\Classes\*
NormalKeyPath=HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\ApplicationAssociationToasts\*
NormalKeyPath=HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced\*
NormalKeyPath=HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FileExts\*
NormalKeyPath=HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\FileAssociations\*
NormalKeyPath=HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\Shell\Associations\*
NormalKeyPath=HKEY_CURRENT_USER\AppEvents\*
NormalKeyPath=HKEY_CURRENT_USER\SOFTWARE\Microsoft\DirectX\UserGpuPreferences\*
NormalKeyPath=HKEY_CURRENT_USER\Environment\*

```

