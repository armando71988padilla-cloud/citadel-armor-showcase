rule ARMOR_Review_Only_Dangerous_Action_Strings
{
    meta:
        description = "Review-only check for dangerous action strings in ARMOR source"
        severity = "medium"
        category = "source_safety"
        review_only = "true"
        action = "none"
    strings:
        $delete_1 = "os.remove(" nocase
        $delete_2 = "unlink(" nocase
        $delete_3 = "shutil.rmtree(" nocase
        $kill_1 = "kill -9" nocase
        $firewall_1 = "ufw deny" nocase
        $firewall_2 = "ufw reset" nocase
        $wifi_1 = "nmcli radio wifi off" nocase
        $bluetooth_1 = "rfkill block bluetooth" nocase
        $usb_1 = "usbguard" nocase
    condition:
        any of them
}

rule ARMOR_Review_Only_Private_Path_String
{
    meta:
        description = "Review-only check for hardcoded private local paths in tracked ARMOR source"
        severity = "low"
        category = "privacy_safety"
        review_only = "true"
        action = "none"
    strings:
        $home_path_pattern = /\/home\/[A-Za-z0-9._-]+/ nocase
    condition:
        any of them
}
